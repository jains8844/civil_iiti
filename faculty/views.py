from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from . import forms
from .models import Faculty, Research_Interest, Education, WorkExperience, Publication

def ulogin(request):
    if(request.user.is_authenticated):
        return HttpResponseRedirect(reverse("login-home"))
    if(request.method=="POST"):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        if(user):
            if(user.is_active):
                login(request, user)
                return HttpResponseRedirect(reverse("login-home"))
            else:
                return render(request, 'faculty/login.html', {"error_messages": "Account Not Active"})
        else:
            return render(request, 'faculty/login.html', {"error_messages": "Login Failed"})
    else:
        return render(request, 'faculty/login.html')

def login_home(request):
    if not(request.user.is_authenticated):
        return render(request, 'faculty/login.html', {"error_messages": "Login First"})
    profile = None
    try:
        profile = Faculty.objects.get(user=request.user)
    except:
        pass
    return render(request, "faculty/login-home.html", {"profile": profile})

def ulogout(request):
    logout(request)
    return render(request, 'faculty/login.html')


def profile(request):
    if not(request.user.is_authenticated):
        return render(request, 'faculty/login.html', {"error_messages": "Login First"})
    form = forms.Profile(instance = Faculty.objects.get(user=request.user))
    if(request.method=="POST"):
        form = forms.Profile(request.POST, request.FILES,  instance = Faculty.objects.get(user=request.user) or None)
        if(form.is_valid()):
            form.save(commit=True)
            return HttpResponseRedirect("login_home")
        else:
            return render(request, "faculty/form.html", {'form':form, 'profile':Faculty.objects.get(user=request.user), 'error_messages':"Invalid Form"})
    return render(request, "faculty/form.html", {'form':form, 'profile':Faculty.objects.get(user=request.user)})

def addprofile(request):
    if not(request.user.is_authenticated):
        return render(request, 'faculty/login.html', {"error_messages": "Login First"})
    form = forms.Profile()
    if(request.method=="POST"):
        form = forms.Profile(request.POST, request.FILES)
        if(form.is_valid()):
            x = form.save(commit=False)
            x.user=request.user
            x.save()
            print(x)
            return HttpResponseRedirect(reverse("login-home"))
        else:
            return render(request, 'faculty/form.html', {'form': form, 'error_messages': "Invalid Form"})
    return render(request, 'faculty/form.html', {'form' : form})

def res_interest(request):
    if not(request.user.is_authenticated):
        return render(request, 'faculty/login.html', {"error_messages": "Login First"})
    res_int = Research_Interest.objects.filter(user=request.user)
    profile = None
    try:
        profile = Faculty.objects.get(user=request.user)
    except:
        pass
    return render(request, 'faculty/res_int.html', {'interests':res_int, 'profile' : profile})

def edit_res_int(request, res_id):
    if not(request.user.is_authenticated):
        return render(request, 'faculty/login.html', {"error_messages": "Login First"})
    obj = get_object_or_404(Research_Interest, pk=res_id)
    res_int = Research_Interest.objects.filter(user=request.user)
    profile = None
    try:
        profile = Faculty.objects.get(user=request.user)
    except:
        pass
    if(obj.user!=request.user):
        return render(request, 'faculty/res_int.html', {'interests':res_int, 'profile':profile, 'error_messages':"You do not have Premission for that"})
    form = forms.Res_Interest(instance = obj)
    if(request.method=="POST"):
        form = forms.Res_Interest(request.POST, instance = obj)
        if(form.is_valid()):
            form.save(commit=True)
            return HttpResponseRedirect(reverse("research interest"))
        else:
            return HttpResponseRedirect(reverse('edit_res_int', args=[res_id]))
    return render(request, "faculty/form.html", {'form':form, 'profile' : profile})

def add_res_int(request):
    if not(request.user.is_authenticated):
        return render(request, 'faculty/login.html', {"error_messages": "Login First"})
    profile = None
    try:
        profile = Faculty.objects.get(user=request.user)
    except:
        pass
    form = forms.Res_Interest()
    if(request.method=="POST"):
        form = forms.Res_Interest(request.POST)
        if(form.is_valid()):
            x = form.save(commit=False)
            x.user=request.user
            x.save()
            return HttpResponseRedirect(reverse("research interest"))
        return render(request, "faculty/form.html", {'form':form, 'error_message':"Invalid Form", 'profile' : profile})
    return render(request, "faculty/form.html", {'form':form, 'profile' : profile})

def del_res_int(request, res_id):
    if not(request.user.is_authenticated):
        return render(request, 'faculty/login.html', {"error_messages": "Login First"})
    profile = None
    try:
        profile = Faculty.objects.get(user=request.user)
    except:
        pass
    obj = get_object_or_404(Research_Interest, pk=res_id)
    if(obj.user!=request.user):
        return render(request, 'faculty/res_int.html', {'interests':res_int, 'profile' : profile, 'error_messages':"You do not have Premission for that"})
    obj.delete()
    return HttpResponseRedirect(reverse("research interest"))


def education(request):
    if not(request.user.is_authenticated):
        return render(request, 'faculty/login.html', {"error_messages": "Login First"})
    education = Education.objects.filter(user=request.user)
    profile = None
    try:
        profile = Faculty.objects.get(user=request.user)
    except:
        pass
    return render(request, 'faculty/education.html', {'education':education, 'profile' : profile})

def add_edu(request):
    if not(request.user.is_authenticated):
        return render(request, 'faculty/login.html', {"error_messages": "Login First"})
    profile = None
    try:
        profile = Faculty.objects.get(user=request.user)
    except:
        pass
    form = forms.Educations()
    if(request.method=="POST"):
        form = forms.Educations(request.POST)
        if(form.is_valid()):
            x = form.save(commit=False)
            x.user=request.user
            x.save()
            return HttpResponseRedirect(reverse("education"))
        return render(request, "faculty/form.html", {'form':form, 'profile' : profile, 'error_message':"Invalid Form"})
    return render(request, "faculty/form.html", {'form':form, 'profile' : profile})

def edit_edu(request, edu_id, error_messages=""):
    if not(request.user.is_authenticated):
        return render(request, 'faculty/login.html', {"error_messages": "Login First"})
    profile = None
    try:
        profile = Faculty.objects.get(user=request.user)
    except:
        pass
    obj = get_object_or_404(Education, pk=edu_id)
    education = Education.objects.filter(user=request.user)
    if(obj.user!=request.user):
        return render(request, 'faculty/education.html', {'interests':education, 'profile' : profile, 'error_messages':"You do not have Premission for that"})
    form = forms.Educations(instance = obj)
    if(request.method=="POST"):
        form = forms.Educations(request.POST, instance = obj)
        if(form.is_valid()):
            form.save(commit=True)
            return HttpResponseRedirect(reverse("education"))
        else:
            return HttpResponseRedirect(reverse('edit_edu', args=[edu_id, "Invalid Form"]))
    return render(request, "faculty/form.html", {'form':form, 'profile' : profile, 'error_messages' : error_messages})

def del_edu(request, edu_id):
    if not(request.user.is_authenticated):
        return render(request, 'faculty/login.html', {"error_messages": "Login First"})
    profile = None
    try:
        profile = Faculty.objects.get(user=request.user)
    except:
        pass
    obj = get_object_or_404(Education, pk=edu_id)
    if(obj.user!=request.user):
        return render(request, 'faculty/res_int.html', {'interests':res_int, 'profile' : profile, 'error_messages':"You do not have Premission for that"})
    obj.delete()
    return HttpResponseRedirect(reverse("education"))

def add_work(request):
    if not(request.user.is_authenticated):
        return render(request, 'faculty/login.html', {"error_messages": "Login First"})
    profile = None
    try:
        profile = Faculty.objects.get(user=request.user)
    except:
        pass
    form = forms.Work()
    if(request.method=="POST"):
        form = forms.Work(request.POST)
        if(form.is_valid()):
            x = form.save(commit=False)
            x.user=request.user
            x.save()
            return HttpResponseRedirect(reverse("works"))
        return render(request, "faculty/form.html", {'form':form, 'error_message':"Invalid Form", 'profile' : profile})
    return render(request, "faculty/form.html", {'form':form, 'profile' : profile})

def work(request):
    if not(request.user.is_authenticated):
        return render(request, 'faculty/login.html', {"error_messages": "Login First"})
    profile = None
    try:
        profile = Faculty.objects.get(user=request.user)
    except:
        pass
    works = WorkExperience.objects.filter(user=request.user)
    return render(request, 'faculty/works.html', {'works':works, 'profile' : profile})

def edit_work(request, work_id, error_messages=""):
    if not(request.user.is_authenticated):
        return render(request, 'faculty/login.html', {"error_messages": "Login First"})
    profile = None
    try:
        profile = Faculty.objects.get(user=request.user)
    except:
        pass
    obj = get_object_or_404(WorkExperience, pk=work_id)
    works = WorkExperience.objects.filter(user=request.user)
    if(obj.user!=request.user):
        return render(request, 'faculty/works.html', {'work':works, 'profile' : profile, 'error_messages':"You do not have Premission for that"})
    form = forms.Work(instance = obj)
    if(request.method=="POST"):
        form = forms.Work(request.POST, instance = obj)
        if(form.is_valid()):
            form.save(commit=True)
            return HttpResponseRedirect(reverse("works"))
        else:
            return HttpResponseRedirect(reverse('edit_edu', args=[edu_id, "Invalid Form"]))
    return render(request, "faculty/form.html", {'form':form, 'profile' : profile, 'error_messages' : error_messages})

def del_work(request, work_id):
    if not(request.user.is_authenticated):
        return render(request, 'faculty/login.html', {"error_messages": "Login First"})
    profile = None
    try:
        profile = Faculty.objects.get(user=request.user)
    except:
        pass
    obj = get_object_or_404(WorkExperience, pk=work_id)
    if(obj.user!=request.user):
        return render(request, 'faculty/publication.html', {'work':works, 'profile' : profile, 'error_messages':"You do not have Premission for that"})
    obj.delete()
    return HttpResponseRedirect(reverse("works"))

def add_pub(request):
    if not(request.user.is_authenticated):
        return render(request, 'faculty/login.html', {"error_messages": "Login First"})
    profile = None
    try:
        profile = Faculty.objects.get(user=request.user)
    except:
        pass
    form = forms.Publications()
    if(request.method=="POST"):
        form = forms.Publications(request.POST)
        if(form.is_valid()):
            x = form.save(commit=False)
            x.user=request.user
            x.save()
            return HttpResponseRedirect(reverse("publication"))
        return render(request, "faculty/form.html", {'form':form, 'profile' : profile})
    return render(request, "faculty/form.html", {'form':form, 'profile' : profile})

def pub(request):
    if not(request.user.is_authenticated):
        return render(request, 'faculty/login.html', {"error_messages": "Login First"})
    profile = None
    try:
        profile = Faculty.objects.get(user=request.user)
    except:
        pass
    publications = Publication.objects.filter(user=request.user)
    return render(request, 'faculty/publication.html', {'publications':publications, 'profile' : profile})

def edit_pub(request, pub_id, error_messages=""):
    if not(request.user.is_authenticated):
        return render(request, 'faculty/login.html', {"error_messages": "Login First"})
    profile = None
    try:
        profile = Faculty.objects.get(user=request.user)
    except:
        pass
    obj = get_object_or_404(Publication, pk=pub_id)
    publications = Publication.objects.filter(user=request.user)
    if(obj.user!=request.user):
        return render(request, 'faculty/publication.html', {'publications':publications, 'profile' : profile, 'error_messages':"You do not have Premission for that"})
    form = forms.Publications(instance = obj)
    if(request.method=="POST"):
        form = forms.Publications(request.POST, instance = obj)
        if(form.is_valid()):
            form.save(commit=True)
            return HttpResponseRedirect(reverse("publication"))
        else:
            return HttpResponseRedirect(reverse('edit_pub', args=[pub_id, "Invalid Form"]))
    return render(request, "faculty/form.html", {'form':form, 'profile' : profile, 'error_messages' : error_messages})

def del_pub(request, pub_id):
    if not(request.user.is_authenticated):
        return render(request, 'faculty/login.html', {"error_messages": "Login First"})
    profile = None
    try:
        profile = Faculty.objects.get(user=request.user)
    except:
        pass
    obj = get_object_or_404(Publication, pk=pub_id)
    publications = Publication.objects.filter(user=request.user)
    if(obj.user!=request.user):
        return render(request, 'faculty/publication.html', {'publications': publications, 'profile' : profile, 'error_messages':"You do not have Premission for that"})
    obj.delete()
    return HttpResponseRedirect(reverse("publication"))

def index(request):
    users = User.objects.all()
    details = Faculty.objects.all()
    res_int = Research_Interest.objects.all()
    context = {'users' : User, 'hod' : details.filter(designation='Head of the Discipline'), "associate": details.filter(designation='Associate Professor'), "assistant": details.filter(designation='Assistant Professor'), "assistantII": details.filter(designation='Assistant Professor(Grade II)'), "visiting": details.filter(designation='Visiting Assistant Professor'), "adjunct": details.filter(designation='Adjunct Professor'),  'res_int': res_int }
    return render(request, "faculty/home.html", context)

def detail(request, fac_id):
    return render(request, "faculty/facdetail.html", {'profile' : Faculty.objects.get(pk=fac_id), 'id' : fac_id})

def facedu(request, fac_id):
    return render(request, "faculty/facedu.html", {'education' : Education.objects.filter(user=Faculty.objects.get(pk=fac_id).user), 'id' : fac_id, 'profile' : Faculty.objects.get(pk=fac_id)})

def facwork(request, fac_id):
    return render(request, "faculty/facwork.html", {'works' : WorkExperience.objects.filter(user=Faculty.objects.get(pk=fac_id).user), 'id' : fac_id, 'profile' : Faculty.objects.get(pk=fac_id)})

def facpub(request, fac_id):
    return render(request, "faculty/facpub.html", {'publications' : Publication.objects.filter(user=Faculty.objects.get(pk=fac_id).user), 'id' : fac_id, 'profile' : Faculty.objects.get(pk=fac_id)})

def facres(request, fac_id):
    return render(request, "faculty/facres.html", {'res_int' : Research_Interest.objects.filter(user=Faculty.objects.get(pk=fac_id).user), 'id' : fac_id, 'profile' : Faculty.objects.get(pk=fac_id)})

def contact(request):
    if not(request.user.is_authenticated):
        return render(request, 'faculty/login.html', {"error_messages": "Login First"})
    profile = None
    try:
        profile = Faculty.objects.get(user=request.user)
    except:
        pass
    return render(request, 'faculty/contact.html', {'profile' : profile})

def faccontact(request, fac_id):
    return render(request, "faculty/faccontact.html", {'profile' : Faculty.objects.get(user=Faculty.objects.get(pk=fac_id).user), 'id' : fac_id, 'profile' : Faculty.objects.get(pk=fac_id)})
