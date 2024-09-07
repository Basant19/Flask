'''Create a Flask app with a form that accepts user input and displays it.
'''


from flask import Flask, render_template, request
app = Flask(__name__)



@app.route('/')
def form_show():
    return render_template('nameform.html')


@app.route('/showname', methods=['POST'])
def show_name():
    name = request.form.get('fname')
    return render_template('showname.html', name=name)



if __name__ == '__main__':
    app.run(debug=True)
