# -*- coding: utf-8 -*-
"""Setup the pegasus application"""
from __future__ import print_function
import sys
import logging
from tg import config
import transaction

def setup_schema(command, conf, vars):
    """Place any commands to setup pegasus here"""
    # Load the models

    # <websetup.websetup.schema.before.model.import>
    from pegasus import model
    if 'nose' not in sys.modules:
        confirm = raw_input("Destroy actual database? ([yes]/no) ")
        if confirm == "yes" or confirm == "":
            print("Destroying previous databases")
            model.metadata.drop_all(bind=config['pylons.app_globals'].sa_engine)
        else:
            print("Keeping database...")
    
    # <websetup.websetup.schema.before.metadata.create_all>
    print("Creating tables")
    model.metadata.create_all(bind=config['tg.app_globals'].sa_engine)
    # <websetup.websetup.schema.after.metadata.create_all>
    transaction.commit()
    print('Initializing Migrations')
    import alembic.config, alembic.command
    alembic_cfg = alembic.config.Config()
    alembic_cfg.set_main_option("script_location", "migration")
    alembic_cfg.set_main_option("sqlalchemy.url", config['sqlalchemy.url'])
    alembic.command.stamp(alembic_cfg, "head")
