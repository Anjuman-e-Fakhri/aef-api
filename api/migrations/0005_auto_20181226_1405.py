# Generated by Django 2.1.4 on 2018-12-26 19:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20181226_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mumin',
            name='birthday',
            field=models.DateField(blank=True, help_text="Birthday must be entered in the format: 'yyyy-mm-dd'.", null=True),
        ),
        migrations.AlterField(
            model_name='mumin',
            name='cell_number',
            field=models.CharField(help_text="Phone number must be entered in the format: '###-###-###'.", max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number not entered in the format: '###-###-###'.", regex='^\\d{3}-\\d{3}-\\d{4}$')]),
        ),
        migrations.AlterField(
            model_name='mumin',
            name='other_number',
            field=models.CharField(blank=True, help_text="Phone number must be entered in the format: '###-###-###'.", max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number not entered in the format: '###-###-###'.", regex='^\\d{3}-\\d{3}-\\d{4}$')]),
        ),
        migrations.AlterField(
            model_name='mumin',
            name='res_number',
            field=models.CharField(blank=True, help_text="Phone number must be entered in the format: '###-###-###'.", max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number not entered in the format: '###-###-###'.", regex='^\\d{3}-\\d{3}-\\d{4}$')]),
        ),
        migrations.AlterField(
            model_name='mumin',
            name='zone',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
