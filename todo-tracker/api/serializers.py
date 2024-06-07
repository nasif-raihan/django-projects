from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

    @staticmethod
    def validate_title(value: str) -> str:
        if 5 > len(value) or len(value) > 100:
            raise serializers.ValidationError(
                "Todo task name must be within length of 5 to 100"
            )
        return value