# Generated by Django 2.2.13 on 2020-06-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='subject',
            field=models.CharField(choices=[('GCSE', 'GSCE'), ('A-Level', 'A-Level'), ('AS-Level', 'AS'), ('BTEC', 'BTEC'), ('Degree', 'Degree')], max_length=100),
        ),
    ]
