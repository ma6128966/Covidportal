# Generated by Django 2.2.10 on 2020-07-25 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0002_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='hospital_addr',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]