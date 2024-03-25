import requests
import sys

def fetch_birthday_report(month, department):
    url = f"http://localhost:5000/birthdays?month={month}&department={department}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        total = data.get('total', 0)
        employees = data.get('employees', [])
        
        print(f"Birthday report for {department} department for {month} fetched.")
        print(f"Total: {total}")
        print("Employees:")
        for employee in employees:
            print(f"- {employee['Birthday']}, {employee['Name']}")
    else:
        print(f"Failed to fetch report: {response.status_code}")
        
def fetch_anniversary_report(month, department):
    url = f"http://localhost:5000/birthdays?month={month}&department={department}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        total = data.get('total', 0)
        employees = data.get('employees', [])
        
        print(f"Anniversary report for {department} department for {month} fetched.")
        print(f"Total: {total}")
        print("Employees:")
        for employee in employees:
            print(f"- {employee['Hiring Date']}, {employee['Name']}")
    else:
        print(f"Failed to fetch report: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python fetch_report.py <month> <department>")
        sys.exit(1)
    
    month = sys.argv[1]
    department = sys.argv[2]
    
    print("\n")
    fetch_birthday_report(month, department)
    print("\n")
    fetch_anniversary_report(month, department)
