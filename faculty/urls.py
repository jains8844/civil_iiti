from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
path('login', views.ulogin, name='login'),
path('login_home', views.login_home, name="login-home"),
path('edit_profile', views.profile, name="profile"),
path('res_int', views.res_interest, name="research interest"),
path('logout', views.ulogout, name="logout"),
re_path(r'^edit_res_int/(?P<res_id>[0-9]+)$', views.edit_res_int, name="edit_res"),
re_path(r'^del_res_int/(?P<res_id>[0-9]+)$', views.del_res_int, name="del_res"),
path('add_res_int', views.add_res_int, name="add research interest"),
path('education', views.education, name="education"),
path('add_edu', views.add_edu, name="add_edu"),
re_path(r'^edit_edu/(?P<edu_id>[0-9]+)$', views.edit_edu, name="edit_edu"),
re_path(r'^del_edu/(?P<edu_id>[0-9]+)$', views.del_edu, name="del_edu"),
path('works', views.work, name='works'),
path('add_work', views.add_work, name='add_work'),
re_path(r'^edit_work/(?P<work_id>[0-9]+)$', views.edit_work, name="edit_work"),
re_path(r'^del_work/(?P<work_id>[0-9]+)$', views.del_work, name="del_work"),
path('', views.index, name='faculty'),
re_path(r'^(?P<fac_id>[0-9]+)/home$', views.detail, name="fac-detail"),
re_path(r'^(?P<fac_id>[0-9]+)/education$', views.facedu, name="fac-edu"),
re_path(r'^(?P<fac_id>[0-9]+)/works$', views.facwork, name="fac-work"),
re_path(r'^(?P<fac_id>[0-9]+)/publications$', views.facpub, name="fac-pub"),
re_path(r'^(?P<fac_id>[0-9]+)/research$', views.facres, name="fac-res_int"),
path('publications', views.pub, name='publication'),
path('add_pub', views.add_pub, name='add_pub'),
re_path(r'^edit_pub/(?P<pub_id>[0-9]+)$', views.edit_pub, name="edit_pub"),
re_path(r'^del_pub/(?P<pub_id>[0-9]+)$', views.del_pub, name="del_pub"),
path('contact', views.contact, name='contact'),
re_path(r'^(?P<fac_id>[0-9]+)/contact$', views.faccontact, name="fac-contact"),
re_path('add_profile', views.addprofile, name="add-profile")
]

if(settings.DEBUG):
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
