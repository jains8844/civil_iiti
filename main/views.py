from django.shortcuts import render
from .models import About, Workshop, Conference, Seminar, Industrial_Visit, Industrial_Visit_Picture, Gallery, Computational_Lab, News, Slideshow, Event, Recruitment, Staff, Phd_Student, BTech_Student, Research_Area, Sponsored_Project, Consultancy_Project, Teaching_Lab, Research_Lab
import datetime
# Create your views here.
def index(request):
    news1 = News.objects.all()
    ss = Slideshow.objects.all()
    events = Event.objects.all()
    for i in events:
        if(i.End_Date < datetime.datetime.today().date()):
            i.Past = True
        i.save()
    events = Event.objects.filter(Past=False)
    events_past = Event.objects.filter(Past=True)
    recruit = Recruitment.objects.all()
    for i in recruit:
        s = str(i.Deadline)
        if(i.Deadline < datetime.datetime.today().date()):
            i.delete()
            i.Past = True
    return render(request, 'main/index.html', {'news' : news1, "slideshow" : ss, "events" : events, "recruit" : recruit, "events_past" : events_past})

def staff(request):
    staff = Staff.objects.all()
    return render(request, 'main/staff.html', {'staffs' : staff})

def phd(request):
    students = Phd_Student.objects.all()
    return render(request, 'main/phd.html', {"students" : students})

def btech(request):
    students = BTech_Student.objects.all()
    x = BTech_Student.objects.values('Year').distinct()
    context = dict()
    for i in x:
        context[i["Year"]]=students.filter(Year = i["Year"])
    return render(request, 'main/btech.html', {'dictionary' : context})

def researcharea(request):
    areas = Research_Area.objects.all()
    return render(request, 'main/resareas.html', {'areas' : areas})

def sponsored(request):
    projects = Sponsored_Project.objects.all()
    return render(request, 'main/sponsored.html', {'projects' : projects})

def consultancy(request):
    projects = Consultancy_Project.objects.all()
    return render(request, 'main/consultancy.html', {'projects' : projects})

def teaching(request):
    labs = Teaching_Lab.objects.all()
    return render(request, 'main/teaching.html', {'labs' : labs})

def research_lab(request):
    labs = Research_Lab.objects.all()
    return render(request, 'main/researchlab.html', {'labs' : labs})

def computational(request):
    labs  = Computational_Lab.objects.all()
    return render(request, 'main/computational.html', {'labs' : labs})

def workshop(request):
    workshops = Workshop.objects.all()
    return render(request, 'main/workshops.html', {'workshops' : workshops})

def conferences(request):
    conferences = Conference.objects.all()
    return render(request, 'main/conferences.html', {'conferences' : conferences})

def contact(request):
    return render(request, 'main/contact.html')

def about(request):
    messages = About.objects.all()
    return render(request, 'main/about.html', {'messages' : messages})

def seminar(request):
    seminars = Seminar.objects.all()
    return render(request, 'main/seminars.html', {'seminars' : seminars})

def industrial(request):
    visits = Industrial_Visit.objects.all()
    return render(request, 'main/indvisits.html', {"visits" : visits})

def gallery(request):
    pictures = Gallery.objects.all()
    return render(request, 'main/gallery.html', {"pictures" : pictures})
