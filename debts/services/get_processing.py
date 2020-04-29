from django.db.models import Q

from debts.models import Debt
from debts.rest.serializer import DebtSerializer
from profiles.models import UserProfile


def get_by_uid(uid):
    try:
        up = UserProfile.objects.get(pk=uid)
        debts = Debt.objects.filter(Q(receiver=up) | Q(sender=up))
        return DebtSerializer(debts, many=True).data
    except:
        return "error"
