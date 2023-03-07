from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import StudentForm
from .models import Aplication
# Create your views here.


def index(request):
    students = Aplication.objects.all()
    form = StudentForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        form.save()
    form = StudentForm()
    return render(request, 'base.html', {'students': students, "form": form})


def student_delete(request, id):
    student = Aplication.objects.get(id=id)
    student.delete()
    return redirect('home')
def student_edit(request, id):
    stud_edit=Aplication.objects.get(id=id)
    form=StudentForm(request.POST or None, instance=stud_edit)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'student_edit.html', {'form':form, 'stud_edit':stud_edit})
                    
