import sys
from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, StringField, SubmitField# DateField #Validators
from wtforms.fields import DateField
from wtforms.validators import Required
#from wtforms.fields.html5 import DateField


class LoginForm(FlaskForm):
		login = TextField('login', validators = [Required()])
		password = TextField ('password', validators = [Required()])
		remember_me = BooleanField('remember_me', default = False)


class AddAuthor(FlaskForm):
	author_name = StringField('AddAuthor', validators = [Required()])
	author_date = DateField('Date', validators = [Required()])
	submit = SubmitField("Submit")

class AddBook(FlaskForm):
	book_name = StringField('book_name', validators = [Required()])
	book_author = StringField('book_author', validators = [Required()])
	book_genre = StringField('book_genre', validators = [Required()])
	submit = SubmitField("Submit")

class EditBook(Form):
    book_name = StringField('book_name', validators = [Required()])
	book_author = StringField('book_author', validators = [Required()])
	book_genre = StringField('book_genre', validators = [Required()])
	submit = SubmitField("Submit")