from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def start():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Отбор астронавтов</title>
                    <link rel="stylesheet" href="static/css/style.css">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
                  </head>
                  <body>
                    <h1 align="center">Анкета претендента на участие в миссии</h1>
                    <br></br>
                    
                    <div class="mb-3">
                        <label for="exampleFormControlInput1" class="form-label">Фамилия претендента на участие в миссии</label>
                        <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="Введите фамилию">
                    </div>
                    
                    <br></br>
                    <div class="mb-3">
                        <label for="exampleFormControlInput1" class="form-label">Имя претендента на участие в миссии</label>
                        <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="Введите имя">
                    </div>
                    
                    <br></br>
                    <div class="mb-3">
                        <label for="exampleFormControlInput1" class="form-label">Почта претендента на участие в миссии</label>
                        <input type="email" class="form-control" id="exampleFormControlInput1" placeholder="Введите почту">
                    </div>
                    
                    <br></br>
                    <p>Какое у Вас образование?</p>
                    
                    <select class="form-select form-select-lg mb-3" aria-label=".form-select-lg example">
                      <option selected>Среднее общее образование</option>
                      <option value="1">Среднее профессиональное образование</option>
                      <option value="2">Высшее образование - бакалавриат</option>
                      <option value="3">Высшее образование - специалитет, магистратура</option>
                      <option value="3">Высшее образование - подготовка кадров высшей квалификации</option>
                    </select>
                    
                    <br></br>
                    <p>Какие у Вас есть профессии?</p>
                    
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                      <label class="form-check-label" for="flexCheckDefault">
                        Инженер-строитель
                      </label>
                    </div>
                    
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                      <label class="form-check-label" for="flexCheckDefault">
                        Инженер-исследователь
                      </label>
                    </div>
                    
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                      <label class="form-check-label" for="flexCheckDefault">
                        Пилот
                      </label>
                    </div>
                    
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                      <label class="form-check-label" for="flexCheckDefault">
                        Метеоролог
                      </label>
                    </div>
                    
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                      <label class="form-check-label" for="flexCheckDefault">
                        Инженер по жизнеобеспечению
                      </label>
                    </div>
                    
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                      <label class="form-check-label" for="flexCheckDefault">
                        Инженер по радиационной защите
                      </label>
                    </div>
                    
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                      <label class="form-check-label" for="flexCheckDefault">
                        Врач
                      </label>
                    </div>
                    
                    <div class="form-check">
                      <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                      <label class="form-check-label" for="flexCheckDefault">
                        Биолог
                      </label>
                    </div>
                    
                    <br></br>
                    <div class="form-check form-switch">
                      <input class="form-check-input" type="checkbox" id="flexSwitchCheckChecked">
                      <label class="form-check-label" for="flexSwitchCheckChecked">Готовы остаться на Марсе?</label>
                    </div>
                    
                    <br></br>
                    <p>Укажите свой пол</p>
                    
                    <div class="form-check">
                      <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                      <label class="form-check-label" for="flexRadioDefault1">
                        Мужской
                      </label>
                    </div>
                    
                    <div class="form-check">
                      <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                      <label class="form-check-label" for="flexRadioDefault1">
                        Женский
                      </label>
                    </div>
                    
                    <br></br>
                    <div class="mb-3">
                      <label for="exampleFormControlTextarea1" class="form-label">Почему Вы хотите поучаствовать в миссии?</label>
                      <textarea class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
                    </div>
                    
                    <br></br>
                    <button type="button" class="btn btn-primary">Отправить</button>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
