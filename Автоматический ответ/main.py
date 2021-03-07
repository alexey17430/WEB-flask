from flask import render_template, Flask, url_for

app = Flask(__name__)
param = {'title': 'Анкета', 'surname': 'Watny', 'name': 'Mark', 'education': 'выше среднего',
         'profession': 'штурман марсохода', 'sex': 'male',
         'motivation': 'Всегда мечтал застрять на марсе', 'ready': 'True'}


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
