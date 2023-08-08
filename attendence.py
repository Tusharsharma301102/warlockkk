users = {
    "tushar sharma": "1234",
    "aman kumawat": "4321",
    "shivay sharma": "7894",
    "tanya verma": "4567",
    "shivam verma": "8520",
}

def login():
    username = input("Username:")
    password = input("Password:")

    if username in users and users[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

def register():
    new_username = input("New Username:")
    new_password = input("New Password:")

    if new_username not in users:
        users[new_username] = new_password
        print("Registration successful!")
    else:
        print("Username already exists. Please choose a different one.")

students = []

def add_student():
    pass

def view_students():
    pass

def update_student():
    pass

def delete_student():
    pass

attendance_records = {}

def mark_attendance():
    pass

def view_attendance():
    pass

def filter_attendance():
    pass

def generate_report():
    pass

def export_to_csv():
    pass

def main():
    print("Attendance Management System")

    while True:
        print("1.Login")
        print("2.Register")
        print("3.Add Student")
        print("4.View Students")
        print("5.Update Student")
        print("6.Delete Student")
        print("7.Mark Attendance")
        print("8.View Attendance")
        print("9.Generate Report")
        print("10.Export to CSV")
        print("11.Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            login()
        elif choice == 2:
            register()
        elif choice == 3:
            add_student()
        elif choice == 4:
            view_students()
        elif choice == 5:
            update_student()
        elif choice == 6:
            delete_student()
        elif choice == 7:
            mark_attendance()
        elif choice == 8:
            view_attendance()
        elif choice == 9:
            generate_report()
        elif choice == 10:
            export_to_csv()
        elif choice == 11:
            print("exit the program")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
