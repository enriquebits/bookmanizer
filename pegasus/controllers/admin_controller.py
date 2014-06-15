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


class AdminController(BaseController):
    allow_only = predicates.not_anonymous()

    @expose('pegasus.templates.admin')
    def index(self):
        return dict(page='index')

    @expose('pegasus.templates.admin')
    def admin(self):
        return dict(page='index')