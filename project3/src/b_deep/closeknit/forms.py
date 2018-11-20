from django import forms
from closeknit.models import UserAccount

class AddFriendForm(forms.Form):
    username = forms.CharField(help_text ="Enter a Username to Add")
    friend_code = forms.CharField(help_text="Enter a Friend Code to Add")
    
    def clean(self):
        username = self.cleaned_data.get('username')
        friend_code = self.cleaned_data.get('friend_code')

        #check if the username exists and friend code is correct
        if username and friend_code:
            self.user_cache = authenticate(username=username, friend_code=friend_code)
            if self.user_cache is None:
                raise forms.ValidationError(_("That User does not exist"))
                return username and friend_code


