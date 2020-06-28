# Generated by Django 2.2.13 on 2020-06-27 17:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu_type', models.CharField(max_length=200)),
                ('gradeAchieved', models.CharField(choices=[('A*', 'A*'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('Distinction', 'Distinction'), ('Merit', 'Merit'), ('Pass', 'Pass'), ('First Class', 'First Class'), ('2:1', '2:1'), ('2:2', '2:2')], max_length=100)),
                ('subject', models.TextField()),
                ('extraInfo', models.TextField()),
                ('dateAchieved', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]