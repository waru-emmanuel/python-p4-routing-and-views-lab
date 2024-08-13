#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_parameter(parameter):
    //print(parameter)
    return parameter

@app.route('/count/<parameter>')
def count_numbers(parameter):
    count = ''
    for i in range(int(parameter)):
        count += f'{i}\n'
    return count

@app.route('/math/<int:num1>/<operator>/<int:num2>')
def perform_math(num1, operator, num2):
    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return str(num1 - num2)
    elif operator == '*':
        return str(num1 * num2)
    elif operator == 'div':
        return str(num1 / num2) if num2 != 0 else 'Error: Division by zero'
    elif operator == '%':
        return str(num1 % num2)
    else:
        return 'Error: Invalid operator'
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
