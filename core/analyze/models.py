from django.conf import settings
from django.db import models


class DiabetesModel(models.Model):
    CHOICE_YES_NO = (
        (1, '-بله'),
        (0, '-خیر')

    )
    CHOICE_SEX = (
        (0, '-زن'),
        (1, '-مرد')
    )

    CHOICE_EDUCATION = (
        (1, '-بی سواد'),
        (2, '-سیکل'),
        (3, '-دیپلم'),
        (4, '-کارشناسی'),
        (5, '-کارشناسی ارشد'),
        (6, '-دکترا')
    )

    Diabetes_012 = models.PositiveSmallIntegerField()
    HighBP = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO, blank=False, default=-1)
    HighChol = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO, blank=False, default=-1)
    CholCheck = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO, blank=False, default=-1)
    BMI = models.PositiveSmallIntegerField()
    Smoker = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO, blank=False, default=-1)
    Stroke = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO, blank=False, default=-1)
    HeartDiseaseorAttack = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO, blank=False, default=-1)
    PhysActivity = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO, blank=False, default=-1)
    Fruits = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO, blank=False, default=-1)
    Veggies = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO, blank=False, default=-1)
    HvyAlcoholConsump = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO, blank=False, default=-1)
    AnyHealthcare = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO, blank=False, default=-1)
    NoDocbcCost = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO, blank=False, default=-1)
    GenHlth = models.PositiveSmallIntegerField()
    MentHlth = models.PositiveSmallIntegerField()
    PhysHlth = models.PositiveSmallIntegerField()
    DiffWalk = models.PositiveSmallIntegerField(choices=CHOICE_YES_NO, blank=False, default=-1)
    Sex = models.PositiveSmallIntegerField(choices=CHOICE_SEX, blank=False, default=-1)
    Age = models.PositiveSmallIntegerField()
    Education = models.PositiveSmallIntegerField(choices=CHOICE_EDUCATION, blank=False, default=-1)
    Label = models.CharField(max_length=32)
    Date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='diabetes')
    result = models.CharField(max_length=32)

    def __str__(self):
        return self.user

    def age_rate(self, age):
        if (age >= '18') and (age <= '24'):
            self.Age = 1
        elif (age >= '25') and (age <= '29'):
            self.Age = 2
        elif (age >= '30') and (age <= '34'):
            self.Age = 3
        elif (age >= '35') and (age <= '39'):
            self.Age = 4
        elif (age >= '40') and (age <= '44'):
            self.Age = 5
        elif (age >= '45') and (age <= '49'):
            self.Age = 6
        elif (age >= '50') and (age <= '54'):
            self.Age = 7
        elif (age >= '55') and (age <= '59'):
            self.Age = 8
        elif (age >= '60') and (age <= '64'):
            self.Age = 9
        elif (age >= '65') and (age <= '69'):
            self.Age = 10
        elif (age >= '70') and (age <= '74'):
            self.Age = 11
        elif (age >= '75') and (age <= '79'):
            self.Age = 12
        elif age >= '80':
            self.Age = 13
