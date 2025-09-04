# students = [
#     {"name": "Alice", "math": 78, "science": 89},
#     {"name": "Bob", "math": 92, "science": 76},
#     {"name": "Charlie", "math": 88, "science": 95},
#     {"name": "David", "math": 65, "science": 70}
# ]
# # process_students(students, get_names)
# # # ['Alice', 'Bob', 'Charlie', 'David']

# # process_students(students, get_avg_score)
# # # [83.5, 84.0, 91.5, 67.5]

# # process_students(students, get_grade)
# # # ['B', 'B', 'A', 'C']


# def get_names(students):
#     names=[]
#     for i in students:
#         names.append(i["name"])
#     print(names)
# def  get_avg_score(students):
#     average=[]
#     for i in students:
#         average.append((i["math"]+i["science"])/2)
#     print(average)
# def  get_grade(students):
#     grades=[]
#     average=[]
#     for i in students:
#         average.append((i["math"]+i["science"])/2)
#     for i in average:
#         if i>90:
#             grades.append("A")
#         elif i>80 and i<90:
#             grades.append("B")
#         elif i>60 and i<80:
#             grades.append("c")
#     print(grades)
# def process_students(students,choice):  #   if this is called then 
#     print("process students is called")
#     return choice(students) # choice==get_name--->get_names(students)-->will be called
# option=input("Enter names or grades or average:")

# if option=="names": #if names i given as input then below function will be called
#     process_students(students,get_names)
# elif option=="average":
#     process_students(students,get_avg_score)
# elif option=="grades":
#     process_students(students,get_grade)


employees = [
    {"name": "Raj", "salary": 45000, "experience": 2},
    {"name": "Sneha", "salary": 70000, "experience": 5},
    {"name": "Aman", "salary": 55000, "experience": 3},
    {"name": "Priya", "salary": 90000, "experience": 7}
]

def employee_names(employees):
    names=[]
    for i in employees:
        names.append(i["name"])
    return names
def bonus(employees):
    bonus_salary=[]
    for i in employees:
        bonus_salary.append(i["salary"]/10)
    # print(bonus_salary)
    return bonus_salary
def promotion_eligibility(employees):
    eligibility=[]
    for i in employees:
        if i["experience"]>=5:
            eligibility.append("Eligible")
        else:
            eligibility.append("Not eligible")
    return eligibility
def salary_grade(employees):
    grades=[]
    for i in employees:
        if i["salary"]>=80000:
            grades.append("A")
        elif i["salary"]>=60000 and i["salary"]<80000:
            grades.append("B")
        elif i["salary"]<60000:
            grades.append("C")
    # print(grades)
    return grades
def process_employees(employees,choice):
    return choice(employees)

while True:
    option=input("Enter names or bonus or promotion or grades \n")
    match option:
        case "names":
            ans=process_employees(employees,employee_names)
        case "bonus":
            ans=process_employees(employees,bonus)
        case "salary":
            ans=process_employees(employees,salary_grade)
        case "promotion":
            ans=process_employees(employees,promotion_eligibility)
        case "exit":
            break
        case _:
            print("Enter appropriate option")
    print(ans)

        
    
        