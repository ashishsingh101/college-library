from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy, reverse
import datetime
from django.http import HttpResponse
from .models import StudentRecords

class CreateRecord(CreateView):
    model = StudentRecords
    template_name = 'create.html'
    fields = ['rollNo', 'dateIssued', 'yearOfAdmission', 'name', 'branch','emailId','phoneNo']

class MainPage(TemplateView):
    template_name = 'mainpage.html'

    def post(self, request):
        roll = request.POST['roll']
        student = StudentRecords.objects.all().filter(rollNo=str(roll))
        id = None
        if student:
            id = student[0].id

        return render(request, self.template_name, {'student':student, 'roll':roll})

class SearchPage(ListView):
    template_name = 'search.html'
    model = StudentRecords
    context_object_name = 'student_rollno'
    date = datetime.datetime.now()
    year = date.year
    month = date.month

    def post(self, request):
        roll = request.POST['roll']
        student = StudentRecords.objects.all().filter(rollNo=str(roll))
        yearofstudy = int(0)
        if student:
            yearofstudy = int(self.year) - int(student[0].yearOfAdmission)
        if int(self.month)-6 >= 0:
            yearofstudy += 1
        
        return render(request, self.template_name, {'rollno':roll, 'student':student, 'yearofstudy':yearofstudy})

class IssuedBooks(UpdateView):
    model = StudentRecords
    template_name = 'addBooks.html'
    fields = ['book1', 'book2', 'book3']
