from django.shortcuts import render,redirect
from .forms import StudentForm,CourseForm
from .models import Student,Course
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def studentView(request):
    template_name = 'app1/studentview.html'
    form = StudentForm()
    context = {'form':form}
    if request.method=='POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('courseview')



    return render(request,template_name,context)

@login_required()
def courseView(request):
    template_name = 'app1/courseview.html'
    form = CourseForm()
    context = {'form':form}

    if request.method=='POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()




    return render(request,template_name,context)

@login_required()
def studentdataView(request):
    template_name = 'app1/studentdata.html'
    data = Student.objects.all()
    context = {'data':data}

    return render(request,template_name,context)



@login_required()
def editView(request,id):
    template_name = 'app1/studentview.html'
    obj= Student.objects.get(sid = id)
    form = StudentForm(instance=obj)
    context = {'form':form}
    if request.method=='POST':
        form = StudentForm(request.POST,instance=obj)

        if form.is_valid():
            form.save()

            return redirect('studentdata')


    return render(request,template_name,context)


def removeView(request,id):
    template_name = 'app1/confirm.html'
    obj = Student.objects.get(sid=id)
    context = {'obj':obj}

    if request.method=='POST':
        obj.delete()

        return redirect('studentdata')



    return render(request,template_name,context)


