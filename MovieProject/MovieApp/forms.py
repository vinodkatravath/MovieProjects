from django import forms
from MovieApp.models import Movies
'''
class MoviesForm(forms.ModelForm):
    #no seperate fields are required
    class Meta:
        model=Movies
        fields='__all__'
'''
class DateInput(forms.DateInput):
 input_type = 'date';
#=> Now define/modify ModelForm class as follows:-
class MoviesForm(forms.ModelForm):
 releasedate = forms.DateField(widget=DateInput())
 moviename = forms.CharField()
 actor = forms.CharField()
 actress = forms.CharField()
 rating = forms.FloatField()
 class Meta:
     model = Movies
     fields = ('releasedate','moviename', 'actor', 'actress', 'rating');