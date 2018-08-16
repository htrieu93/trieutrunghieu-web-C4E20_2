from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # set values for parameters the same as their names
    posts= [{
        'title' : "Thơ con cóc",
        'content' : """Hôm nay trăng lên cao quá
                Anh muốn hôn em vào má""",
        'author' : "Tuấn Anh",
        'gender' : 1
        },
        {
        'title' : "Từ Từ",
        'content' : "Từ Từ",
        'author' : "Thu Minh",
        'gender' : 0
        },
        {
        'title' : "Chưa nghĩ ra",
        'content' : "Em không biết",
        'author' : "Khánh Ngô",
        'gender' : 1
        },
        {
        'title' : "Thơ lập trình",
        'content' : "Thầy bảo",
        'author' : "Hồng Thái",
        'gender' : 1
        },
        {
        'title' : "Đen Vãi",
        'content' : "Đen",
        'author' : "Sơn Hải",
        'gender' : 1
        }
    ]

    return render_template('index.html', 
                            posts = posts)

@app.route('/hello')
def say_hello():
    return('Hello from the other side')

@app.route('/say_hi/<name>/<age>')
def my_name(name, age):
    return("Hi {}, you're {} years old".format(name, age))

@app.route('/sum/<int:x>/<int:y>')
def total(x, y):
    return(str(x + y))

if __name__ == '__main__':
  app.run(debug = True)
 
