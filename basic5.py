from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
app.secret_key = 'login'


@app.route('/')
def login1():
    return render_template('sessionlogin.html')


@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login1'))





@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'basant' and password == '1234':
            session['email'] = username
            return redirect(url_for('profile'))
        else:
            msg = 'Invalid username or password'
            return render_template('sessionlogin.html', msg=msg)

@app.route('/profile')
def profile():
    if 'email' in session:
        email = session['email']
        return render_template('sessionprofile.html', name=email)
    else:
        return redirect(url_for('login1'))


if __name__ == '__main__':
    app.run(debug=True)
