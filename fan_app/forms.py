from django import forms

class FanControlForm(forms.Form):
    STATUS_CHOICES = [
        (1, 'On'),
        (0, 'Off')
    ]
    SPEED_CHOICES = [(i, i) for i in range(1, 6)]

    status = forms.ChoiceField(choices=STATUS_CHOICES)
    speed_level = forms.ChoiceField(choices=SPEED_CHOICES)

class ConsumptionQueryForm(forms.Form):
    start_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    end_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
