import mysql.connector
from mysql.connector import Error

# Database connection
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Paulmoses2806#",
        database="company_db"
    )

# Create employee
def add_employee(name, position, salary):
    db = connect_db()
    cursor = db.cursor()
    query = "INSERT INTO employee (name, position, salary) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, position, salary))
    db.commit()
    print("✅ Employee Added Successfully!")
    db.close()

# View employees
def view_employees():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employee")
    results = cursor.fetchall()
    for row in results:
        print(row)
    db.close()

# Update employee
def update_salary(emp_id, new_salary):
    db = connect_db()
    cursor = db.cursor()
    query = "UPDATE employee SET salary=%s WHERE id=%s"
    cursor.execute(query, (new_salary, emp_id))
    db.commit()
    print("✅ Salary Updated!")
    db.close()

# Delete employee
def delete_employee(emp_id):
    db = connect_db()
    cursor = db.cursor()
    query = "DELETE FROM employee WHERE id=%s"
    cursor.execute(query, (emp_id,))
    db.commit()
    print("✅ Employee Deleted!")
    db.close()

# Menu system
if __name__ == "__main__":
    while True:
        print("\n1. Add Employee")
        print("2. View Employees")
        print("3. Update Salary")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            position = input("Position: ")
            salary = float(input("Salary: "))
            add_employee(name, position, salary)

        elif choice == "2":
            view_employees()

        elif choice == "3":
            emp_id = int(input("Employee ID: "))
            new_salary = float(input("New Salary: "))
            update_salary(emp_id, new_salary)

        elif choice == "4":
            emp_id = int(input("Employee ID: "))
            delete_employee(emp_id)

        elif choice == "5":
            break

        else:
            print("Invalid choice!")