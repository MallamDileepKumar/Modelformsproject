from django.shortcuts import render
from .models import Register
from .forms import RegModelForm, LogForm
from django.http import HttpResponse
from django.views import View
# Create your views here
class HomeView(View):
    def get(self,request):
        return render(request,'home.html')
class RegInput(View):
    def get(self,request):
        return render(request,'reg.html',{'reg': RegModelForm()})
class RegView(View):
    def post(self,request):
        Fm = RegModelForm(request.POST)
        if Fm.is_valid():
            Fm.save()
        return HttpResponse('''<center><h1>Form submitted successfully!</h1></center>''')
class LogInput(View):
    def get(self,request):
        return render(request,'log.html',{'log': LogForm()})
class LogView(View):
    def post(self,request):
        Lf = LogForm(request.POST)
        if Lf.is_valid():
            log = Register.objects.filter(Email=Lf.cleaned_data['Email'],
                           Password=Lf.cleaned_data['Password'],)
            if log:
                return HttpResponse('''<center><h1>Login successfully!</h1></center>''')
            else:
                return HttpResponse('''<center><h1>login failed!</h1></center>''')




