# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


REP_STYLE_CHOICES = (
    ('str', 'Strength'),
    ('hypertrophy', 'Hypertrophy'),
    ('power', 'Power'),
    ('endurance', 'Endurance'),
)


BODY_PART_CHOICES = (
    ('arms', 'Arms'),
    ('legs', 'Legs'),
    ('chest', 'Chest'),
    ('back', 'Back'),
    ('shoulder', 'Shoulder'),
    ('core', 'Core'),
)


MODALITY_CHOICES = (
    ('barbell', 'Barbell'),
    ('kettlebell', 'Kettlebell'),
    ('dumbbell', 'Dumbbell'),
    ('machine', 'Machine'),
    ('cable', 'Cable'),
    ('smith', 'Smith'),
    ('band', 'Band'),
    ('body-weight', 'Body Weight'),
)


class Exercise(models.Model):
    title = models.CharField(max_length=200)
    body_party = models.CharField(max_length=50, choices=BODY_PART_CHOICES, db_index=True)
    variation = models.CharField(max_length=50, null=True, blank=True)
    modality = models.CharField(max_length=50, choices=MODALITY_CHOICES, db_index=True)


class Workout(models.Model):
    date = models.DateField(default=timezone.now)
    user = models.ForeignKey(User)
    note = models.TextField()


class WorkoutSet(models.Model):
    workout = models.ForeignKey(Workout)
    exercise = models.ForeignKey(Exercise)
    reps = models.IntegerField()
    rep_style = models.CharField(max_length=50, choices=REP_STYLE_CHOICES)
    notes = models.TextField()
    intensity = models.IntegerField()
    load = models.IntegerField(help_text='Weight in pounds')
