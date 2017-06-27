from django.conf.urls import url

from fitness.views import home, WorkoutList, WorkoutSingle


urlpatterns = (
    url('^workouts$', WorkoutList.as_view(), name='workout-list'),
    url('^workout/(?P<workout_id>\d+)$', WorkoutSingle.as_view(), name='workout-single'),
    url('^$', home, name='home'),
)


# ('abc')
# ('abc', )