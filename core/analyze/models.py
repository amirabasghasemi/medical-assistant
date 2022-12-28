from django.conf import settings
from django.db import models


class DiabetesModel(models.Model):
    Diabetes_012 = models.PositiveSmallIntegerField()
    HighBP = models.PositiveSmallIntegerField()
    HighChol = models.PositiveSmallIntegerField()
    CholCheck = models.PositiveSmallIntegerField()
    BMI = models.PositiveSmallIntegerField()
    Smoker = models.PositiveSmallIntegerField()
    Stroke = models.PositiveSmallIntegerField()
    HeartDiseaseorAttack = models.PositiveSmallIntegerField()
    PhysActivity = models.PositiveSmallIntegerField()
    Fruits = models.PositiveSmallIntegerField()
    Veggies = models.PositiveSmallIntegerField()
    HvyAlcoholConsump = models.PositiveSmallIntegerField()
    AnyHealthcare = models.PositiveSmallIntegerField()
    NoDocbcCost = models.PositiveSmallIntegerField()
    GenHlth = models.PositiveSmallIntegerField()
    MentHlth = models.PositiveSmallIntegerField()
    PhysHlth = models.PositiveSmallIntegerField()
    DiffWalk = models.PositiveSmallIntegerField()
    Sex = models.PositiveSmallIntegerField()
    Age = models.PositiveSmallIntegerField()
    Education = models.PositiveSmallIntegerField()
    Label = models.CharField(max_length=32)
    Date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='diabetes')
    result = models.CharField(max_length=32)

    def __str__(self):
        return self.user
