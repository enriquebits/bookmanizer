# -*- coding: utf-8 -*-
"""Link model module."""
from datetime import datetime
from sqlalchemy import *
from sqlalchemy.orm import mapper, relationship
from sqlalchemy import Table, ForeignKey, Column, or_
from sqlalchemy.types import Integer, Unicode, DateTime
#from sqlalchemy.orm import relation, backref

from pegasus.model import DeclarativeBase, metadata, DBSession

import re
import logging
log = logging.getLogger(__name__)

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
    
    id = Column(Integer, primary_key=True, autoincrement=True)

    category_id = Column(Integer, ForeignKey('category.id'))

    user_id = Column(Integer, ForeignKey('tg_user.id'))
    
    url = Column(Unicode(255))

    description = Column(Unicode(128))

    created_date = Column(DateTime, default=datetime.now())

    likes = Column(Integer)

    dislikes = Column(Integer)

    flags = Column(Integer)

    is_liked = Column(Boolean, nullable=True)

    is_disliked = Column(Boolean, nullable=True)

    is_flagged = Column(Boolean, nullable=True)
    
    #}

    # Relations { 

    tags = relationship('Tag', secondary=link_tag_table, backref='tags_links')
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

    @classmethod
    def links_id(cls, tags=None, pag=None):
        log.debug("Recibe: %s\n", tags)
        log.debug("Numero de registros: %s\n", pag)
        if pag==1:
            return DBSession.query(cls).join("tags_links").filter(Tag.id.in_(tags)).offset(0).limit(16).all()
        else:
            return DBSession.query(cls).join("tags_links").filter(Tag.id.in_(tags)).offset(16*pag).limit(32*pag).all()

    # }



        





