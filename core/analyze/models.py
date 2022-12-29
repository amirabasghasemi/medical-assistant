from django.conf import settings
from django.db import models


class DiabetesModel(models.Model):
    CHOICE_YES_NO = (
        (0, 'No'),
        (1, 'Yes')
    )
    CHOICE_SEX = (
        (0, 'Female'),
        (1, 'Male')
    )

    CHOICE_EDUCATION = (
        (1, 'بی سواد'),
        (2, 'سیکل'),
        (3, 'دیپلم'),
        (4, 'کارشناسی'),
        (5, 'کارشناسی ارشد'),
        (6, 'دکترا')
    )

    Diabetes_012 = models.PositiveSmallIntegerField()
    HighBP = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO)
    HighChol = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO)
    CholCheck = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO)
    BMI = models.PositiveSmallIntegerField()
    Smoker = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO)
    Stroke = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO)
    HeartDiseaseorAttack = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO)
    PhysActivity = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO)
    Fruits = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO)
    Veggies = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO)
    HvyAlcoholConsump = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO)
    AnyHealthcare = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO)
    NoDocbcCost = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO)
    GenHlth = models.PositiveSmallIntegerField()
    MentHlth = models.PositiveSmallIntegerField()
    PhysHlth = models.PositiveSmallIntegerField()
    DiffWalk = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO)
    Sex = models.PositiveSmallIntegerField(choices=CHOICE_SEX)
    Age = models.PositiveSmallIntegerField()
    Education = models.PositiveSmallIntegerField(choices=CHOICE_EDUCATION)
    Label = models.CharField(max_length=32)
    Date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='diabetes')
    result = models.CharField(max_length=32)

    def __str__(self):
        return self.user
