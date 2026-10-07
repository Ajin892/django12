from django.shortcuts import render

def clas(request):
    emp = [
        {'name':'a','jobtitle':'aa','salary':123,'time':'part'},
        {'name':'b','jobtitle':'bb','salary':123,'time':'full'},
        {'name':'c','jobtitle':'cc','salary':123,'time':'full'}
        ]
    context={'emp':emp}
    return render(request,'index.html',context)
