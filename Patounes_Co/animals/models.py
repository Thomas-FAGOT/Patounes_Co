from django.db import models

# Create your models here.

class Animals(models.Model):
    SEXE = (
        ('M', 'Male'),
        ('F', 'Femelle')
    )

    def positive_age_validator(value):
        if value < 0:
            raise ValidationError("L'âge ne peut pas être négatif")
    
    def positive_taille_validator(value):
        if value < 0:
            raise ValidationError("La taille ne peut pas être négatif")

    nom = models.CharField(max_length=20)
    race = models.CharField(max_length=100)
    sexe = models.CharField(max_length=1, choices=SEXE)
    age = models.IntegerField(validators=[positive_age_validator])
    taille = models.FloatField(validators=[positive_taille_validator])
    ville_refuge = models.CharField(max_length=250)
    incompatible = models.TextField(max_length=250)
    vaccin = models.BooleanField()
    sterelise = models.BooleanField