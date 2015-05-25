# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, lurl, request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_

from pegasus import model
from pegasus.lib.base import BaseController
from pegasus.lib.misc import forceUser
from pegasus.controllers.error import ErrorController
from pegasus.controllers.dashboard_controller import DashboardController
from pegasus.controllers.admin_controller import AdminController
from pegasus.controllers.link_controller import LinkController

import logging
log = logging.getLogger(__name__)


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
    dashboard = DashboardController()
    link = LinkController()
    admin = AdminController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "Pegasus"

    @expose('pegasus.templates.index')
    def index(self):
        """Handle the front-page."""
        if request.identity:
            redirect('/dashboard')
        return dict(page='index')

    @expose('pegasus.templates.about')
    def about(self):
        """Handle the 'about' page."""
        return dict(page='about')

    @expose('pegasus.templates.environ')
    def environ(self):
        """This method showcases TG's access to the wsgi environment."""
        return dict(page='environ', environment=request.environ)

    @expose('pegasus.templates.login')
    def login(self, came_from=lurl('/'), **kw):
        login_counter = request.environ.get('repoze.who.logins', 0)

        if login_counter > 0:
            flash(_('Wrong credentials'), 'warning')

        return dict(page='login', login_counter=str(login_counter),
                    came_from=came_from)

    @expose()
    def post_login(self, came_from=lurl('/')):
        """
        Redirect the user to the initially requested page on successful
        authentication or redirect her back to the login page if login failed.

        """
        if not request.identity:
            login_counter = request.environ.get('repoze.who.logins', 0) + 1
            redirect('/login',
                params=dict(came_from=came_from, __logins=login_counter))
        else:
            userid = request.identity['user']
            flash(_('Welcome back, %s!') % userid)
            redirect(came_from)

    @expose()
    def post_logout(self, came_from=lurl('/')):
        """
        Redirect the user to the initially requested page on logout and say
        goodbye as well.

        """
        flash(_('We hope to see you soon!'))
        redirect(came_from)

    @expose()
    def register(self, **kw):
        """
        User register
        """
        log.debug("Recibiendo de registro %s", kw)
        if request.identity:
            redirect('/')

        """ Adding new user """
        user = model.User()
        user.email_address = kw.get('email', None)
        user.password = kw.get('password', None)
        user.user_name = kw.get('username', None)
        model.DBSession.add(user)

        # Persisting
        from sqlalchemy.exc import IntegrityError
        try:
            model.DBSession.flush()
            forceUser(user.user_name)
            flash(_(u'Bienvenido %s, su cuenta ha sido creada con éxito' % user.user_name), 'alert alert-success')
            redirect('/')
        except IntegrityError as e:
            log.debug('Error:', e)
            model.DBSession.rollback()
            if e.orig[0] == 1062: 
                # User register already exits
                flash(_('Parece que ya tienes cuenta'))
                redirect('/login')
            else:
                raise  

    @expose('pegasus.templates.data')
    @expose('json')
    def data(self, **kw):
        """This method showcases how you can use the same controller for a data page and a display page"""
        return dict(page='data', params=kw)
