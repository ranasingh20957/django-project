from django import forms
from SMS.models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'
            field.widget.attrs['placeholder']='Enter '+field.label
            


class PaymentDetialsFrom(forms.ModelForm):
    class Meta:
        model=paymentDetials
        fields='__all__'
