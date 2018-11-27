from django import forms
from closeknit.models import UserAccount

class AddFriendForm(forms.Form):
    username = forms.CharField(label='UserName' , help_text ="Enter a Username to Add")
    friend_code = forms.CharField(label = 'Friend Code', help_text="Enter a Friend Code to Add")
    
    def clean(self):
        username = self.cleaned_data.get('username')
        friend_code = self.cleaned_data.get('friend_code')
        you = UserAccount.objects.get(pk=1)
        #check if the username exists and friend code is correct
        if username and friend_code:
            self.user_cache = authenticate(username=username, friend_code=friend_code)
            if self.user_cache is None:
              raise forms.ValidationError(_("That User does not exist"))
            elif username 
                raise forms.ValidationError(_("This is your username!!"))

               
    return self.cleaned_data
            


# widget=forms.TextInput(attrs={'style' : 'margin-left: 5px;'}),