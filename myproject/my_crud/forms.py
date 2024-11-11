from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'price', 'image']  # Add 'image' field
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter item name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter item description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter item price'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})  # Add widget for image input
        }


# from django import forms
# from .models import Item

# class ItemForm(forms.ModelForm):
#     class Meta:
#         model = Item
#         fields = ['name', 'description', 'price']
