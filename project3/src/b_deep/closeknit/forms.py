from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _ 
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



###_________________________________________________________________________________________________###
#The forms for the Settings page: respectively for Updating Email, Username, Friend Code & Password

class SettingsEmailForm(forms.Form):
    email = forms.EmailField(required = True)

    def clean(self):
        data = self.cleaned_data.get('email')

        print("clean emaile girdik")
        print(data)

        #checks if email is valid and then if email already exists
        if data:

            print("xd data dogru")

            if UserAccount.objects.filter(email = data):
                raise ValidationError(_("This email is already in use. Please enter a different email."))

        """
        else:
            print("invalid email bok")
            raise ValidationError(_("Invalid email."))
        """

        #returns the cleaned data
        return data

class SettingsUsernameForm(forms.Form):
    username = forms.CharField(help_text ="Enter a Username to Add")

    def clean(self):
        data = self.cleaned_data.get('username')

        print("clean username girdik")
        print(data)

        if data:
            if UserAccount.objects.filter(username = data):
                raise ValidationError(_("This username is already in use. Please enter a different username."))

        #returns the cleaned data
        return data

class SettingsFriendCodeForm(forms.Form):
    friend_code = forms.CharField(help_text="Enter a Friend Code to Add")

    def clean(self):
        data = self.cleaned_data.get('friend_code')

        print("clean friend code a girdik")
        print(data)

        if data:
            if UserAccount.objects.filter(friend_code = data):
                raise ValidationError(_("This friend code belongs to another user. Please select a different friend code."))

        #returns the cleaned data
        return data

class SettingsPasswordForm(forms.Form):
    old_password = forms.CharField(required = True)
    new_password = forms.CharField(label = "New Password", required = True)
    confirm_password = forms.CharField(label = "Confirm New Password", required = True)

    def clean(self):
        old_data = self.cleaned_data.get('old_password')
        new_data = self.cleaned_data.get('new_password')
        confirm_data = self.cleaned_data.get('confirm_password')

        print("old_data: " + old_data)
        print("new_data: " + new_data)
        print("confirm_data: " + confirm_data)
        print("user password: " + UserAccount.objects.get(pk=1).password)

        if old_data != UserAccount.objects.get(pk=1).password:
           raise ValidationError(_("Invalid current password.")) 
        else:
            if new_data != confirm_data:
                raise ValidationError(_("New passwords do not match."))
        
        #returns the cleaned data
        return new_data
