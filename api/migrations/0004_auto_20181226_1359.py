# Generated by Django 2.1.4 on 2018-12-26 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20181226_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mumin',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
