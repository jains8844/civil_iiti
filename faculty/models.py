from django.db import models
from django.contrib.auth.models import Permission, User
# Create your models here.

class Faculty(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    photo=models.ImageField()
    name=models.CharField(max_length=256)
    choice = (("Head of the Discipline", "Head of the Discipline"), ("Associate Professor", "Associate Professor"), ("Assistant Professor", "Assistant Professor"), ("Assistant Professor(Grade II)","Assistant Professor(Grade II)"), ("Visiting Assistant Professor", "Visiting Assistant Professor"), ("Adjunct Professor", "Adjunct Professor"))
    designation=models.CharField(max_length=256, choices = choice)
    office=models.CharField(max_length=512)
    email=models.EmailField(max_length=70)
    mobile=models.CharField(max_length=10, blank=True, default="")
    phone=models.CharField(max_length=10, blank=True, default="")
    def __str__(self):
        return self.name

class Research_Interest(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    interest=models.CharField(max_length=256, verbose_name = "Research Interest")
    def __str__(self):
        return self.interest

class Education(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=30, verbose_name = "Education Title")
    description=models.CharField(max_length=512)
    def __str__(self):
        return self.title

class WorkExperience(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=30, verbose_name = "Work Experience Title")
    description=models.CharField(max_length=1024)
    def __str__(self):
        return self.title

class Publication(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=30, verbose_name = "Publication Title")
    description=models.CharField(max_length=2048)
    def __str__(self):
        return self.title
