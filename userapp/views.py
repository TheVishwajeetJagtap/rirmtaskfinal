from django.shortcuts import render,redirect
from django.views import View
from django.db.models import Q
from .models import UserInfo
from .forms import UserInfoForm
import requests
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os
# Create your views here.
class UserInfoView(View):
     def get(self, request):
        form = UserInfoForm()
        return render(request, 'base.html', {'form': form})

     def post(self, request):
            form = UserInfoForm(request.POST)
            if(form.is_valid()):
                form.save()
            return redirect('/userapp/userlist/')

class UserSearchView(View):
    def get(self,request):
        if request.method=='GET':
            query=request.GET.get('q')
            print(query)
            submitbutton=request.GET.get('submit')
            if query is not None:
                lookups=Q(name__icontains=query) | Q(name__icontains=query)
                results=UserInfo.objects.filter(lookups).distinct()
                context={'results':results,'submitbutton':submitbutton}
                print(context)
                print(results)

                return render(request,'index.html',context)
            else:
                return render(request,'index.html')
        else:
            return render(request,'index.html')

class UserListView(View):
    def get(self,request):
        users = UserInfo.objects.all()
        return render(request,'userlist.html',{"users":users})

def BehanceImageView(request):
    imgdata = behance_image()
    return render(request, "behance.html", {"imgdata": imgdata})

def behance_image():
    response = urllib.request.urlopen("https://www.behance.net/harisnazar04f8")
    html     = response.read()
    soup     = BeautifulSoup(html, features="html.parser")
    images   = soup.findAll("img")

    for image in images:
        yield image["src"]

# class BehanceImageView(View):
#     def get(self,request):
#
#         return render(request,'behance.html',{'imgdata':images})
class Dashboard(View):
    def get(self,request):
        return render(request,'dashboard.html')
