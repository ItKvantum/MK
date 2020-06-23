from flask import Blueprint, render_template, request, redirect, url_for
from models import Post, Tag
from .forms import PostForm
from app import db
from flask_security import login_required
posts = Blueprint('posts',__name__, template_folder='templates')


@posts.route('/')
def index():
    q = request.args.get('q')
    
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.text.contains(q))
        pages = posts.paginate(page=page, per_page=len(posts.all()))
    else:
        posts = Post.query.order_by(Post.date.desc())
        pages = posts.paginate(page=page, per_page=4)
    return render_template('posts/index.html', obj=posts, pages=pages)

@posts.route('/create', methods=['GET','POST'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        try:
            post = Post(title=title, text=text)
            db.session.add(post)
            db.session.commit()
        except:
            print('Ой-ой :(')
        return redirect(url_for('posts.index'))
    form = PostForm()
    return render_template('posts/create_post.html', form=form)

@posts.route('/<slug>/edit/', methods = ['POST', 'GET'])
@login_required
def edit_post(slug):
    post = Post.query.filter(Post.slug==slug).first_or_404()
    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post)
        db.session.commit()
        return redirect(url_for('posts.post_detail', slug=post.slug))
    
    form = PostForm(obj=post)
    return render_template('posts/edit_post.html', post=post, form=form)
@posts.route('/<slug>')
def post_detail(slug):
    pst = Post.query.filter(Post.slug == slug).first_or_404()
    tags = pst.tags
    return render_template('posts/post_detail.html', post=pst, tags=tags)

@posts.route('/tag/<slug>')
def tag_detail(slug):
    tg = Tag.query.filter(Tag.slug==slug).first_or_404()
    pst = tg.posts.all()
    return render_template('posts/tag_detail.html', tag=tg, posts=pst)
