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

TITLE_CHOICES = (
    ('Shaikh', 'Shaikh'),
    ('Mulla', 'Mulla'),
    ('Bhai', 'Bhai'),
    ('Bhen', 'Bhen')
)

RELATIONSHIP_CHOICES = (
    ('Self', 'Self'),
    ('Husband', 'Husband'),
    ('Wife', 'Wife'),
    ('Son', 'Son'),
    ('Daughter', 'Daughter'),
    ('Father', 'Father'),
    ('Mother', 'Mother'),
    ('Grand Father', 'Grand Father'),
    ('Grand Mother', 'Grand Mother'),
    ('Grand Daughter', 'Grand Daughter'),
    ('Grand Son', 'Grand Son'),
    ('Son-in-law', 'Son-in-law'),
    ('Daughter-in-law', 'Daughter-in-law'),
    ('Father-in-law', 'Father-in-law'),
    ('Mother-in-law', 'Mother-in-law'),
    ('Brother', 'Brother'),
    ('Sister', 'Sister'),
    ('Uncle', 'Uncle'),
    ('Aunt', 'Aunt'),
    ('Cousin', 'Cousin'),
    ('Niece', 'Niece'),
    ('Nephew', 'Nephew')
)

class Mumin(models.Model):
    its_id = models.CharField(max_length=8)
    jamaat_id_regex = RegexValidator(
        regex=r'^[A-Z]{1}\d{3}$',
        message="Jamaat ID not entered in the format: 'A000'."
        )
    jamaat_id = models.CharField(
        validators=[jamaat_id_regex],
        max_length=4,
        help_text="Jamaat ID must be entered in the format: 'A000'.")
    hof_its_id = models.CharField(max_length=8)
    is_hof = HofField('family head')
    title = models.CharField(
        max_length=10,
        choices=TITLE_CHOICES,
        blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default="M")
    relationship_to_hof = models.CharField(
        "Relation to Head of Family",
        max_length=30,
        choices=RELATIONSHIP_CHOICES,
        blank=True)
    birthday = models.DateField(
        blank=True,
        null=True,
        help_text="Birthday must be entered in the format: 'yyyy-mm-dd'.")
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=2)
    postal_regex = RegexValidator(
        regex=r'^[A-Z][0-9][A-Z][0-9][A-Z][0-9]$',
        message="Postal Code not entered in the format: 'A1A1A1'."
        )
    postal_code = models.CharField(
        validators=[postal_regex],
        max_length=6,
        help_text="Postal Code must be entered in the format: 'A1A1A1'.")
    country = models.CharField(max_length=255)
    email = models.EmailField()
    email_2 = models.EmailField(blank=True)
    phone_regex = RegexValidator(
        regex=r'^\d{3}-\d{3}-\d{4}$',
        message="Phone number not entered in the format: '###-###-###'.")
    cell_number = models.CharField(
        validators=[phone_regex],
        max_length=12,
        help_text="Phone number must be entered in the format: '###-###-###'.")
    res_number = models.CharField(
        validators=[phone_regex],
        max_length=12,
        blank=True,
        help_text="Phone number must be entered in the format: '###-###-###'.")
    other_number = models.CharField(
        validators=[phone_regex],
        max_length=12,
        blank=True,
        help_text="Phone number must be entered in the format: '###-###-###'.")
    zone = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

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
