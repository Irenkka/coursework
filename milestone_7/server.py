from flask import Flask, request, jsonify, make_response
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
    error = 0
    try:
        month = request.args.get('month')
        assert(month != None)
    except:
        error = 1
        error_message = "Missing 'month' parameter"
        response = make_response(error_message, 400)
    
    try:
        department = request.args.get('department')
        assert(department != None)
    except:
        if error == 0:
            error = 2
            error_message = "Missing 'department' parameter"
        else:
            error_message = "Missing 'department' and 'month' parameter"
            error == 3
        response = make_response(error_message, 400)

    if error != 0:
        return response
    else:
        filtered_employees = get_month_data("./milestone_5/database.csv", "birthday", month)
        department_employees = filtered_employees[department]

        response = {
            "total": len(department_employees),
            "employees": department_employees
        }

        return jsonify(response)

@app.route('/anniversaries')
def anniversaries():
    error = 0
    try:
        month = request.args.get('month')
        assert(month != None)
    except:
        error = 1
        error_message = "Missing 'month' parameter"
        response = make_response(error_message, 400)
    
    try:
        department = request.args.get('department')
        assert(department != None)
    except:
        if error == 0:
            error = 2
            error_message = "Missing 'department' parameter"
        else:
            error_message = "Missing 'department' and 'month' parameter"
            error == 3
        response = make_response(error_message, 400)

    if error != 0:
        return response
    else:
        filtered_employees = get_month_data("./milestone_5/database.csv", "anniversary", month)
        department_employees = filtered_employees[department]

        response = {
            "total": len(department_employees),
            "employees": department_employees
        }

        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False)
