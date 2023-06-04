from django import forms
from django.forms import ModelForm
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"  # include all fields in form
        # fields = ("title",)  # include particular fileds of model in form

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Listeye Eklemek istediğiniz veriyi giriniz",
            }
        ),
    )

    completed = forms.CharField(
        required=False,
        widget=forms.widgets.CheckboxInput(attrs={"class": "form-check-input"}),
    )