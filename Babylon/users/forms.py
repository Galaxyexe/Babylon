from django import forms
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, User
from Babylon import settings

#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Submit
#from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']

    #to be replaced with regular forms
    '''def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.add_input(
            Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.form_method = 'POST'
        '''
class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    number = forms.CharField()
    class Meta:
        model=User
        fields=['username','email', 'phone']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['profile_pic','description']
