from django.contrib import admin

# Register your models here.
from django import forms
from django.core.exceptions import ValidationError
from django.contrib import admin
from .models import Recipe

def validate_title(value):
    words = value.split()
    if len(words) < 1:
        raise ValidationError("Title Kami bilan 1 ta so'zdan iborat bo'lishi kerak")

class RecipeForm(forms.ModelForm):
    title = forms.CharField(validators=[validate_title])

    class Meta:
        model = Recipe
        fields = '__all__'

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    form = RecipeForm
    list_display = ('title', 'image', 'body')
