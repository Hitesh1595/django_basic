from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.


def index(request):
    return render(request,'firstapp/index.html')


def formpage(request):
    form = forms.FormName()

    print(request.method)
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print(form.cleaned_data.get("name"))
            print(form.cleaned_data.get("email"))
        
    return render(request,"firstapp/form_page.html",context  = {'form':form})


