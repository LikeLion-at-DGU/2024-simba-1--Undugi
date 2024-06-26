from django import forms
from accounts.models import Profile
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = Profile
        fields = ['profileImage', 'nickName', 'goal', 'weight', 'major', 'password']
        widgets = {
            'profileImage': forms.FileInput()
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['nickName'].required = False
        self.fields['profileImage'].required = False

    def save(self, commit=True):
        profile = super(UserProfileForm, self).save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user = profile.user
            user.set_password(password)
            if commit:
                user.save()
        if commit:
            profile.save()
        return profile


    def clean_nickName(self):
        nickName = self.cleaned_data.get('nickName')
        if Profile.objects.filter(nickName=nickName).exclude(user=self.instance.user).exists():
            raise forms.ValidationError("This nickname is already in use.")
        return nickName