# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View

from fitness.models import Workout


def home(request):
    context = {

    }
    return render(request, 'home.html', context)


class WorkoutList(View):
    def get(self, request):
        context = {
            'workouts': Workout.objects.all(),
        }
        return render(request, 'fitness/workout_list.html', context)


class WorkoutSingle(View):
    def get(self, request, workout_id):
        context = {
            'workout': Workout.objects.get(pk=workout_id),
            # 'workout': Workout.objects.get(self.kwargs.get('workout_id')),
        }
        return render(request, 'fitness/workout_single.html', context)
