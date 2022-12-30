from django import forms

from analyze.models import DiabetesModel
from lib.validators import bmi_validate, general_health_validate, mental_physical_health_validate, age_validate


class DiabetesForm(forms.ModelForm):
    BMI = forms.IntegerField(validators=[bmi_validate])
    GenHlth = forms.IntegerField(validators=[general_health_validate])
    MenHlth = forms.IntegerField(validators=[mental_physical_health_validate])
    PhysHlth = forms.IntegerField(validators=[mental_physical_health_validate])
    Age = forms.IntegerField(validators=[age_validate])
    class Meta:
        model = DiabetesModel
        exclude = ('Diabetes_012', 'Label', 'Date', 'user', 'result')
        widgets = {
            'HighBP': forms.RadioSelect(attrs={'class': "border-0 opacity-0 ms-4"}),
            'HighChol': forms.RadioSelect(attrs={'class': "border-0 opacity-0 ms-4"}),
            'CholCheck': forms.RadioSelect(attrs={'class': "border-0 opacity-0 ms-4"}),
            'Smoker': forms.RadioSelect(attrs={'class': "border-0 opacity-0 ms-4"}),
            'Stroke': forms.RadioSelect(attrs={'class': "border-0 opacity-0 ms-4"}),
            'HeartDiseaseorAttack': forms.RadioSelect(attrs={'class': "border-0 opacity-0 ms-4"}),
            'PhysActivity': forms.RadioSelect(attrs={'class': "border-0 opacity-0 ms-4"}),
            'Fruits': forms.RadioSelect(attrs={'class': "border-0 opacity-0 ms-4"}),
            'Veggies': forms.RadioSelect(attrs={'class': "border-0 opacity-0 ms-4"}),
            'HvyAlcoholConsump': forms.RadioSelect(attrs={'class': "border-0 opacity-0 ms-4"}),
            'AnyHealthcare': forms.RadioSelect(attrs={'class': "border-0 opacity-0 ms-4"}),
            'NoDocbcCost': forms.RadioSelect(attrs={'class': "border-0 opacity-0 ms-4"}),
            'DiffWalk': forms.RadioSelect(attrs={'class': "border-0 opacity-0 ms-4"}),
            'Sex': forms.RadioSelect(attrs={'class': "border-0 opacity-0 ms-4"}),
            'Education': forms.RadioSelect(attrs={'class': "border-0 opacity-0 ms-4"})
        }




