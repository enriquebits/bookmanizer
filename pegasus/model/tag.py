# -*- coding: utf-8 -*-
"""Tag model module."""

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode
#from sqlalchemy.orm import relation, backref

from pegasus.model import DeclarativeBase, metadata, DBSession

# log imports
import re
import logging
log = logging.getLogger(__name__)


class Tag(DeclarativeBase):
    __tablename__ = 'tag'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    
    #{ Columns
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    name = Column(Unicode(64))

    # }

    # Special methods { 
    
    def __repr__(self):
    	return ("<Tag: id=%s, name=%s>" % \
    			(self.id, self.name)).encode('utf-8')

    def __unicode__(self):
    	return self.name
    
    # }

    # Helpers {
   	
   	@property
   	def to_json(self):
   		return {'id': self.id, 'name': self.name}
    
    @classmethod
    def get_by_id(cls, id):
    	return DBSession.query(cls).filter(cls.id==id).first()

    @classmethod
    def get_all(cls):
    	return DBSession.query(cls).order_by(cls.name).all()

    @classmethod
    def get_tags_by_name(cls, name):
        name = '%'+name+'%'
        return DBSession.query(cls).filter(cls.name.like(name)).limit(10)

    @classmethod
    def links_tag_id(cls, tags=None, pag=None):
        log.debug("Recibe: %s\n", tags)
        log.debug("Numero de registros: %s\n", pag)
        lista = []
        links = []
        if pag==1:
            lista = DBSession.query(cls).filter(cls.id.in_(tags)).offset(0).limit(16).all()
        else:
            lista = DBSession.query(cls).filter(cls.id.in_(tags)).offset(16*pag).limit(32*pag).all()
        
        for t in lista:
            if len(t.tags_links) < 16-len(links):
                links.append(t.tags_links)
            else:
                break
        return links

    # }






