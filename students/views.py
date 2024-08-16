from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Student
from .forms import StudentForm

def index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students': students})

def view_student(request, id):
    student = get_object_or_404(Student, pk=id)
    return render(request, 'students/view_student.html', {'student': student})

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the model
            return render(request, 'students/add.html', {
                'form': StudentForm(),
                'success': True
            }) 
    else:
        form = StudentForm()
        
    return render(request, 'students/add.html', {
        'form': form
    })

def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return render(request, 'students/edit.html', {
            'form': form,
            'success': True
        })
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {
        'form': form
    })

def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))