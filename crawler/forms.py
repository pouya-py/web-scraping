from django import forms



class input_form(forms.Form):

    rooms = forms.IntegerField(min_value=0, max_value=5, required=True)
    space = forms.IntegerField(required=True)
    price = forms.IntegerField(required=True)
