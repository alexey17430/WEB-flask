from flask import Flask

app = Flask(__name__)


@app.route('/')
def start():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Стартовое окно</title>
                    <link rel="stylesheet" href="static/css/style.css">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
                  </head>
                  <body>
                    <div class="alert alert-success" role="alert" align="center">
                      <h4 class="alert-heading">Стартовое окно</h4>
                      <p>Уважаемый пользователь, это окно является стратовым</p>
                      <hr>
                      <p class="mb-0">Чтобы перейти на другую страничку измените ссылку в соответствии с определёнными параметрами</p>
                    </div>
                  </body>
                </html>"""


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/choice/<planet_name>')
def results(planet_name):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Варианты выбора</title>
                    <link rel="stylesheet" href="static/css/style.css">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
                  </head>
                  <body>
                    <h1 align="center">Моё предложение {planet_name}</h1>
                    <div class="alert alert-primary" role="alert">
                      <h2>Эта планета близка к Земле</h2>
                    </div>
                    <div class="alert alert-success" role="alert">
                      <h2>На ней много необходимых ресурсов для работы и поддержания жизнедеятельности</h2>
                    </div>
                    <div class="alert alert-info" role="alert">
                        <h2>На ней есть вода и атмосфера</h2>
                    </div>
                    <div class="alert alert-danger" role="alert">
                        <h2>Наконец, она просто красива</h2>
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
