# Generated by Django 3.2.7 on 2021-10-10 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recorddb', '0012_auto_20211009_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]
