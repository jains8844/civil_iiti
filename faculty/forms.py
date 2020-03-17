from django import forms
from django.contrib.auth.models import User

from .models import Faculty, Research_Interest, Education, WorkExperience, Publication

class Res_Interest(forms.ModelForm):
    class Meta:
        model = Research_Interest
        fields = ['interest']
        widgets = {'interest':forms.Textarea(attrs={'cols':50, 'rows':1})}

class Profile(forms.ModelForm):
    designation = forms.ChoiceField(choices = Faculty.choice)
    class Meta:
        model = Faculty
        fields = ['photo', 'name', 'designation', 'office', 'email', 'mobile', 'phone']
        widgets = {'name':forms.Textarea(attrs={'cols':50, 'rows':1}),'designation':forms.Textarea(attrs={'cols':50, 'rows':1}),'office':forms.Textarea(attrs={'cols':50, 'rows':1}),'email':forms.Textarea(attrs={'cols':50, 'rows':1}),'mobile':forms.Textarea(attrs={'cols':50, 'rows':1}),'phone':forms.Textarea(attrs={'cols':50, 'rows':1})}

class Educations(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['title', 'description']
        widgets = {'title':forms.Textarea(attrs={'cols':50, 'rows':1}), 'description':forms.Textarea(attrs={'cols':50, 'rows':4})}

class Work(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['title', 'description']
        widgets = {'title':forms.Textarea(attrs={'cols':50, 'rows':1}), 'description':forms.Textarea(attrs={'cols':50, 'rows':4})}

class Publications(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['title', 'description']
        widgets = {'title':forms.Textarea(attrs={'cols':50, 'rows':1}), 'description':forms.Textarea(attrs={'cols':50, 'rows':4})}
