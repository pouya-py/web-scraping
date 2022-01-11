from django import forms
import jdatetime
print(jdatetime.datetime.now().year)

class input_form(forms.Form):
    room = forms.IntegerField(min_value=0, max_value=5, required=True, label='تعداد اتاق‌ها')
    space = forms.IntegerField(required=True, label='متراژ خانه')
    year_of_construction = forms.IntegerField(required=True, label='سال ساخت')
    
    def clean_room(self):
        cleaned_data = self.cleaned_data
        rooms = cleaned_data['room']
        if rooms not in [1,2,3,4,5]:
            raise forms.ValidationError('تعداد اتاق درست نیست.')
        return cleaned_data

    def clean_space(self):

        cleaned_data = self.cleaned_data
        space = self.cleaned_data['space']  
        if space not in range(30,3000):
            raise forms.ValidationError('لطفاً متراژ خانه را درست وارد کنید.')
        return cleaned_data

    def clean_year_of_construction(self):
        cleaned_data = self.cleaned_data
        year_of_construction = self.cleaned_data['year_of_construction']
        if year_of_construction not in range(1300,int(jdatetime.datetime.now().year)):
            raise forms.ValidationError('سال ساخت را اشتباه وارد کرده‌اید.')
        return cleaned_data
