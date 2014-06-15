# -*- coding: utf-8 -*-

"""WebHelpers used in pegasus."""

#from webhelpers import date, feedgenerator, html, number, misc, text
from tg import request
from markupsafe import Markup
from datetime import datetime
from pegasus.lib.misc import getUser
from pegasus import model
from pegasus.model import DBSession, metadata

def current_year():
  now = datetime.now()
  return now.strftime('%Y')

def icon(icon_name):
    return Markup('<i class="glyphicon glyphicon-%s"></i>' % icon_name)

def link(link_id):
	return model.Link.get_by_id(link_id)

def like_link(link):
	link.likes += 1
	model.DBSession.add(link)
	model.DBSession.flush()

def dislike_link(link):
	link.dislike += 1
	model.DBSession.add(link)
	model.DBSession.flush()

def favourite_link(link):
	user = getUser(request)
	user.favourites.append(link)
	model.DBSession.add(user)
	model.DBSession.flush()