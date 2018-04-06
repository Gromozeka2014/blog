from django import forms
from .models import Post, Profile
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name', 'second_name', 'middle_name', 'phone',
                  'email', 'description', 'avatar')


class LoginForm(forms.Form):
    username = forms.CharField(label=u'Имя')
    password = forms.CharField(label=u'Пароль', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if not self.errors:
            user = authenticate(username=cleaned_data['username'],
            password=cleaned_data['password'])
            if user is None:
                raise forms.ValidationError(u'Имя или пароль не подходит')
            self.user = user
        return cleaned_data

    def get_user(self):
        return self.user or None


class RegistrationForm(forms.Form):
    username1 = forms.CharField(label=u'Имя пользователя')
    password1 = forms.CharField(label=u'Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label=u'Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username1', 'password1', 'password2')

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        if not self.errors:
            username1 = self.cleaned_data.get('username1')
            if User.objects.filter(username__exact=username1):
                raise forms.ValidationError(u'Пользователь с таким именем уже существует')
            pass1 = self.cleaned_data.get('password1')
            pass2 = self.cleaned_data.get('password2')
            if pass1 != pass2:
                raise forms.ValidationError(u'Пароли не совпадают')
        return cleaned_data

    def myuser(self):
        name = self.cleaned_data.get('username1')
        passw = self.cleaned_data.get('password1')
        user = User.objects.create(username=name, password=passw)
        user.set_password(passw)
        user.save()
        self.user = user
        return self.user
