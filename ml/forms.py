from django import forms
from django.core.exceptions import ValidationError
import jdatetime

class input_form(forms.Form):
    # form to display to get user input in a view.
    room = forms.IntegerField(min_value=0, max_value=5, required=True, label='تعداد اتاق‌ها')
    space = forms.IntegerField(required=True, label='متراژ خانه')
    year_of_construction = forms.IntegerField(required=True, label='سال ساخت')
    
    # removing ':' from forms.  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
    # form validation for room
    def clean_room(self):
        rooms = self.cleaned_data['room']
        if rooms not in [1,2,3,4,5]:
            raise ValidationError('.تعداد اتاق درست نیست')
        return rooms
    # form validation for space
    def clean_space(self):

        space = self.cleaned_data['space']
        if space not in range(30,3000):
            raise ValidationError('.لطفاً متراژ خانه را درست وارد کنید')
        return space
    # form validation for year_of_construction
    def clean_year_of_construction(self):
        year_of_construction = self.cleaned_data['year_of_construction']
        if year_of_construction not in range(1300,int(jdatetime.datetime.now().year)):
            raise ValidationError('.سال ساخت را اشتباه وارد کرده‌اید')
        return year_of_construction
