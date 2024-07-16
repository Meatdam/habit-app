from django.urls import path


from habits.apps import HabitsConfig
from habits.views import HabitsListAPIView, HabitsCreateAPIView, HabitsUpdateAPIView, HabitsRetrieveAPIView, \
    HabitsDestroyAPIView, HabitsPublicListAPIView

app_name = HabitsConfig.name


urlpatterns = [
    path('habits/', HabitsListAPIView.as_view(), name='habits_list'),
    path('create/', HabitsCreateAPIView.as_view(), name='habits_create'),
    path('update/<int:pk>/', HabitsUpdateAPIView.as_view(), name='habits_update'),
    path('detail/<int:pk>/', HabitsRetrieveAPIView.as_view(), name='habits_detail'),
    path('delete/<int:pk>/', HabitsDestroyAPIView.as_view(), name='habits_delete'),
    path('public/', HabitsPublicListAPIView.as_view(), name='public_list')
]
