from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('staff', views.staff, name="Staff"),
    path('phd', views.phd, name="Ph.D"),
    path('btech', views.btech, name="B.Tech"),
    path('researchareas', views.researcharea, name="Research Area"),
    path('sponsred', views.sponsored, name="Sponsored"),
    path('consultancy', views.consultancy, name="Consultancy"),
    path('teaching', views.teaching, name="Teaching"),
    path('researchlab', views.research_lab, name="Research Labs"),
    path('computational', views.computational, name="Computational"),
    path('workshop', views.workshop, name="Workshop"),
    path('conferences', views.conferences, name="Conferences"),
    path('seminar', views.seminar, name="Seminar"),
    path('industrial', views.industrial, name="Industrial"),
    path('gallery', views.gallery, name="Gallery"),
    path('contact', views.contact, name="Contact"),
    path('about', views.about, name="About"),
]

if(settings.DEBUG):
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
