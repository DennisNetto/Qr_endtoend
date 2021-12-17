from django import forms


class CreateNewEntry(forms.Form):
    id_number = forms.CharField(label='ID', max_length=26)
    First_name = forms.CharField(max_length=22)
    Last_name = forms.CharField(max_length=22)
    DOB = forms.CharField(max_length=10)


class CreateNewQR(forms.Form):
    id_number = forms.CharField(label='ID', max_length=26)
    First_name = forms.CharField(max_length=22)
    Last_name = forms.CharField(max_length=22)
    DOB = forms.CharField(max_length=10)


