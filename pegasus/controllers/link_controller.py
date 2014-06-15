# -*- coding: utf-8 -*-
"""Link controller module"""

# turbogears imports
from tg import expose, predicates

from tg import redirect, validate, flash, request
from tg.i18n import ugettext as _
#from tg import predicates

# project specific imports
from pegasus.lib.base import BaseController
from pegasus.lib.misc import getUser
from pegasus.model import DBSession, metadata
from pegasus import model

import re
import logging
log = logging.getLogger(__name__)

class LinkController(BaseController):
    allow_only = predicates.not_anonymous(msg='El usuario debe de estar autentificado')
    
    @expose('pegasus.templates.link')
    def index(self, **kw):
        return dict(page='Index de LinkController')

    @expose('pegasus.templates.link_form')
    def add(self):
        return dict(page='Add Link')

    @expose('pegasus.templates.link')
    def add_post(self, **kw):
    	user = request.identity['user']
    	log.debug("Recibiendo para post link: %s \n", kw)

    	url = kw['link']
    	tags = kw['tags_input'].split(',')
        log.debug("Tags: %s\n", tags)

        newLink = model.Link()
        newLink.url = url
        newLink.user_id = user.id

        model.DBSession.add(newLink)

        for t in tags:
        	try:
        		tag_id = int(t)
        		thisTag = model.Tag.get_by_id(tag_id)
        		newLink.tags.append(thisTag)
        	except ValueError:
        		newTag = model.Tag()
        		newTag.name = t
        		model.DBSession.add(newTag)
        		newLink.tags.append(newTag)

        model.DBSession.flush()
        flash(_('Your link has been added!!'))
        redirect('/dashboard')

    @expose('json')
    def like(self, **kw):
        log.debug("Recibiendo de like %s", kw)
        link_id = kw.get('lid', None)
        is_liked = kw.get('isLiked', None)
        link = model.Link.get_by_id(link_id)
        response = dict()
        
        if link: 
            if int(is_liked) == 1:
                link.likes += 1
                link.is_liked = True

                if link.is_disliked:
                    link.dislikes -= 1
                    link.is_disliked = None
                
                model.DBSession.add(link)
                model.DBSession.flush()
                response["liked"] = "true"
            else:
                link.likes -= 1
                link.is_liked = None
                model.DBSession.add(link)
                model.DBSession.flush()
                response["liked"] = "null"

        import json
        return json.dumps(response)

    @expose('json')
    def dislike(self, **kw):
        log.debug("Recibiendo de dislike %s", kw)
        link_id = kw.get('lid', None)
        is_disliked = kw.get('isDisliked', None)
        link = model.Link.get_by_id(link_id)
        response = dict()
        
        if link: 
            if int(is_disliked) == 1:
                link.dislikes += 1
                link.is_disliked = True

                if link.is_liked:
                    link.flags -= 1
                    link.is_liked = None

                model.DBSession.add(link)
                model.DBSession.flush()
                response["disliked"] = "true"
            else:
                link.dislikes -= 1
                link.is_disliked = None
                model.DBSession.add(link)
                model.DBSession.flush()
                response["disliked"] = "null"

        import json
        return json.dumps(response)

    @expose('json')
    def favourite(self, **kw):
        log.debug("Recibiendo de favourite %s", kw)
        link_id = kw.get('lid', None)
        is_favourite = kw.get('isFavourite', None)
        link = model.Link.get_by_id(link_id)
        user = getUser(request)
        response = dict()
        
        if link: 
            if int(is_favourite) == 1:
                link.flags -= 1
                link.is_flagged = None
                model.DBSession.add(link)
                model.DBSession.flush()
                user.favourite_links.append(link)
                model.DBSession.add(user)
                model.DBSession.flush()
                response["favourite"] = "true"
            else:
                user.favourite_links.remove(link)
                model.DBSession.add(user)
                model.DBSession.flush()
                response["favourite"] = "null"

        import json
        return json.dumps(response)

    @expose('json')
    def flag(self, **kw):
        log.debug("Recibiendo de flag %s", kw)
        link_id = kw.get('lid', None)
        is_flagged = kw.get('isFlagged', None)
        link = model.Link.get_by_id(link_id)
        user = getUser(request)
        response = dict()
        
        if link: 
            if int(is_flagged) == 1:
                link.flags += 1
                link.is_flagged = True
                model.DBSession.add(link)
                model.DBSession.flush()
                user.favourite_links.remove(link)
                model.DBSession.add(user)
                model.DBSession.flush()
                response["flagged"] = "true"
            else:
                link.flags -= 1
                link.is_flagged = None
                model.DBSession.add(link)
                model.DBSession.flush()
                response["flagged"] = "null"

        import json
        return json.dumps(response)

