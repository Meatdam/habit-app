from rest_framework import serializers

from habits.models import Habits
from habits.validators import HabitsValidatorRelated, ValidatorPrize, ValidatorDuration, ValidatorRelated


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Habits
    """
    class Meta:
        model = Habits
        fields = '__all__'
        validators = [HabitsValidatorRelated(field='is_good', field2='related'),
                      ValidatorPrize(field='prize', field2='is_good'), ValidatorDuration(field='duration'),
                      ValidatorRelated(field='related', field2='prize')]
