from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from forms import AddAuthor, AddBook, EditBook
import models


@app.route('/')
@app.route('/index')
def index(): 
	return render_template("index.html",
							title = 'Library',
							authors = models.Authors.query.count(),
							book = models.Books.query.count())



						
@app.route('/books', methods = ['GET', 'POST'])
def books():
	return render_template("books.html",
							title = 'Books',
							books= models.Books.query.all())
		   
		   
@app.route('/authors', methods = ['GET', 'POST'])
def authors():
	return render_template("authors.html",
							title = 'Authors',
							authors= models.Authors.query.all())


@app.route('/add_auth',methods =['GET', 'POST'])
def add_auth():
	form = AddAuthor()
	if form.validate_on_submit():
		new_a = models.Authors(author=form.author_name.data, date=form.author_date.data)
		db.session.add(new_a)
		db.session.commit()
		print 'good'
		return redirect('/authors')
	return render_template('add_auth.html',
		title = 'Add auth',
		form = form)

@app.route('/add_book',methods =['GET', 'POST'])
def add_book():
	form = AddBook()
	if form.validate_on_submit():
		new_b = models.Books(book=form.book_name.data, author_id=form.book_author.data, genres=form.book_genre.data)
		db.session.add(new_b)
		db.session.commit()
		return redirect('/books')
	return render_template('add_book.html',
		title = 'Add book',
		form = form)


@app.route('/edit_book', methods = ['GET', 'POST'])
def edit():
    form = EditBook()
    if form.validate_on_submit():
    	tmp = models.Books.query.get()
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_book'))
    else:
        form.nickname.data = g.user.nickname
        form.about_me.data = g.user.about_me
    return render_template('edit_book.html',
        form = form)
