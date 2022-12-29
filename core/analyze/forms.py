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
            'HighBP': forms.RadioSelect,
            'HighChol': forms.RadioSelect,
            'CholCheck': forms.RadioSelect,
            'Smoker': forms.RadioSelect,
            'Stroke': forms.RadioSelect,
            'HeartDiseaseorAttack': forms.RadioSelect,
            'PhysActivity': forms.RadioSelect,
            'Fruits': forms.RadioSelect,
            'Veggies': forms.RadioSelect,
            'HvyAlcoholConsump': forms.RadioSelect,
            'AnyHealthcare': forms.RadioSelect,
            'NoDocbcCost': forms.RadioSelect,
            'DiffWalk': forms.RadioSelect,
            'Sex': forms.RadioSelect,
            'Education': forms.RadioSelect
        }




