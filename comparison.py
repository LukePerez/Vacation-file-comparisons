import re
print("Vacation checker")
print("Please input file names as comlete file paths, thank you")

file1 = input("Employee-name database file: ")#employee_names.txt
file2 = input("Employee-vacation time file: ")#employee_vacation_hours.txt

with open(file1) as f1,open(file2) as f2:
    employees = f1.read().split()
    employees_vacation_time = f2.read().split("-")
    f2.seek(0)
    employees_vaca_hours = f2.read().split(",")
    employees_with_vaca = set(employees) & set(employees_vacation_time)
    employee_vaca_wrongly_retained = set(employees_vacation_time) - set(employees)
    employees_no_vacation = set(employees) - set(employees_vacation_time)
    
    for each in employees_with_vaca:
        pattern = r"([0-9]+)(hours)"
        if re.match(pattern, each):
            continue
        print("Employee " + each + " has unused vacation time.\n")
    for each in employees_no_vacation:
        print("Employee " + each + " is out of vacation time.\n")
    for each in employee_vaca_wrongly_retained:
        pattern = r"[0-9]+"
        pattern2 = r"[A-Z]+"
        if re.match(pattern, each):
            continue
        if re.match(pattern2, each):
            print("Former employee " + each + " is still listed in the vacation time file.\n")
    
    response = input("Enter 'y' to see employee vacation hours remaining\n")
    if response == 'y':
        for each in employees_vaca_hours:
            print(each + "\n")
    else:
        print("Application terminated. \n")
    print("Thank you for using my program.")

