from django import forms
from .models import get_mens,get_women,get_kids,create_user

class form1(forms.ModelForm):
    class Meta:
        model = get_mens
        fields = ['product_img', 'product_Name', 'product_price', 'product_details']

class form2(forms.ModelForm):
    class Meta:
        model = get_women
        fields = ['product_img', 'product_Name', 'product_price', 'product_details']

class form3(forms.ModelForm):
    class Meta:
        model = get_kids
        fields = ['product_img', 'product_Name', 'product_price', 'product_details']

class register_user(forms.ModelForm):
    class Meta:
        model = create_user
        fields = ['name', 'phone', 'password']

class login_user(forms.Form):
    phone = forms.CharField(label='Your Phone', max_length=15)
    password = forms.CharField(label='Your Password', widget=forms.PasswordInput)