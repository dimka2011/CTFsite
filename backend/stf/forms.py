from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms
from django.forms import DateInput
from backend.stf.models import Task, Profile
from django_countries.fields import CountryField


class FlagForm(forms.Form):
  user_flag = forms.CharField(label='Flag', max_length=100)
  def clean(self):
      user_flag = super().clean().get('user_flag')
      flag = Task.objects.get('flag')
      print("good")
      if user_flag != flag:
          raise forms.ValidationError("Try again")


class UserRegisterForm(UserCreationForm):
    """
    Переопределенная форма регистрации пользователей
    """

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

    def clean_email(self):
        """
        Проверка email на уникальность
        """
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise ValidationError('Такой email уже используется в системе')
        return email

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы регистрации
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields['username'].widget.attrs.update({"placeholder": 'Придумайте свой логин'})
            self.fields['email'].widget.attrs.update({"placeholder": 'Введите свой email'})
            self.fields['first_name'].widget.attrs.update({"placeholder": 'Ваше имя'})
            self.fields["last_name"].widget.attrs.update({"placeholder": 'Ваша фамилия'})
            self.fields['password1'].widget.attrs.update({"placeholder": 'Придумайте свой пароль'})
            self.fields['password2'].widget.attrs.update({"placeholder": 'Повторите придуманный пароль'})
            self.fields[field].widget.attrs.update({"class": "form-control", "autocomplete": "off"})


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    location = CountryField().formfield(required=False)
    birth_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}), required=False)

    def clean_email(self):
        """
        Проверка email на уникальность
        """
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise ValidationError('Такой email уже используется в системе')
        return email

    class Meta:
        model = Profile
        fields = ('location', 'birth_date')


class TaskForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user_id = User.pk
        super().__init__(*args, **kwargs)
        self.fields['file'].required = False
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control', 'autofocus': ''})
    class Meta:
        model = Task
        file = forms.FileField(required=False)
        fields = ('title', 'describtion', 'flag', 'category', 'file')

