from django.shortcuts import render,HttpResponse,redirect
from App.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request,'home.html')

def profile(request):
    userr = Account.objects.get(User=request.user)
    ou = Account.objects.filter(pk__isnull=False)
    otherusers = ou.exclude(User=request.user)
    Personal_interests=[]
    Match_score={}
    for i in userr.Interests:
        Personal_interests.append(i)

    for i in range(0,len(otherusers)): 
        ot_interests =[]
        count=0
        for j in otherusers[i].Interests: 
            ot_interests.append(j)
        for k in range(0,len(ot_interests)):
            if Personal_interests[k]==ot_interests[k]:
                count+=1       
        Match_score[userr.User,otherusers[i].User] = (count/len(ot_interests))*100         
    context={'userr':userr,'Match_score':Match_score.items()}
    return render(request,'profile.html',context)

def contact(request):
    return HttpResponse("Contact")

def signup(request):
    if request.method == 'POST':
        acc = Account()
        user = User()
        acc.User = request.POST['user']
        user.username = acc.User
        acc.Age = request.POST['age']
        acc.Password = request.POST['pass']
        user.set_password(request.POST['pass'])
        acc.Email = request.POST['email']
        user.email = acc.Email
        acc.Interests = [request.POST['Sportselect'],request.POST['Bookselect'],request.POST['Misciselect'],request.POST['Movieselect'],]
        acc.save()
        user.save()
        return redirect('logiN')
    else:
        return render(request,'signup.html')  

def logiN(request):
    if request.method == 'POST':
        user = User()
        username = request.POST['user']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            msg = "Invalid username or password."    
            return render(request,'login.html',context = {'msg':msg,'user':user})
    else:
        return render(request,'login.html')
