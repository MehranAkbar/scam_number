from cgitb import html
from importlib.resources import contents
from multiprocessing import context
from urllib import request
from webbrowser import get
from xml.etree.ElementTree import Comment
from django.shortcuts import render
from django.http import HttpResponse
from .models import phonemodel, reviewmodel
# Create your views here.
def index(request):
    allnumbers = phonemodel.objects.all()
    
    context={'allnumbers': allnumbers}
    return render(request, 'mobilenumber/home.html', context)
def search(request):
    number= request.GET.get('number', None)
    review_text = request.GET.get("review_text", None)
    review_number = request.GET.get("number_review", None)
    review_status = request.GET.get("reviewstatus", None)
    alluser= phonemodel.objects.filter(phone_number=number)
   
    if review_text:
        numbers_forigen_key = phonemodel.objects.filter(phone_number=review_number)
        number_fk = numbers_forigen_key[0]
        review = reviewmodel.objects.create(reviewnumber = number_fk, review = review_text, review_status=review_status )
        review.save()
        alluser= phonemodel.objects.filter(phone_number=review_number)

    if alluser.exists():
        alluser = alluser[0]
        
    print(alluser)
    context= {'alluser': alluser}
    return render(request, 'mobilenumber/search.html', context)
def reportnumber(request):
    reportednumber= request.GET.get('phone',None)
    reportedstatus= request.GET.get('reportedstatus',None)
    reportedcomment=request.GET.get('reportedcomment',None)
    print(reportednumber, type(reportnumber))
    print(reportedstatus)
    print(reportedcomment)
    context = {}
    context["message"] = ""
    if reportednumber:
        reports = phonemodel.objects.create(phone_number = reportednumber, comment=reportedcomment, status= reportedstatus)
        reports.save()
        context["message"] = "Message complaintis recorded"
        
    return render(request, 'mobilenumber/reportnumber.html', context=context)

def allnumbers(request):
    allnumbers = phonemodel.objects.all()
    
    context={'allnumbers': allnumbers}
    return render(request,'mobilenumber/allnumbers.html', context )
