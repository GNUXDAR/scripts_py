from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from flask_todolist.auth import login_required
from flask_todolist.db import get_db

bp = Blueprint("blog", __name__)


@bp.route("/")
def index():
    """Show all the list, most recent first."""
    db = get_db()
    lists = db.execute(
        "SELECT p.id, title, body, created, author_id, username"
        " FROM item p JOIN user u ON p.author_id = u.id"
        " ORDER BY created DESC"
    ).fetchall()
    return render_template("blog/index.html", lists=lists)


def get_item(id, check_author=True):
    """Get a item of list and its author by id.

    Checks that the id exists and optionally that the current user is
    the author.

    :param id: id of item to get
    :param check_author: require the current user to be the author
    :return: the item with author information
    :raise 404: if a item with the given id doesn't exist
    :raise 403: if the current user isn't the author
    """
    item = (
        get_db()
        .execute(
            "SELECT p.id, title, body, created, author_id, username"
            " FROM item p JOIN user u ON p.author_id = u.id"
            " WHERE p.id = ?",
            (id,),
        )
        .fetchone()
    )

    if item is None:
        abort(404, f"Item id {id} doesn't exist.")

    if check_author and item["author_id"] != g.user["id"]:
        abort(403)

    return item


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    """Create a new item for the current user."""
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO item (title, body, author_id) VALUES (?, ?, ?)",
                (title, body, g.user["id"]),
            )
            db.commit()
            return redirect(url_for("blog.index"))

    return render_template("blog/create.html")


@bp.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    """Update a item if the current user is the author."""
    item = get_item(id)

    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "UPDATE item SET title = ?, body = ? WHERE id = ?", (title, body, id)
            )
            db.commit()
            return redirect(url_for("blog.index"))

    return render_template("blog/update.html", item=item)


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    """Delete a item.

    Ensures that the item exists and that the logged in user is the
    author of the item.
    """
    get_item(id)
    db = get_db()
    db.execute("DELETE FROM item WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for("blog.index"))
