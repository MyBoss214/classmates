from django.db import models

# Create your models here.
# Raw code for copy paste

class Classmate(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    address = models.CharField(max_length=200, default='')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='0')
    age = models.IntegerField()

    def __str__(self):
        return self.firstname

    def get_absolute_url(self):
        return reverse('classmate_edit', kwargs={'pk': self.pk})

