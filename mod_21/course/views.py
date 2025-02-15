from django.contrib import messages
from django.shortcuts import render, redirect 
from . import models
from . import forms
from django.http import HttpResponse
from django.views.generic import ListView, UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy


#THis is for html forms
# # Create your views here.
# def home(request):
#     print(request.POST)
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         password = request.POST.get('password')
#         checkbox = request.POST.get('checkbox')
#         photo = request.FILES.get('photo')


#         if checkbox == 'on':
#             checkbox = True
#         else:
#             checkbox = False


#         course = models.course(name=name, email=email, phone=phone, password=password, checkbox=checkbox, photo=photo)
#         course.save()

#         #return HttpResponse("Course Object created successfully")

#     return render(request, 'student/index.html')
    


#THis is for Model forms


def create_student(request):
    
    if request.method == 'POST':
        form = forms.courseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Student Created successfully.')

            return redirect('home')
    else:
        form = forms.courseForm()
    return render(request, 'student/create_edit_student.html', {'form': form})
#function based view
def home(request):
    students = models.course.objects.all()
    return render(request, 'student/index.html', {'students': students}) 

#class based view
class Studentlist(ListView):
    model = models.course
    template_name = 'student/index.html'
    context_object_name = 'students'


def update_student(request, id):
    student = models.course.objects.get(id=id)
    form = forms.courseForm(instance=student)  # user er ager data diye form fill up korlam
    # form = forms.StudentForm()

    if request.method == 'POST':  # 1. user post request koreche
        form = forms.courseForm(request.POST, request.FILES, instance=student)  # 2. user er post data form e boshalam
        if form.is_valid():  # 3. user input validation kortechi
            form.save()  # 4. user input save korlam
            messages.add_message(request, messages.SUCCESS, 'Student Updated successfully.')
            return redirect('home')

    return render(request, 'student/create_edit_student.html', {'form': form, 'edit': True})

#class based view
class UpdateStudentData(UpdateView):
    form_class = forms.courseForm
    model = models.course
    template_name = 'student/create_edit_student.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Student Updated Successfully')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context


def delete_student(request, id):
    student = models.course.objects.get(id=id)
    student.delete()
    messages.add_message(request, messages.SUCCESS, 'Student Deleted successfully.')
    return redirect('home')

#class based delete view
class DeleteStudent(DeleteView):
    model = models.course
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    template_name = 'student/delete_student.html'

    def delete(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, 'Student deleted Successfully')
        return super().delete(request, *args, **kwargs)



class CreateStudent(CreateView):
    form_class = forms.courseForm
    success_url = reverse_lazy('home')
    template_name = 'student/create_edit_student.html'

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'Student Created Successfully')
        return super().form_valid(form)