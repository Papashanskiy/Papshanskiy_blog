from __init__ import app, db
from models import Post
from flask import render_template, request, redirect, url_for, flash, send_file, send_from_directory
import datetime, os


FILES_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static', 'music')


@app.route('/')                                     # View functions
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.filter_by(id=post_id).one()
    return render_template('post.html', post=post)


@app.route('/new_post')
def new_post():
    return render_template('new_post.html')


@app.route('/addpost', methods=['POST', 'GET'])
def addpost():
    if request.method == 'POST':
        title = request.form['title']
        subtitle = request.form['subtitle']
        author = request.form['author']
        content = request.form['content']

        post = Post(title=title, sub_title=subtitle, author=author, content=content, date_post=datetime.datetime.now())

        db.session.add(post)
        db.session.commit()

        return redirect(url_for('index'))
    else:
        flash('<h1>Something came wrong</h1>')
        return redirect(url_for('index'))


@app.route('/login', methods=["POST", "GET"])
def login():
    return 'Login'


@app.route('/download', methods=['POST', 'GET'])
def download():
    filenames = [f for f in os.listdir(FILES_FOLDER)]
    print(filenames)
    return render_template('download.html', files=filenames)


@app.route('/return-file/<filename>')
def return_file(filename):
    file_path = os.path.join(FILES_FOLDER)
    return send_from_directory(file_path, filename, as_attachment=True)


@app.errorhandler(404)                             # Error handlers
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
