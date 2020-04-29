from rest_framework import serializers

from debts.models import Debt


class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ("sender", "receiver", "count", "is_confirm")
