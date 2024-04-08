import csv
import sys
from collections import defaultdict
from datetime import datetime

def load_data(file_name):
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

def generate_report(data, title):
    print(title)
    total = sum(len(employees) for employees in data.values())
    print(f"Total: {total}")
    print("By department:")
    for department, employees in data.items():
        print(f"- {department}: {len(employees)}")

def main(file_name, month):
    data = load_data(file_name)
    filtered_data_anniv = filter_by_month(data, month, 'Hiring Date')
    filtered_data_bday = filter_by_month(data, month, 'Birthday')
    print(f"Report for {month.capitalize()} generated")
    generate_report(filtered_data_bday, "--- Birthdays ---")
    generate_report(filtered_data_anniv, "--- Annirversaries ---")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python report.py <database_file> <month>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    month = sys.argv[2]
    main(file_name, month)