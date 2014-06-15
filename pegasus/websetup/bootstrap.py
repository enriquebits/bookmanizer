# -*- coding: utf-8 -*-
"""Setup the pegasus application"""
from __future__ import print_function

import logging
from tg import config
from pegasus import model
import transaction
import random

def categories():
    manager = model.User.by_user_name("manager")
    categories = [
        (1, u"Cocina"),
        (2, u"Artes"),
        (3, u"Ciencia"),
        (4, u"Educación"),
        (5, u"Humanidades"),
        (6, u"Computación"),
        (7, u"Finanzas"),
        (8, u"Deportes"),
        (9, u"Tecnología")
    ]

    for c in categories:
        category = model.Category()
        category.id = c[0]
        category.name = c[1]
        category.user_id = manager.id
        model.DBSession.add(category)

def links():
    links = [
        # url, category_id, likes, dislikes, flags
        (1, "http://www.muylinux.com/", 5, 2, 0, 0),
        (2, "http://openlibrary.org/", 4, 2, 0, 0),
        (3, "http://buscaebooks.blogspot.mx/", 4, 2, 0, 0),
        (4, "http://bitelia.com/", 9, 2, 0, 0),
        (5, "http://www.bignerdranch.com/index", 6, 2, 0, 0)
    ]

    tags_db = model.Tag.get_all()

    for l in links:
        link = model.Link()
        link.id = l[0]
        link.url = l[1]
        link.category_id = l[2]
        link.likes = l[3]
        link.dislikes = l[4]
        link.flags = l[5]
        tags = random.sample(tags_db, 2)
        link.tags.extend(tags)
        model.DBSession.add(link)

def tags():
    tags = [
        (1, u"Tecnología"),
        (2, u"Linux"),
        (3, u"Libros"),
        (4, u"E-books"),
        (5, u"Tecnología"),
        (6, u"Gadgets"),
        (7, u"Nerd"),
        (8, u"Software")
    ]

    for t in tags:
        tag = model.Tag()
        tag.id = t[0]
        tag.name = t[1]
        model.DBSession.add(tag)

def bootstrap(command, conf, vars):
    """Place any commands to setup pegasus here"""

    # <websetup.bootstrap.before.auth
    from sqlalchemy.exc import IntegrityError
    try:
        u = model.User()
        u.user_name = 'manager'
        u.display_name = 'Example manager'
        u.email_address = 'manager@somedomain.com'
        u.password = 'managepass'
    
        model.DBSession.add(u)
    
        g = model.Group()
        g.group_name = 'managers'
        g.display_name = 'Managers Group'
    
        g.users.append(u)
    
        model.DBSession.add(g)
    
        p = model.Permission()
        p.permission_name = 'manage'
        p.description = 'This permission give an administrative right to the bearer'
        p.groups.append(g)
    
        model.DBSession.add(p)
    
        u1 = model.User()
        u1.user_name = 'editor'
        u1.display_name = 'Example editor'
        u1.email_address = 'editor@somedomain.com'
        u1.password = 'editpass'
    
        model.DBSession.add(u1)
        model.DBSession.flush()
        transaction.commit()
    except IntegrityError:
        print('Warning, there was a problem adding your auth data, it may have already been added:')
        import traceback
        print(traceback.format_exc())
        transaction.abort()
        print('Continuing with bootstrapping...')

    # <websetup.bootstrap.after.auth>
    transaction.begin()
    # categories
    categories()
    # tags
    tags()

    model.DBSession.flush()

    transaction.commit()

    transaction.begin()
    # links
    links()

    model.DBSession.flush()

    transaction.commit()
