from django.forms import ModelForm
from . models import Room
from django import forms
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class  Meta:
      model = Room #specifying the model you want to create a form for
      fields = '__all__' #will get all the values spesified in the Room model
      exclude = ['host','participants']#exclude host and participants from showing up when creating a room.we
      #want host to be added automatically
      
class RegistrationForm(forms.Form):
  username = forms.CharField(max_length=200)
  email = forms.EmailField(label="Email")
  password = forms.CharField(label="password",widget=forms.PasswordInput)
  confirm_password = forms.CharField(label = 'cornfirm password',widget=forms.PasswordInput)
  
  
class UserForm(ModelForm):
  class Meta:
    model = User
    fields = ['username','email']