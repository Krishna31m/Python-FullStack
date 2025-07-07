from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}"


@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return f"Result: {a + b}"


@app.route('/html')
def html():
    html = """
<h1> Hello World </h1>
<h4> Human (we) are going Destroy the You </h4>
"""
    return html    # http://127.0.0.1:5000/html


@app.route('/template')
def template():
    return render_template('index.html')

@app.route('/add', methods = ['GET', 'POST'])
def add_page():
    result = None
    if request.method == 'POST':
        try:
            a = int(request.form['a'])
            b = int(request.form['b'])
            result = a + b
        except (KeyError, ValueError):
            result = "Invalid input"
    return render_template('add.html', result=result)

#calculate body mass index
@app.route('/bmi', methods=['GET', 'POST'])
def bmi():
    result = None
    if request.method == 'POST':
        try:
            weight = float(request.form['weight'])
            height = float(request.form['height'])
            bmi_value = (weight / (height * height)) * 10000   #(weight in kilograms / (height in centimeters * height in centimeters)) * 10,000
            result = f"BMI: {bmi_value:.2f}"
        except (KeyError, ValueError):
            result = "Invalid input"
    return render_template('bmi.html', result=result)

#Simple calculator
# Simple calculator
@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            a = float(request.form['num1'])
            b = float(request.form['num2'])
            op = request.form['operation']
            if op == 'add':
                result = a + b
            elif op == 'subtract':
                result = a - b
            elif op == 'multiply':
                result = a * b
            elif op == 'divide':
                result = a / b if b != 0 else 'Division by zero'
            else:
                result = 'Invalid operation'
        except (KeyError, ValueError):
            result = 'Invalid input'
    return render_template('calculator.html', result=result)


#Loan calculator
@app.route('/loan', methods=['GET', 'POST'])
def loan_calculator():
    result = None
    if request.method == 'POST':
        try:
            principal = float(request.form['principal'])
            rate = float(request.form['rate']) / 100 / 12  # monthly interest rate
            years = float(request.form['years'])
            n_payments = years * 12
            if rate == 0:
                payment = principal / n_payments
            else:
                payment = principal * (rate * (1 + rate) ** n_payments) / ((1 + rate) ** n_payments - 1)
            result = f"Monthly Payment: {payment:.2f}"
        except (KeyError, ValueError, ZeroDivisionError):
            result = "Invalid input"
    return render_template('loan.html', result=result)


#Roller Coaster
@app.route('/roller', methods=['GET', 'POST'])
def roller_coaster_check():
    result = None
    if request.method == 'POST':
        try:
            weight = float(request.form['weight'])
            height = float(request.form['height'])
            age = int(request.form['age'])
            if 40 <= weight <= 120 and height >= 120 and age >= 10:
                result = "Eligible for the roller coaster!"
            else:
                result = "Sorry, you are not eligible for the roller coaster."
        except (ValueError, KeyError):
            result = "Invalid input."
    return render_template('roller.html', result=result)


#area calculator
@app.route('/area', methods=['GET', 'POST'])
def area_calculator():
    result = None
    if request.method == 'POST':
        shape = request.form.get('shape')
        try:
            if shape == 'rectangle':
                length = float(request.form['length'])
                width = float(request.form['width'])
                result = f"Area of Rectangle: {length * width:.2f} m²"
            elif shape == 'circle':
                radius = float(request.form['radius'])
                result = f"Area of Circle: {3.1416 * radius ** 2:.2f} m²"
            elif shape == 'triangle':
                base = float(request.form['base'])
                height = float(request.form['height'])
                result = f"Area of Triangle: {0.5 * base * height:.2f} m²"
            else:
                result = "Unknown shape"
        except (ValueError, KeyError):
            result = "Invalid input."
    return render_template('area.html', result=result)

# @app.route('/area', methods=['GET', 'POST'])
# def area_calculator():
#     result = None
#     if request.method == 'POST':
#         shape = request.form.get('shape')
#         try:
#             if shape == 'rectangle':
#                 length = float(request.form['length'])
#                 width = float(request.form['width'])
#                 result = f"Area of Rectangle: {length * width:.2f} m²"
#             elif shape == 'circle':
#                 radius = float(request.form['radius'])
#                 result = f"Area of Circle: {3.1416 * radius ** 2:.2f} m²"
#             elif shape == 'triangle':
#                 base = float(request.form['base'])
#                 height = float(request.form['height'])
#                 result = f"Area of Triangle: {0.5 * base * height:.2f} m²"
#             else:
#                 result = "Please select a valid shape."
#         except (ValueError, KeyError):
#             result = "Invalid input."
#     return render_template('area.html', result=result)




if __name__ == '__main__' :
    app.run(debug=True)


