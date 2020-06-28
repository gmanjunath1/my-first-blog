from django.conf import settings
from django.db import models
from django.utils import timezone

#models.Model means that Post is a django model and should be stored in the database
class skillSummary(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.text


class Education(models.Model):
    grade_choices = (
        ('A*', 'A*'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('Distinction', 'Distinction'),
        ('Merit', 'Merit'),
        ('Pass', 'Pass'),
        ('First Class', 'First Class'),
        ('2:1', '2:1'),
        ('2:2', '2:2'),
        ('Current Studies', 'Current Studies'),
    )
    edu_choices = (
        ('GCSE', 'GSCE'),
        ('A-Level', 'A-Level'),
        ('AS-Level', 'AS-Level'),
        ('BTEC', 'BTEC'),
        ('Degree', 'Degree'),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    edu_type = models.CharField(max_length=100, choices=edu_choices)
    subject = models.CharField(max_length=200)
    gradeAchieved = models.CharField(max_length=100, choices=grade_choices)
    dateAchieved = models.DateField()
    extraInfo = models.TextField(null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.edu_type + " - " + self.subject


class WorkExperience(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    companyName = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    startDate = models.DateField()
    extraInfo = models.TextField(null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.companyName + " - " + self.startDate.strftime("%d/%m/%Y")



class AchieveAccomplish(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titleAch = models.CharField(max_length=100)
    dateAchieved = models.DateField()
    description = models.TextField(null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.titleAch + " - " + self.dateAchieved.strftime("%d/%m/%Y")


class memberships(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    membershipName = models.CharField(max_length=100)
    dateMembership = models.DateField()
    description = models.TextField(null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.membershipName

class Projects(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    projectName = models.CharField(max_length=100)
    projectDate = models.DateField()
    description = models.TextField(null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.projectName