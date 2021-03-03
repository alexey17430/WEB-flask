from flask import render_template, Flask

app = Flask(__name__)
TITLE = "Заготовка"
LIST_PROF = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
             'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите',
             'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог',
             'опратор марсохода', 'киберинженер', 'штурман', 'пилот дронов']


@app.route('/')
@app.route('/index')
def index():
    global TITLE
    return render_template('base.html', title=TITLE)


@app.route('/list_prof/<spisok_type>')
def list_prof(spisok_type):
    global LIST_PROF
    return render_template('base.html', title=TITLE, spisok_type=spisok_type, spisok=LIST_PROF)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
