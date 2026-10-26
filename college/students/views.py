from django.shortcuts import render, redirect
STUDENT_NAMES = ["Aarav", "Diya", "Rahul", "Priya"]

def student_list(request):
    return render(request, "students/student_list.html", {
        "students": STUDENT_NAMES,
        "welcome_message": "Welcome to the Students page!",
    })

def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        if name:
            STUDENT_NAMES.append(name)
    return redirect("students:list")
