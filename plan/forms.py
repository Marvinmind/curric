__author__ = 'Martin'
from django import forms
from plan.models import ModuleSelections, Module
from django.forms.widgets import CheckboxSelectMultiple

"""
class ModuleForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        self.fields["modules"].widget = CheckboxSelectMultiple()
        self.fields["modules"].queryset = Module.objects.all()

"""
class TestForm(forms.Form):

    def __init__(self, *args, **kwargs):
        #args for super may not enclude modules kwarg. Therefore a copy is made and modules removed
        super_kwargs = dict(kwargs)
        del super_kwargs['modules']

        super(TestForm, self).__init__(*args, **super_kwargs)
        self.fields['stuff'] = forms.MultipleChoiceField(kwargs['modules'], widget=forms.CheckboxSelectMultiple(), required=False)
        self.fields['section'] = forms.CharField(widget=forms.HiddenInput())




