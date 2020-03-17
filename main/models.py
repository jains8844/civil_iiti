from django.db import models
import datetime
# Create your models here.
class News(models.Model):
    Title = models.CharField(max_length = 256)
    Description = models.CharField(max_length = 1024)
    Link = models.CharField(max_length = 2000, blank = True)
    File = models.FileField(blank = True)
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
    def __str__(self):
        return self.Title

class Slideshow(models.Model):
    Title = models.CharField(max_length = 256)
    File = models.ImageField()
    Caption = models.CharField(max_length=256, blank = True, null = True)
    class Meta:
        verbose_name = 'SlideShow Image'
    def __str__(self):
        return self.Title

class Event(models.Model):
    Event_Title = models.CharField(max_length = 256)
    Description = models.CharField(max_length = 1000)
    Link = models.CharField(max_length = 2000, null = True, blank = True)
    End_Date = models.DateField()
    Past = models.BooleanField(default = False)
    def __str__(self):
        if(self.End_Date < datetime.datetime.today().date()):
            self.Past = True
        self.save()
        return self.Event_Title

class Recruitment(models.Model):
    Title = models.CharField(max_length = 256)
    Description = models.CharField(max_length = 1000)
    Link = models.CharField(max_length = 2000, null = True, blank = True)
    Deadline = models.DateField()
    Past = models.BooleanField(default = False)
    File = models.FileField(blank = True)
    def __str__(self):
        if(self.Deadline < datetime.datetime.today().date()):
            self.Past = True
        self.save()
        return self.Title

class Staff(models.Model):
    Name = models.CharField(max_length=256)
    Image = models.ImageField(blank=True)
    Email = models.EmailField()
    def __str__(self):
        return self.Name
    class Meta:
        verbose_name = 'Staff Member'

class Phd_Student(models.Model):
    Name = models.CharField(max_length=256)
    Roll_no = models.CharField(max_length=10)
    Date_of_joining = models.CharField(max_length=15)
    Supervisor = models.CharField(max_length=256)
    Email = models.EmailField()
    class Meta:
        verbose_name = 'Ph.D Student'
    def __str__(self):
        return self.Name

class BTech_Student(models.Model):
    Name = models.CharField(max_length=256)
    Roll_no = models.CharField(max_length=9)
    now1 = datetime.datetime.now()
    c = []
    y = now1.year
    m = now1.month
    if(m<8):
        y-=1
    for i in range(2016, y+1):
        c.append((str(i), str(i)))
    Year = models.CharField(max_length=4, choices = c, default = str(y))
    class Meta:
        verbose_name = 'B.Tech Student'
    def __str__(self):
        return self.Name

class Research_Area(models.Model):
    Area = models.CharField(max_length=256)
    def __str__(self):
        return self.Area
    class Meta:
        verbose_name = 'Research Area'

class Sponsored_Project(models.Model):
    Project = models.CharField(max_length=1024)
    def __str__(self):
        return self.Project
    class Meta:
        verbose_name = 'Sponsored Project'

class Consultancy_Project(models.Model):
    Project = models.CharField(max_length=1024)
    def __str__(self):
        return self.Project
    class Meta:
        verbose_name = 'Consultancy Project'

class Teaching_Lab(models.Model):
    Lab_name = models.CharField(max_length=256)
    def __str__(self):
        return self.Lab_name
    class Meta:
        verbose_name = 'Teaching Lab'

class Research_Lab(models.Model):
    Lab_name = models.CharField(max_length=256)
    def __str__(self):
        return self.Lab_name
    class Meta:
        verbose_name = 'Research Lab'

class Computational_Lab(models.Model):
    Lab_name = models.CharField(max_length=256)
    def __str__(self):
        return self.Lab_name
    class Meta:
        verbose_name = 'Computational Lab'

class Workshop(models.Model):
    Description = models.CharField(max_length=1024)
    File = models.FileField(blank = True)
    Link = models.CharField(blank = True, max_length=1024)
    def __str__(self):
        return self.Description

class Conference(models.Model):
    Description = models.CharField(max_length= 1024)
    def __str__(self):
        return self.Description

class Seminar(models.Model):
    Description = models.CharField(max_length=1024)
    def __str__(self):
        return self.Description

class Industrial_Visit(models.Model):
    Description = models.CharField(max_length=1024)
    def __str__(self):
        return self.Description
    class Meta:
        verbose_name = 'Industrial Visit'

class Industrial_Visit_Picture(models.Model):
    Description = models.ForeignKey(Industrial_Visit, on_delete=models.CASCADE)
    Photo = models.ImageField()
    def __str__(self):
        return self.Description.Description
    class Meta:
        verbose_name = 'Industrial Visit Image'

class Gallery(models.Model):
    Picture = models.ImageField()
    class Meta:
        verbose_name = 'Gallery Image'
    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))
    image_tag.short_description = 'Image'
    list_display = ['image_tag',]

class About(models.Model):
    Message = models.CharField(max_length = 2048)
    def __str__(self):
        return self.Message
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
