from django.db import models

class ContactForm(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    address = models.TextField()
    notice_period = models.IntegerField()
    current_ctc = models.FloatField()
    expected_ctc = models.FloatField()
    experience = models.FloatField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name
