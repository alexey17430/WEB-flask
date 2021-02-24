from flask import Flask, request

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


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Результаты</title>
                    <link rel="stylesheet" href="static/css/style.css">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
                  </head>
                  <body>
                    <h1 align="center">Результаты отбора</h1>
                    
                    <div class="alert alert-primary" role="alert">
                      <h2>Претендент на участие в миссии - {nickname}</h2>
                    </div>
                    
                    <div class="alert alert-success" role="alert">
                      <h3>Поздравляем ваш рейтинг после {level} этапа отбора выше среднего</h3>
                    </div>
                    
                    <div class="alert alert-info" role="alert">
                        <h3>А именно равен {rating} баллам</h3>
                    </div>
                    
                    <div class="alert alert-danger" role="alert">
                        <h3>Желаем удачи в дальнейшем прохождении наших испытаний!!!</h3>
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
