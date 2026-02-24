from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Student
from .forms import StudentForm

@login_required
def student_list(request):
    students = Student.objects.filter(user=request.user)
    return render(request, 'students/student_list.html', {'students': students})

def about(request):
    return render(request, 'students/about.html')

@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('students:student_list')
    else:
        form = StudentForm()
    return render(request,'students/add_student.html', {'form': form})

@login_required
def update_student(request,id):
    student = get_object_or_404(Student, id=id, user=request.user)

    if request.method == "POST":
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            student.save()
            return redirect('students:student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/update_student_list.html', {'form': form})

@login_required
def delete_student(request,id):
    student = get_object_or_404(Student, id=id, user=request.user)
    if request.method =="POST":
        student.delete()
        return redirect('students:student_list')
    return render(request, 'students/confirm_delete.html', {'student': student})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('students:student_list')
    else:
        form = UserCreationForm()
    return render(request,'registration/registor.html',{'form':form})
