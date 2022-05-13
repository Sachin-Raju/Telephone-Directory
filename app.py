from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
d={}
@app.route('/')
def index():
	return render_template("layout.html")


@app.route('/add',methods=['GET','POST'])
def add():
	global d

	name=request.form.get("name")
	number=request.form.get("number")
	d[name]=number
	return render_template("add.html",d=d, name=name, number=number)


@app.route('/display',methods=['GET','POST'])
def display():
	global d

	name=request.form.get("name")
	number=request.form.get("number")
	d[name]=number
	return render_template("display.html",d=d, name=name, number=number)


@app.route('/search',methods=['GET','POST'])
def search():
	global d
	name=request.form.get("name")
	return render_template("search.html",d=d, name=name)

@app.errorhandler(404)
def error(e):
	return "Kindy check the url or name"

if __name__=='__main__':
	app.run(debug=True)