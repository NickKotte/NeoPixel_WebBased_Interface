from flask import Flask, jsonify, render_template, flash, redirect, url_for, g, make_response, send_file, send_from_directory, request
#from forms import RegistrationForm, LoginForm
from LED import led
from neopixel import *
app = Flask(__name__)

app.config['SECRET_KEY'] = '579118502384030cxfr3483220xe348951kd23'

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html')

strip = led()
@app.route('/background_process')
def background_process():
	color = request.args.get('color')
	if color == 'red':
		strip.showSolidColor(Color(0,255,0),20)
		return jsonify(result='Displaying red')
	elif color == 'blue':
		strip.showSolidColor(Color(0,0,255),20)
		return jsonify(result='Displaying blue')
	elif color == 'green':
		strip.showSolidColor(Color(255,0,0),20)
		return jsonify(result='Displaying green')
	elif color == 'clear':
		strip.showSolidColor(Color(0,0,0),20)
		return jsonify(result='Cleaning display')
	else:
		return jsonify(result='...')
    
@app.route('/about')
def about():
    return render_template('about.html')

#@app.route('/registration', methods=['GET', 'POST'])
#def register():
#	form = RegistrationForm()
#	if form.validate_on_submit():
#		flash('Account created for {form.username.data}')
#		return redirect(url_for('home'))
#	return render_template('register.html', title='Register', form=form)

#@app.route('/login')
#def login():
#	form = LoginForm()
#	return render_template('login.html', title='Login', form=form)
		

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
