from django import forms


class LIC624Form(forms.Form):
    date_occured_1 = forms.DateField(label='Date of Incident:')
    describe_incident = forms.CharField(label='Describe the Incident/Event:')
    unauthorized_absence = forms.BooleanField(required=False)
    aa_self = forms.BooleanField(required=False)
