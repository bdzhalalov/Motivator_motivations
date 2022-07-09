from django import forms
from .models import Motivation


class MotivationForm(forms.ModelForm):


    class Meta:
        
        model = Motivation
        fields = ('motivation',)
        widgets = {
                'motivation': forms.Textarea(attrs={
            'class': 'form-control mt-4',
            'placeholder': 'Напишите свою мотивацию.'
                    }),
        }