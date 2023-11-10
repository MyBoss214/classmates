from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Classmate


class ClassmateList(ListView):
    model = Classmate

class ClassmateView(DetailView):
    model = Classmate

class ClassmateCreate(CreateView):
    model = Classmate
    fields = ['firstname', 'lastname', 'age', 'address', 'gender']
    success_url = reverse_lazy('classmate_list')
    
    def form_valid(self, form):
        #logic
        if not self.custom_validation_logic(form):
            # If fail return error
            return self.form_invalid(form)

        # If valid, proceed
        return super().form_valid(form)

    def custom_validation_logic(self, form):
        # logic
        # Check form data and return True if validation passes, or False if it fails

        # age  validation:
        age = form.cleaned_data.get('age')
        if age < 18:
            form.add_error('age', 'Age must be 18 or older.')
            return False

        # Add more if want.

        return True

class ClassmateDelete(DeleteView):
    model = Classmate
    success_url = reverse_lazy('classmate_list')




class ClassmateUpdate(UpdateView):
    model = Classmate
    fields = ['firstname', 'lastname', 'age', 'address', 'gender']
    success_url = reverse_lazy('classmate_list')

    def form_valid(self, form):
        #logic
        if not self.custom_validation_logic(form):
            # If fail return error
            return self.form_invalid(form)

        # If valid, proceed
        return super().form_valid(form)

    def custom_validation_logic(self, form):
        # logic
        # Check form data and return True if validation passes, or False if it fails

        # age  validation:
        age = form.cleaned_data.get('age')
        if age < 18:
            form.add_error('age', 'Age must be 18 or older.')
            return False

        # Add more if want.

        return True

