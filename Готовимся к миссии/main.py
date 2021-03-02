from flask import render_template, Flask

app = Flask(__name__)
TITLE = "Заготовка"


@app.route('/')
@app.route('/index')
def index():
    global TITLE
    return render_template('base.html', title=TITLE)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
