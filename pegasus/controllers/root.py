# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, lurl, request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_

from pegasus.lib.base import BaseController
from pegasus.controllers.error import ErrorController

""" TUTORIAL: TODOS los controladores nuevos tienen que importarse aquí con la siguiente sintaxis:
    from direccion.del.archivo_controlador import NombreDeLaClaseDelControlador: """
from pegasus.controllers.sample_controller import SampleController

__all__ = ['RootController']


class RootController(BaseController):
    """ 
    The root controller for the example application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """

    error = ErrorController()

    """ TUTORIAL: además deben instanciarse con el nombre desde el cual se quiera acceder en la URL,
    en este caso para acceder a las páginas del controlador SampleController se escribirá en la URL: localhost:XXXX/sample """
    sample = SampleController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "example"

    @expose('pegasus.templates.index')
    def index(self):
        """Handle the front-page."""
        return dict(page='index')

    @expose('pegasus.templates.about')
    def about(self):
        """Handle the 'about' page."""
        return dict(page='about')

    @expose('pegasus.templates.environ')
    def environ(self):
        """This method showcases TG's access to the wsgi environment."""
        return dict(page='environ', environment=request.environ)

    @expose('pegasus.templates.data')
    @expose('json')
    def data(self, **kw):
        """This method showcases how you can use the same controller for a data page and a display page"""
        return dict(page='data', params=kw)
