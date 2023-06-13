from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flask_todolist.auth import login_required
from flask_todolist.db import get_db

bp = Blueprint('list', __name__)


@bp.route('/')
def index():
    db = get_db()
    lists = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM item p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('list/index.html', lists=lists)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO item (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('list.index'))

    return render_template('list/create.html')


def get_item(id, check_author=True):
    item = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM item p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if item is None:
        abort(404, f"Item id {id} doesn't exist.")

    if check_author and item['author_id'] != g.user['id']:
        abort(403)

    return item


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    item = get_item(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE item SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('list.index'))

    return render_template('list/update.html', item=item)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_item(id)
    db = get_db()
    db.execute('DELETE FROM item WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('list.index'))
