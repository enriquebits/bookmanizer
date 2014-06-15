# -*- coding: utf-8 -*-
"""Sample controller module"""

# turbogears imports
from tg import expose

from tg import redirect, validate, flash, request
#from tg.i18n import ugettext as _
#from tg import predicates

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
    
    @expose('pegasus.templates.logged_index')
    def index(self):
        user = request.identity['user']
    	if len(user.categories) == 0:
    		links = model.Link.get_all(None)
    		return dict(resp=links, op=1)
    	else:
    		links = model.Category.categorias_usuario(user.id)
    		return dict(resp=links, op=2)

    """@expose('pegasus.templates.logged_index')
    def about(self):
    	user = request.identity['user']
    	responde = ""
    	if len(user.categories) == 0:
    		responde = 'No hay nada'
    	else:
    		responde = 'Si tiene categorias'
    	return dict(page='Resultado', values=responde)"""
