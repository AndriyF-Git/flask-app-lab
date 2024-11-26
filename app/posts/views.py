from . import post_bp
from flask import render_template, abort, flash, redirect, url_for, session
from .forms import PostForm
from .functions import read_posts, write_posts, get_new_id
from .models import Post
from app import db




@post_bp.route('/')
def get_posts():
    posts = db.session.query(Post).order_by(Post.posted.desc()).all()
    return render_template("posts.html", posts=posts)


@post_bp.route('/<int:id>')
def detail_post(id):
    #posts = read_posts()
    
    #post = next((post for post in posts if post["id"] == id), None)
    post = db.session.get(Post, id)
    if post is None:
        abort(404)

    return render_template("detail_post.html", post=post)

@post_bp.route('/delete_post/<int:id>', methods=['POST'])
def delete_post(id):
    # Отримуємо пост із бази даних
    post = db.session.get(Post, id)

    # Якщо пост не знайдено, повертаємо 404
    if not post:
        abort(404)

    # Видаляємо пост із бази даних
    db.session.delete(post)
    db.session.commit()

    # Виводимо повідомлення про успішне видалення
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('posts.get_posts'))  # Повертаємося до списку постів


@post_bp.route('/edit_post/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    # Отримуємо пост із бази даних
    post = db.session.get(Post, id)

    # Якщо пост не знайдено, повертаємо 404
    if not post:
        abort(404)

    # Ініціалізуємо форму з даними поста
    form = PostForm(obj=post)

    if form.validate_on_submit():
        # Оновлюємо дані поста з форми
        post.title = form.title.data
        post.content = form.content.data
        post.category = form.category.data
        post.is_active = form.is_active.data
        post.posted = form.publish_date.data

        # Зберігаємо зміни у базі даних
        db.session.commit()

        flash('Post updated successfully!', 'success')
        return redirect(url_for('posts.get_posts'))  # Повертаємося до списку постів

    return render_template('edit_post.html', form=form, post=post)

@post_bp.route('/add_post', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        # Створюємо новий об'єкт Post
        new_post = Post(
            title=form.title.data,
            content=form.content.data,
            category=form.category.data,
            is_active=form.is_active.data,
            posted=form.publish_date.data,  # Збереження дати з форми
            author=session.get('username', 'Unknown')  # Автор з session
        )

        # Додаємо об'єкт у базу даних
        db.session.add(new_post)
        db.session.commit()  # Фіксуємо зміни в базі

        flash('Post added successfully!', 'success')
        return redirect(url_for('posts.get_posts'))  # Повертаємося до списку постів

    return render_template('add_post.html', form=form)
