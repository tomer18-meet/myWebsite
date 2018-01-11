from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, tomer!</h1>'

@app.route('/pets')
def my_favorite_pet():
	return 'My favorite pet is Cat!'

@app.route('/food')
def my_favorite_food():
	return 'My favorite food is knafe!'

@app.route('/user/<username>')
def show(username):
	return username	

@app.route('/calculator/<num1>/<num2>/<math_opperation>')
def calculator(num1,num2,math_opperation):

	if math_opperation == '+':
		plus=int(num2)+int(num1)
		return str(plus)
	if math_opperation == '*':
		moltiply=int(num2)*int(num1)
		return str(moltiply)
	if math_opperation == '-':
		minus=int(num2)-int(num1)
		return str(minus)		
	if math_opperation == ':':
		devide=int(num2)/int(num1)
		return str(devide)
	else:
		return error		

