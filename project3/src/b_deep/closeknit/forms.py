from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from closeknit.models import UserAccount, Comment, Post

class SignUpForm(forms.Form):
    fname = forms.CharField()
    lname = forms.CharField()
    email = forms.EmailField()
    username = forms.CharField()
    friend_code = forms.CharField()
    password = forms.CharField()
    re_password = forms.CharField()

    def clean_user(self):
        data = self.cleaned_data['fname','lname','email','username','friend_code','password','re_password']

        if password != re_password:
            raise ValidationError(_('Passwords do not match.'))

        return data

class AddFriendForm(forms.Form):
    username = forms.CharField(label='username' , help_text ="Enter a Username to Add")
    friend_code = forms.CharField(label = 'friend_code', help_text="Enter a Friend Code to Add")
    
    def clean(self):
        username_data = self.cleaned_data.get('username') 
        friend_code_data = self.cleaned_data.get('friend_code')
        try:
            user = User.objects.get(username = username_data)
        except User.DoesNotExist:
            user = None
        
        #check if the username exists and friend code is correct
        if user != None:
            if user.useraccount.friend_code != friend_code_data:
                raise ValidationError(_("This User does not want to be friends with you :("))
        elif user == None:
            raise ValidationError(_("This User does not exist :("))
        return username_data







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

            if User.objects.filter(email = data):
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
            if User.objects.filter(username = data):
                raise ValidationError(_("This username is already in use. Please enter a different username."))

        #returns the cleaned data
        return data

class SettingsFriendCodeForm(forms.Form):
    friend_code = forms.CharField(help_text="Enter a Friend Code to Add")

    def clean(self):
        data = self.cleaned_data.get('friend_code')

        print("clean friend code a girdik")
        print(data)

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

        if new_data != confirm_data:
            raise ValidationError(_("New passwords do not match."))

        #returns the cleaned data
        return new_data

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text_content',)
