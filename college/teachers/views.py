from django.shortcuts import render, redirect
TEACHER_NAMES = ["Mrs. Sharma", "Mr. Kumar", "Ms. Joseph"]

def teacher_list(request):
    return render(request, "teachers/teacher_list.html", {
        "teachers": TEACHER_NAMES,
        "welcome_message": "Welcome to the Teachers page!",
    })

def add_teacher(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        if name:
            TEACHER_NAMES.append(name)
    return redirect("teachers:list")
