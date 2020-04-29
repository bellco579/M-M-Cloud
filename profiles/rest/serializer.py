from rest_framework import serializers

from debts.models import Debt
from profiles.models import UserProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("uid",)
