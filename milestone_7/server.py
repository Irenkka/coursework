from flask import Flask, request, jsonify
import csv
import sys
from collections import defaultdict
from datetime import datetime

def load_data(file_name):
    print("Dataloaded")
    data = defaultdict(list)
    with open(file_name, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data[row['Department']].append(row)
    return data

def filter_by_month(data, month, filter_type):
    filtered_data = defaultdict(list)
    for department, employees in data.items():
        for employee in employees:
            hiring_date = datetime.strptime(employee[filter_type], '%Y-%m-%d')
            if hiring_date.strftime('%B').lower() == month.lower():
                filtered_data[department].append(employee)
    return filtered_data

def get_month_data(file_name, flag, month):
    data = load_data(file_name)
    if flag == 'anniversary':
        res = filter_by_month(data, month, 'Hiring Date')
    else:
        res = filter_by_month(data, month, "Birthday")
    return res

app = Flask(__name__)

@app.route('/health_check')
def health_check():
    return jsonify("Server Running")

@app.route('/birthdays')
def birthdays():
    month = request.args.get('month')
    department = request.args.get('department')

    filtered_employees = get_month_data("./milestone_5/database.csv", "birthday", month)
    department_employees = filtered_employees[department]

    response = {
        "total": len(department_employees),
        "employees": department_employees
    }

    return jsonify(response)

@app.route('/anniversaries')
def anniversaries():
    month = request.args.get('month')
    department = request.args.get('department')

    filtered_employees = get_month_data("./milestone_5/database.csv", "anniversary", month)
    department_employees = filtered_employees[department]

    response = {
        "total": len(department_employees),
        "employees": department_employees
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False)
