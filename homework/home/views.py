from django.shortcuts import render

def student_list(request):

    students = [
        {"name": "Rajesh", "grade": 85, "passed": True},
        {"name": "Rahul", "grade": 72, "passed": True},
        {"name": "Sruthi", "grade": 45, "passed": False},
        {"name": "Anu", "grade": 90, "passed": True}
    ]

    return render(request, "students/student_list.html", {
        "students": students
    })