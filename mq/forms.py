'''
Creates the form for the user to input the starting 
and ending locations.
'''
from django import forms

class LocationsForm(forms.Form):
    start_location = forms.CharField()
    end_location = forms.CharField()
