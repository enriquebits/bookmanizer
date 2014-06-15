# -*- coding: utf-8 -*-
"""Link controller module"""

# turbogears imports
from tg import expose, predicates

from tg import redirect, validate, flash
#from tg.i18n import ugettext as _
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
