from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from parsons import db
from parsons.models import Program
from parsons.utils import generate_random_url


bp = Blueprint('puzzle', __name__)


@bp.route('/puzzle/<string:program_url>')
def puzzle(program_url):
    """Show specific program as a puzzle."""
    program = (Program.query.filter_by(url=program_url)
                            .first_or_404())
    return render_template('puzzle.html', program=program)


@bp.route('/', methods=('GET', 'POST'))
def create():
    """Create a new program."""
    if request.method == 'POST':
        title = request.form['title']
        code = request.form['code']
        error = None

        if not title:
            error = 'Title is required.'

        if not code:
            error = 'Code is required.'

        if error is not None:
            flash(error)
        else:
            program_url = generate_random_url()
            db.session.add(Program(title=title,
                                   code=code,
                                   url=program_url))
            db.session.commit()

            return redirect(url_for('puzzle.puzzle',
                                    program_url=program_url))

    return render_template('create.html')
