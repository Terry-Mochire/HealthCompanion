from django import forms


class LocationForm(forms.Form):
    country = forms.CharField(max_length=100)
    county = forms.CharField(max_length=100)
    sub_county = forms.CharField(max_length=100)

    class Meta:
        fields = ['countries', 'counties', 'sub_counties']

