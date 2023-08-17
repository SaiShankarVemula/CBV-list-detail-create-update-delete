from django.shortcuts import render
from app1.models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.


class SchoolList(ListView):
    model=School
    context_object_name='allso'
    # template_name='app1/School_list.html' optional when we deal with Specific Templates
    

class SchoolDetail(DetailView):
    model=School
    context_object_name='DOS'

class SchoolCreate(CreateView):
    model=School
    fields='__all__'


class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'
    
class SchoolDelete(DeleteView):
    model=School
    context_object_name='SDO'
    success_url=reverse_lazy('SchoolList')
    
