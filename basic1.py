'''Create a Flask app that displays "Hello, World!" on the homepage.
'''

"""To run : 
   flask run
   flask run --port
"""

from flask import Flask 
app = Flask (__name__)


@app.route ('/')
def show ():
    return 'Hello wold'


if __name__=='__main__':
   app.run(debug=True)

