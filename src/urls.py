from  flask import render_template, request, jsonify, redirect


from .server import app, db
from  .model import Post


@app.route('/')
def index():
    blogs = Post.query.all()
    return render_template('index.html',blogs=blogs)

@app.route('/newblog', methods=['GET', 'POST'])
def newblog():
    if request.method == 'GET':
        return render_template('newblog.html')
    elif request.method == 'POST':
        post = request.form.get('post')
        post_db = Post(html=post)
        db.session.add(post_db)
        db.session.commit()
        
        return jsonify(post='success')

@app.route('/blog/<postid>', methods=['GET', 'POST'])
def blog(postid):
    post = Post.query.get(postid)
    if post:
        if post.html:
            blog = post.html
            return render_template('blog.html', blog=blog)
        else:
            return render_template('blog.html', blog='')
    else:
        return redirect('newblog')
@app.route('/edit/')  
@app.route('/edit/<postid>', methods=['GET', 'POST'])
def edit(postid=None):

    if request.method == 'POST':
        post = Post.query.get(postid)
        if post:
            html = request.form.get('post')
            post.html = html
            db.session.add(post)
            db.session.commit()
            return jsonify(post='success')
    else:
        post = Post.query.get(postid)
        if post and post.html:
            blog = post.html
            return render_template('edit.html', blog=blog, error=False)
        else:
            return render_template('edit.html', error=True, message="Couldn't load the post for editting ")
        

    




@app.route('/remember')
def remember():
    return 'The world is just here'