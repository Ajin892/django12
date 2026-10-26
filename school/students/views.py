from django.shortcuts import render

STUDENT_RESULTS = {
    "Ajay": 85,
    "Anu": 92,
    "Rahul": 78,
    "Priya": 95,
}

def home(request):
    students = list(STUDENT_RESULTS.keys())
    return render(request, "students/home.html", {"students": students})

def result(request, name):
    marks = STUDENT_RESULTS.get(name)
    return render(
        request,
        "students/result.html",
        {"name": name, "marks": marks},
    )
