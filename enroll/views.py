from django.shortcuts import render,HttpResponsePermanentRedirect
from .forms import Studentinfo
from django.core import validators
from .models import Student

# Create your views h fffff
def home(request):
    if request.method=="POST":
        stud=Studentinfo(request.POST)
        if stud.is_valid():
            nm=stud.cleaned_data["name"]
            em=stud.cleaned_data["email"]
            pw=stud.cleaned_data["password"]
            ph=stud.cleaned_data["phone"]
            reg=Student(name=nm,email=em,password=pw,phone=ph)
            reg.save()
            return HttpResponsePermanentRedirect("/")
    else:
        stud=Studentinfo()
    show=Student.objects.all()
    return render(request, "enroll/addandshow.html",{"std":stud, "stu":show})



def upadte_data(request,id):
    if request.method=="POST":
        pi=Student.objects.get(pk=id)
        stud=Studentinfo(request.POST,instance=pi)
        if stud.is_valid():
            stud.save()
    else:
        pi=Student.objects.get(pk=id)
        stud=Studentinfo(instance=pi)
    return render(request, "enroll/update.html",{"form":stud})

#this function for delete
def delete_data(request,id):
    if request.method=="POST":
        pi=Student.objects.get(pk=id)
        pi.delete()
        return HttpResponsePermanentRedirect("/")






