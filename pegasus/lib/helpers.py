# -*- coding: utf-8 -*-

"""WebHelpers used in pegasus."""

#from webhelpers import date, feedgenerator, html, number, misc, text
from markupsafe import Markup
from datetime import datetime
from pegasus import model

def current_year():
  now = datetime.now()
  return now.strftime('%Y')

def icon(icon_name):
    return Markup('<i class="glyphicon glyphicon-%s"></i>' % icon_name)

def link(link_id):
	return model.Link.get_by_id(link_id)
