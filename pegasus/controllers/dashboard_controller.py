# -*- coding: utf-8 -*-
"""Sample controller module"""

# turbogears imports
from tg import expose

from tg import redirect, validate, flash
#from tg.i18n import ugettext as _
#from tg import predicates

# project specific imports
from pegasus.lib.base import BaseController

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
        return dict(page='Index de SampleController')
