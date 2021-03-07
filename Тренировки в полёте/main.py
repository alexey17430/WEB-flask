from flask import render_template, Flask

app = Flask(__name__)
TITLE = "Заготовка"


@app.route('/')
@app.route('/index')
def index():
    global TITLE
    return render_template('base.html', title=TITLE, page=3)


@app.route('/training/<prof>')
def list_prof(prof):
    global TITLE
    if 'инженер' in prof.lower() or 'строитель' in prof.lower():
        page = 1
    else:
        page = 2
    return render_template('base.html', title=TITLE, page=page)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
