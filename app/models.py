from app import db
from datetime import date
from sqlalchemy import ForeignKey


ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
	__tablename__ = 'Users'
	id = db.Column(db.Integer, primary_key = True)
	login = db.Column(db.String, index = True, unique = True)
	password = db.Column(db.String, unique = False)
	role = db.Column(db.SmallInteger, default = ROLE_USER)
	
	def __repr__(self):
		return '<User %r>' % (self.login)
	
class Authors(db.Model):
	__tablename__ = 'Authors'
	id = db.Column(db.Integer, primary_key = True)
	author = db.Column(db.String, index= True, unique = True)
	date = db.Column(db.Date)
	books = db.relationship('Books', backref='writer', lazy='dynamic')

	def __repr__(self):
		return '<Authors %s>'% (self.author)

	def add_author(self):
        	db.session.add(self)
        	db.session.commit()
        	return 'Success! Poll created'
	
class Books(db.Model):
	__tablename__ = 'Books'
	id = db.Column(db.Integer, primary_key = True)
	book = db.Column(db.String, index = True, unique = True)
	author_id = db.Column(db.Integer, db.ForeignKey('Authors.id'))
	genres = db.Column(db.String)
	
	def __repr__(self):
		return '<Books %r>' % (self.book)