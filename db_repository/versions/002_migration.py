from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
Authors = Table('Authors', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('author', VARCHAR),
    Column('date', DATE),
)

authors = Table('authors', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('author', String),
    Column('date', Date),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['Authors'].drop()
    post_meta.tables['authors'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['Authors'].create()
    post_meta.tables['authors'].drop()
