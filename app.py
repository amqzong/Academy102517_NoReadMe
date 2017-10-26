from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG']=True

#webpage localhost:5000/hello
@app.route('/hello')
def hello():
    return "Hello!"


#dynamic webpages localhost:5000/echo/message

@app.route('/add/<x>/<y>')
def add(x,y):
    try:
        return str(int(x)+int(y))
    except:
        return "Error"


#new webpage localhost:5000
@app.route('/home')
def home():
	return render_template('samplehtml.html', name = "Amanda")

@app.route('/bootstrap')
def bootstrap():
	return render_template('RunBaseBootstrap.html')

@app.route('/login')
def login():
	return render_template('login.html')

if __name__ == "__main__":
	app.run()
