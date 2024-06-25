from django import forms
from accounts.models import Profile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profileImage', 'nickName', 'goal', 'weight', 'major']
        widgets = {
            'profileImage': forms.FileInput()
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['nickName'].required = False
        self.fields['profileImage'].required = False
