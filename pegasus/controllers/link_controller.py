# -*- coding: utf-8 -*-
"""Link controller module"""

# turbogears imports
from tg import expose, predicates

from tg import redirect, validate, flash, request
from tg.i18n import ugettext as _
#from tg import predicates

# project specific imports
from pegasus.lib.base import BaseController
from pegasus.model import DBSession, metadata
from pegasus import model

import re
import logging
log = logging.getLogger(__name__)

class LinkController(BaseController):
    allow_only = predicates.not_anonymous(msg='El usuario debe de estar autentificado')
    
    @expose('pegasus.templates.link')
    def index(self):
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
