from django import forms


class FilterForm(forms.Form):

    FIELD_CHOICES = (
        ('name', 'Name'),
        ('qty', 'Qty'),
        ('distance', 'Distance')
    )

    CONDITION_CHOICES = (
        ('eq', 'Equal'),
        ('gt', 'Greater Than'),
        ('lt', 'Lower Than'),
        ('icontains', 'Contains')
    )

    field = forms.ChoiceField(choices=FIELD_CHOICES, label='Select Field')
    condition = forms.ChoiceField(choices=CONDITION_CHOICES, label='Select Condition')
    user_input = forms.CharField(max_length=100, label='Your input here')

    def clean_user_input(self):
        user_input = self.cleaned_data['user_input']
        if self.cleaned_data['field'] in ['qty', 'distance']:
            try:
                int(user_input)
            except ValueError:
                raise forms.ValidationError('Qty and Distance can only handle numbers')
        return user_input