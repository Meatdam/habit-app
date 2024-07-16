from rest_framework import serializers


class HabitsValidatorRelated:
    """
    Проверка связяных привычек,
    связывать приятную привычку запрещено,
    Приятная привычка не может быть связана с другой привычкой
    """
    def __init__(self, field, field2):
        self.field = field
        self.field2 = field2

    def __call__(self, value):
        is_good = dict(value).get(self.field)
        related = dict(value).get(self.field2)

        if related and is_good is True:
            raise serializers.ValidationError(
                'Связывать приятную привычку запрещено')
        elif is_good and related:
            raise serializers.ValidationError(
                'Приятная привычка не может быть связана с другой привычкой')


class ValidatorPrize:
    """
    Проверка наличия награды,
    Награда не может быть установлена для приятной привычки
    """
    def __init__(self, field, field2):
        self.field = field
        self.field2 = field2

    def __call__(self, value):
        prize = dict(value).get(self.field)
        is_good = dict(value).get(self.field2)

        if prize and is_good:
            raise serializers.ValidationError(
                'Приятная привычка не может быть с вознаграждением')


class ValidatorDuration:
    """
    Проверка длительности привычки,
    Длительность выполнения не может быть больше двух минут
    """
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        duration = dict(value).get(self.field)

        if duration is not None:
            if duration > 2:
                raise serializers.ValidationError(
                    'Время выполнения не может быть больше двух минут')


class ValidatorRelated:
    """
    Проверка связи привычек с наградой,
    Связанная привычка не может быть с вознаграждением
    """
    def __init__(self, field, field2):
        self.field = field
        self.field2 = field2

    def __call__(self, value):
        related = dict(value).get(self.field)
        prize = dict(value).get(self.field2)

        if related and prize:
            raise serializers.ValidationError(
                'Связанная привычка не может быть с вознаграждением')
