# -*- coding: utf-8 -*-
"""Category model module."""
from datetime import datetime
from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime
#from sqlalchemy.orm import relation, backref

from pegasus.model import DeclarativeBase, metadata, DBSession

class Category(DeclarativeBase):
    __tablename__ = 'category'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    
    #{ Columns
    
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(Unicode(64))
    
    #}

    # Special methods { 
    
    def __repr__(self):
    	return ("<Category: id=%s, name=%s>" % \
    			(self.id, self.name)).encode('utf-8')

    def __unicode__(self):
    	return self.name
    #}

    # Helpers {
    
    @property
    def to_json(self):
        return {self.id, self.name}
    
    @classmethod
    def get_by_id(cls, id):
        return DBSession.query(cls).filter(cls.id==id).first()

    @classmethod
    def get_all(cls):
        return DBSession.query(cls).order_by(cls.name).all()

    # }






