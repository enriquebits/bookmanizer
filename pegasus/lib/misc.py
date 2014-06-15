# -*- coding: utf-8 -*-
""" Misc tools library for Autogenio """
import tg
import logging
log = logging.getLogger(__name__)
from pegasus import model
    
def getUser(request):
    """ 
    Return current local user
    @param session request
    @return user or None
    """
    if request.identity:
        identity = request.environ.get('repoze.who.identity')
        #log.debug("identity: %s", identity['repoze.who.userid'])
        user = model.User.by_user_name(identity['repoze.who.userid'])
        return user
    else:
        return None
        
def forceUser(user_name):
    """ 
    Force authentication 
    @param user_name
    """
    request = tg.request
    response = tg.response

    request.cookies.clear()
    authentication_plugins = request.environ['repoze.who.plugins']
    identifier = authentication_plugins['main_identifier']

    try:
        response.headers = identifier.remember(request.environ, {'repoze.who.userid':user_name})
    except:
        pass