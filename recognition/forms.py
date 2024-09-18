from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from datetime import date,timedelta
#from django.contrib.admin.widgets import AdminDateWidget

class usernameForm(forms.Form):
	username=forms.CharField(max_length=30)


class UserSelectionForm(forms.Form):
    # Dropdown for selecting users
    username = forms.ModelChoiceField(
        queryset=User.objects.all(),  # Fetch all registered users
        widget=forms.Select,  # Render as a dropdown
        empty_label="Select User"  # Placeholder text for the dropdown
    )
class DateForm(forms.Form):
	date=forms.DateField(widget = forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")),initial=date.today)


class UsernameAndDateForm(forms.Form):
	username=forms.CharField(max_length=30)
	date_from=forms.DateField(widget = forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")),initial=date.today().replace(day=1))
	date_to=forms.DateField(widget = forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")),initial=date.today)


class DateForm_2(forms.Form):
	date_from=forms.DateField(widget = forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")),initial=date.today().replace(day=1))
	date_to=forms.DateField(widget = forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")),initial=date.today)
