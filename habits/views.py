
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from habits.models import Habits
from habits.paginators import Paginator
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitsCreateAPIView(generics.CreateAPIView):
    """
    API для создания новой привычки
    """
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitsListAPIView(generics.ListAPIView):
    """
    API для получения списка привычек
    """
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, )
    pagination_class = Paginator

    def get_queryset(self):
        """
        Получаем список привычек текущего пользователя
        """
        queryset = self.queryset.filter(owner=self.request.user)
        return queryset


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    """
    API для получения одной привычки
    """
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class HabitsUpdateAPIView(generics.UpdateAPIView):
    """
    API для изменения привычки
    """
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class HabitsDestroyAPIView(generics.DestroyAPIView):
    """
    API для удаления привычки
    """
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class HabitsPublicListAPIView(generics.ListAPIView):
    """
    API для получения списка публичных привычек
    """
    serializer_class = HabitSerializer
    queryset = Habits.objects.filter(is_public=True)
    permission_classes = (AllowAny, )
    pagination_class = Paginator
