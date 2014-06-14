# -*- coding: utf-8 -*-
"""Sample model module."""

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode
#from sqlalchemy.orm import relation, backref

from pegasus.model import DeclarativeBase, metadata, DBSession

""" Esta clase representa una tabla en la base de datos (principio de ORM) de nombre sample_model.
Todas las nuevas clases/tablas deben darse de alta en model/__init__.py como si fueran controladores
Cada que se creen nuevas tablas hay que volver a generar a la base de datos con gearbox setup-app
Si se pone imbécil le dan DROP a mano y la vuelven a crear y otra vez gearbox jajajaja"""


class SampleModel(DeclarativeBase):
    __tablename__ = 'sample_model'
    
    #{ Columns
    """ Cada atributo de la clase es una columna, para saber más ver la doc de sqlalchemy """
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    name = Column(Unicode(255), nullable=False)

    description = Column(Unicode(255))

    checkbox = Column(Boolean)

    radio_option = Column(Unicode(255))

    select_option = Column(Unicode(255))
    
    #}

    @classmethod
    def by_id(cls, my_id):
        """Return the sample_model object whose id is ``id``."""
        return DBSession.query(cls).filter_by(id=my_id).first()
