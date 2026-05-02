from db import get_connection

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"
def add_student():
    name = input("Enter Name: ")
    roll_no = input("Enter Roll No: ")
    dept = input("Enter Department: ")
    marks = int(input("Enter Marks: "))

    grade = calculate_grade(marks)

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO students (name, roll_no, department, marks, grade) VALUES (%s, %s, %s, %s, %s)",
            (name, roll_no, dept, marks, grade)
        )
        conn.commit()
        print("✅ Student Added Successfully")
    except Exception as e:
        print("❌ Error:", e)

    conn.close()

def view_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\n📋 Student Records")
    print("-" * 50)

    for row in rows:
        print(row)

    conn.close()


def update_student():
    roll_no = input("Enter Roll No: ")
    marks = int(input("Enter New Marks: "))

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET marks=%s WHERE roll_no=%s",
        (marks, roll_no)
    )
    conn.commit()

    if cursor.rowcount > 0:
        print("✅ Updated Successfully")
    else:
        print("❌ Student Not Found")

    conn.close()


def delete_student():
    roll_no = input("Enter Roll No: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE roll_no=%s",
        (roll_no,)
    )
    conn.commit()

    if cursor.rowcount > 0:
        print("✅ Deleted Successfully")
    else:
        print("❌ Student Not Found")

    conn.close()


def menu():
    while True:
        print("\n🎓 STUDENT RESULT MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Marks")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice")


if __name__ == "__main__":
    menu()