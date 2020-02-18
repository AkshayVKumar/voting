from django.shortcuts import render
from voting.forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    if request.session.get('username'):
        user=request.session.get('username')
        return render(request,"voting/home.html",context={"username":user})
    return render(request,"voting/home.html")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def cast_vote(request):
    user=request.session.get('username')
    u=User.objects.get(username=user)
    if request.method=="POST":
        candidate_name=request.POST['cand_name']
        c=Candidate.objects.get(name=candidate_name)
        v=c.no_votes+1
        c=Candidate.objects.filter(name=candidate_name).update(no_votes=v)
       
        c=Voter.objects.filter(user=u).update(is_voted=True)
        return render(request,"voting/home.html",context={"username":user})
    else:
        v=Voter.objects.get(user=u)
        candidates=Candidate.objects.filter(constituency=v.constituency)
    return render(request,"voting/cast_vote.html",context={"candidates":candidates,"vote_status":v.is_voted})

def register(request):
    registered=False
    if request.method=="POST":
        userform=UserForm(request.POST)
        constform=VoterForm(request.POST)
        if userform.is_valid() and constform.is_valid():
            user=userform.save(commit=False)
            user.set_password(userform.cleaned_data['password'])
            user.save()

            profile=constform.save(commit=False)
            profile.user=user
            profile.save()
            registered=True
    userform=UserForm()
    constform=VoterForm()
    d={'registered':registered,'userform':userform,'constform':constform}
    return render(request,'register.html',context=d)


def user_login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user and user.is_active:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse("Not a Active User or Invalid username and password")
    return render(request,'user_login.html',context={})