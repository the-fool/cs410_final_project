from flask import render_template, url_for, request
from ..models import Cookie, db
from . import main

@main.route('/')
def index():
    cookies = request.args.get('cookies')
    if not cookies:
        return "Okie dokie"

    cookies = [c.strip() for c in cookies.split(';')]
    for c in cookies:
        c = c.split('=')
        cookie = Cookie(name=c[0], value=c[1])
        db.session.add(cookie)
    db.session.commit()
    return ''
