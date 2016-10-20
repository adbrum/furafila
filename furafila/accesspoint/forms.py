'''
Created on //2016

@author: Adriano Regis Vidal Leal
@email: adriano.regis.vidal.leal@outlook.com
'''
from django import forms

from furafila.core.models import AccessPoint


class AccessPointForm(forms.ModelForm):
    class Meta:
        model = AccessPoint
        fields = ['group', 'name', 'description']
