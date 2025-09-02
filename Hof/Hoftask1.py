students = [
    {"name": "Alice", "math": 78, "science": 89},
    {"name": "Bob", "math": 92, "science": 76},
    {"name": "Charlie", "math": 88, "science": 95},
    {"name": "David", "math": 65, "science": 70}
]
# process_students(students, get_names)
# # ['Alice', 'Bob', 'Charlie', 'David']

# process_students(students, get_avg_score)
# # [83.5, 84.0, 91.5, 67.5]

# process_students(students, get_grade)
# # ['B', 'B', 'A', 'C']

def get_names(students):
    names=[]
    for i in students:
        names.append(i["name"])
    # print(f"{names}")
    return names
def get_avg_score(students):
    result=[]
    for i in students:
        avg=0
        avg=(i["math"]+i["science"])/2
        result.append(avg)
    return result
def get_grade(students):
    grades=[]
    result=[]
    for i in students:
        avg=0
        avg=(i["math"]+i["science"])/2
        result.append(avg)
    for i in result:
        if i>90:
            grades.append("A")
        elif i>70:
            grades.append("B")
        elif i>60:
            grades.append("C")
    return grades

def process_students(students,choice):
    print("Process student is called")
    return choice(students)

option=input("Enter correct choice\n")
if option=="names":
    fans=process_students(students,get_names)
elif option=="avg":
    fans=process_students(students,get_avg_score)
elif option=="grades":
    fans=process_students(students,get_grade)
print(f"{fans}")