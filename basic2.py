'''Build a Flask app with static HTML pages and navigate between them
'''



from flask import Flask,render_template 
app= Flask (__name__)


@app.route ('/')
def home ():
    return render_template ('welcome.html')


@app.route ('/first')
def first ():
    return render_template ('first.html')


@app.route ('/second')
def second ():
    return render_template ('second.html')





if __name__=='__main__':
    app.run (debug=True)



