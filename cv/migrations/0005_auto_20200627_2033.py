# Generated by Django 2.2.13 on 2020-06-27 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cv', '0004_auto_20200627_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='dateAchieved',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='education',
            name='edu_type',
            field=models.CharField(choices=[('GCSE', 'GSCE'), ('A-Level', 'A-Level'), ('AS-Level', 'AS-Level'), ('BTEC', 'BTEC'), ('Degree', 'Degree')], max_length=100),
        ),
        migrations.AlterField(
            model_name='education',
            name='extraInfo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='gradeAchieved',
            field=models.CharField(choices=[('A*', 'A*'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('Distinction', 'Distinction'), ('Merit', 'Merit'), ('Pass', 'Pass'), ('First Class', 'First Class'), ('2:1', '2:1'), ('2:2', '2:2'), ('Current Studies', 'Current Studies')], max_length=100),
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=200)),
                ('startDate', models.DateField()),
                ('extraInfo', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]