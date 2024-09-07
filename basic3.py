'''Develop a Flask app that uses URL parameters to display dynamic content.
'''


from flask import Flask
app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome to my page'


@app.route('/checker/<int:number>')
def checker(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."



if __name__ == '__main__':
    app.run(debug=True)
