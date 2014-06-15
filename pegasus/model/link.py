# -*- coding: utf-8 -*-
"""Link model module."""
from datetime import datetime
from sqlalchemy import *
from sqlalchemy.orm import mapper, relationship
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode, DateTime
#from sqlalchemy.orm import relation, backref

from pegasus.model import DeclarativeBase, metadata, DBSession

link_tag_table = Table('aux_link_tag', metadata,
    Column('link_id', Integer, ForeignKey('link.id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tag.id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
)

class Link(DeclarativeBase):
    __tablename__ = 'link'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    
    #{ Columns
    
    id = Column(Integer, primary_key=True)

    category_id = Column(Integer, ForeignKey('category.id'))

    user_id = Column(Integer, ForeignKey('tg_user.id'))
    
    url = Column(Unicode(255))

    description = Column(Unicode(128))

    created_date = Column(DateTime, default=datetime.now())

    likes = Column(Integer)

    dislikes = Column(Integer)

    flags = Column(Integer)
    
    #}

    # Relations { 

    tags = relationship('Tag', secondary=link_tag_table)
    category = relationship('Category', backref='links')

    #}

    # Special methods { 
    
    def __repr__(self):
    	return ("<Link: id=%s, url=%s>" % \
    			(self.id, self.url)).encode('utf-8')

    def __unicode__(self):
    	return self.url
    #}

    # Helpers {
    
    @property
    def to_json(self):
        return {self.id, self.url}
    
    @classmethod
    def get_by_id(cls, id):
        return DBSession.query(cls).filter(cls.id==id).first()

    @classmethod
    def get_all(cls, category_id=None):
        if category_id:
            return DBSession.query(cls).filter(cls.category_id==category_id)\
                        .order_by(cls.created_date).all()
        return DBSession.query(cls).order_by(cls.url).all()

    # }



        





