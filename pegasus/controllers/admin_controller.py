# -*- coding: utf-8 -*-
"""Sample controller module"""

# turbogears imports
from tg import expose

from tg import redirect, validate, flash, request
#from tg.i18n import ugettext as _
from tg import predicates

from tg.i18n import ugettext as _, lazy_ugettext as l_

# project specific imports
from pegasus.lib.base import BaseController
from pegasus import model

from sqlalchemy import update

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
		user = request.identity['user']
		return dict(page='index', usuario=user)

	@expose('pegasus.templates.edit')
	def edit(self):
		user = request.identity['user']
		return dict(page='soy la de edicion', usuario=user)

	@expose()
	def cambia_pass(self, **kw):
		"""
		User register
		"""
		user = request.identity['user']
		log.debug("Recibiendo de registro %s", kw)

		if user.validate_password(kw.get('old_pass', None)):
			# Persisting
			
			user.password = kw.get('new_pass', None)
			model.DBSession.add(user)

			model.DBSession.flush()

			flash(_(u'Ya fue actualizada su contraseña'))
			redirect('/index')
		else:
			flash(_(u'No se encuentra la vieja contraseña'))
			redirect('/index')
			
	@expose()
	def cambia_nombre(self,**kw):
		user=request.identity['user']
		display=kw.get('nombre',None)+" "+kw.get('apellido',None)
		user.display_name=display
		model.DBSession.add(user)
		model.DBSession.flush()
		flash(_(u'Se ha actualizado el nombre'))
		redirect('/index')
