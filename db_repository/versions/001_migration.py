from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
Books = Table('Books', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('book', VARCHAR),
    Column('author_id', INTEGER),
    Column('genres', VARCHAR),
)

books = Table('books', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('book', String),
    Column('author_id', Integer),
    Column('genres', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['Books'].drop()
    post_meta.tables['books'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['Books'].create()
    post_meta.tables['books'].drop()
