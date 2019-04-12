__author__ = 'HuangyiLi'
__date__ = '2019-04-05 21:59'

from django import forms
from operation.models import UserAsk


class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

