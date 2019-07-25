from flask import Flask, jsonify, render_template, flash, redirect, url_for, g, make_response, send_file, send_from_directory, request
#from forms import RegistrationForm, LoginForm
from LED import led
from neopixel import *
import time
app = Flask(__name__)

app.config['SECRET_KEY'] = '579118502384030cxfr3483220xe348951kd23'

@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html')

strip = led()
@app.route('/pattern', methods=['POST'])
def pattern():
	pattern = request.form['pattern']
	cyclesPerSecond = float(request.form['cyclesPerSecond'])
	if cyclesPerSecond < 0:
		cyclesPerSecond = 0
	elif cyclesPerSecond > 5:
		cyclesPerSecond = 5
	
	return strip.testpattern(pattern, float(cyclesPerSecond))

@app.route('/Solidfy_Process', methods=['POST'])
def Solidfy_Process():
	color = request.form['color']
	
	if color == 'red':
		strip.splitSolidColor(Color(0,255,0),10)
	elif color == 'blue':
		strip.splitSolidColor(Color(0,0,255),10)
	elif color == 'green':
		strip.splitSolidColor(Color(255,0,0),10)
	elif color == 'clear':
		strip.setGo(False)
		strip.splitSolidColor(Color(0,0,0),1)
	return 'good'

@app.route('/Detailed_Process', methods=['POST'])
def Detailed_Process():
	color = request.form.getlist('color[]')
	print(color)
	strip.splitSolidColor(Color(int(color[0]),int(color[1]),int(color[2])), 5)
	return 'good'

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
