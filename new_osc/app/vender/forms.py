from django import forms
from .models import Vender

class VenderForm(forms.ModelForm):
    class Meta:
        model = Vender
        exclude = []


class LoginForm(forms.Form):
    username = forms.CharField(
        label='User Name',
        max_length=10,
        # help_text ='your login credenstials'
    )
    # email = forms.EmailField()
    password = forms.CharField(
        label=u'Password',
        widget=forms.PasswordInput(),
        # help_text ='your secret key'
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Nakh baka username nakh'
        self.fields['password'].widget.attrs['placeholder'] = 'Password to nakhi batay'
        # self.fields['password'].widget.attrs['disabled'] = "disabled"
        # self.fields['password'].widget.attrs['readonly'] = True
        # self.fields['password'].required = False
        


    def clean_username(self):
        data = self.cleaned_data['username']

        try:
            User.objects.get(username=data)
            return data
        except Exception as e:
            raise forms.ValidationError('username not found')