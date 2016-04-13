from cookie_monster import create_app
from werkzeug.serving import run_simple

app = create_app()

if __name__ == "__main__":
    run_simple('0.0.0.0', 5005, app, use_reloader=True, use_debugger=True)
