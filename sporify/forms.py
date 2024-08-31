from django import forms

from sporify.models import User, Application


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['name', 'username', 'password', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)

        password = self.cleaned_data['password']
        user.set_password(password)
        user.save()
        return user

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['comment']