import csv
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker to generate fake data
fake = Faker()

jobs = ["HR", "Engineering", "Finance", "R&D"]

# Function to generate random date within a given range
def random_date(start_date, end_date):
    return start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

# Function to generate synthetic data for employees
def generate_employee_data(num_records):
    with open('database.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Hiring Date', 'Department', 'Birthday']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for _ in range(num_records):
            name = fake.name()
            hiring_date = random_date(datetime(2015, 1, 1), datetime(2024, 1, 1)).strftime('%Y-%m-%d')
            department = random.choice(jobs)
            birthday = fake.date_of_birth().strftime('%Y-%m-%d')

            writer.writerow({'Name': name, 'Hiring Date': hiring_date, 'Department': department, 'Birthday': birthday})

# Generate 100 records of employee data
generate_employee_data(100)

print("Data generation complete!")