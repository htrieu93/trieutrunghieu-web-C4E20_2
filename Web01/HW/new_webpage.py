from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/about-me')
def intro():
    about_me = {
            'name': 'Triệu Trung Hiếu',
            'work': 'None',
            'school': 'Drexel University',
            'hobby': 'Coding'
    }
    return render_template('intro.html', about_me = about_me)

@app.route('/school')
def school():
    return redirect('http://techkids.vn')

if __name__ == '__main__':
  app.run(debug=True)
 

