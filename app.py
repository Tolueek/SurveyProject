from flask import Flask, render_template, request
from pymongo import MongoClient
import csv

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"


app = Flask(__name__)

@app.route('/')
def survey_form():
    return render_template('survey_form.html')

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, AWS!"

class User:
    def __init__(self, name, age, gender, income, spending):
        self.name = name
        self.age = age
        self.gender = gender
        self.income = income
        self.spending = spending



if __name__ == '__main__':
    app.run(debug=True)


import csv

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    income = request.form['income']
    spending = request.form['spending']

    user = User(name, age, gender, income, spending)

    # Write to CSV
    with open('user_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user.name, user.age, user.gender, user.income, user.spending])

    return "Survey submitted successfully!"


if __name__ == '__main__':
    app.run(debug=True)





