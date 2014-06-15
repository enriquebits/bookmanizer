# -*- coding: utf-8 -*-
"""Sample controller module"""

# turbogears imports
from tg import expose

from tg import redirect, validate, flash, request
#from tg.i18n import ugettext as _
from tg import predicates

# project specific imports
from pegasus.lib.base import BaseController

from pegasus import model


from pegasus import model
""" con DBSession se puede acceder a las tablas para hacer consultas, ediciones, altas, bajas, etc """
from pegasus.model import DBSession, metadata

""" esto se usa para mostrar logs en la consola (como en post_form) """
# log imports
import re
import logging
log = logging.getLogger(__name__)


class DashboardController(BaseController):
    allow_only = predicates.not_anonymous()
    
    @expose('pegasus.templates.logged_index')
    def index(self):
    	user = request.identity['user']
    	if len(user.categories) == 0:
    		links=[]
    		return dict(resp=links, op=1)
    	else:
    		links = model.Category.categorias_usuario(user.id)
        	return dict(resp=links, op=2)

    @expose('pegasus.templates.search_results')
    def search(self, **kw):
        results = []
        log.debug("Recibiendo para results: %s \n", kw)
        results = map(int, kw['tags'].split(','))
        log.debug("Indices: %s\n", results)
        links = model.Tag.links_tag_id(results, 1)
        #links = model.Link.links_id(results, 1)
        #log.debug("Links: %s\n", tags.tags_links)
        #query = kw.get()
        # do results
        return dict(page='Resultados', links=links, tags=kw['tags'])

    @expose('json')
    def search_ajax(self, **kw):
        results = []
        log.debug("Recibiendo para results: %s \n", kw)
        results = map(int, kw['tags'].split(','))
        pagina = int(kw['page'])
        log.debug("Indices: %s\n", results)
        links= model.Tag.links_tag_id(results, pagina)
        #links = model.Link.links_id(results, pagina)
        #log.debug("Links: %s\n", tags.tags_links)
        #query = kw.get()
        # do results
        return dict(page='Resultados', links=links, tags=kw['tags'])

    @expose('json')
    def get_tags(self, **kw):
        log.debug("Recibiendo para tags: %s \n", kw)
        query = kw.get(u"q", None)

        import json
        results = dict()
        results['results'] = list()   
        # do results
        for tag in model.Tag.get_tags_by_name(query):
            results['results'].append( {'id': tag.id, 'text': tag.name} )
        log.debug("TAG: %s \n", results)
        return json.dumps(results)
