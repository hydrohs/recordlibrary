# Generated by Django 3.2.7 on 2021-10-09 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recorddb', '0005_alter_record_condition'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
