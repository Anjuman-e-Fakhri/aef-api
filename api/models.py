from django.core.validators import RegexValidator
from django.db import models


class HofField(models.BooleanField):
    def pre_save(self, instance, add):
        if instance.its_id == instance.hof_its_id:
            return True
        else:
            return False


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)


class Mumin(models.Model):
    its_id = models.CharField(max_length=8)
    jamaat_id_regex = RegexValidator(
        regex=r'^[A-Z]{1}\d{3}$',
        message="Jamaat ID must be entered in the format: 'A000'.")
    jamaat_id = models.CharField(
        validators=[jamaat_id_regex],
        max_length=4)
    hof_its_id = models.CharField(max_length=8)
    is_hof = HofField('family head')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default="M")
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=2)
    postal_regex = RegexValidator(
        regex=r'^[A-Z][0-9][A-Z][0-9][A-Z][0-9]$',
        message="Phone number must be entered in the format: 'A1A1A1'.")
    postal_code = models.CharField(validators=[postal_regex], max_length=6)
    country = models.CharField(max_length=255)
    email = models.EmailField()
    email_2 = models.EmailField(blank=True)
    phone_regex = RegexValidator(
        regex=r'^\d{3}-\d{3}-\d{4}$',
        message="Phone number must be entered in the format: '905-334-4583'.")
    cell_number = models.CharField(
        validators=[phone_regex],
        max_length=12)
    res_number = models.CharField(
        validators=[phone_regex],
        max_length=12,
        blank=True)
    other_number = models.CharField(
        validators=[phone_regex],
        max_length=12,
        blank=True)
    zone = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # title
    # relation to hof
    # birthday
    # image

    class Meta:
        verbose_name_plural = "Mumineen"
        ordering = ['jamaat_id', 'its_id']

    def __str__(self):
        return "{} | {} - {} {}".format(
            self.jamaat_id,
            self.its_id,
            self.first_name,
            self.last_name)
