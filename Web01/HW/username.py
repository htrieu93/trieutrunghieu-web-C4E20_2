from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def username(username):
    users = {
        'Quan':{
            'name': 'Quan',
            'gender': 'Male',
            'age': 17,
            'hobbies': 'gaming'
        },
        'Tien':{
            'name': 'Tien',
            'gender': 'Female',
            'age': 23,
            'hobbies': 'reading'
        },
        'Cuong':{
            'name': 'Cuong',
            'gender': 'Male',
            'age': 20,
            'hobbies': 'soccer'
        } 
    }
    if username in users:
        return render_template('username.html', username = users[username])
    else:
        return 'User not found'

if __name__ == '__main__':
  app.run(debug=True)
 