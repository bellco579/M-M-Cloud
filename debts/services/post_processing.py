from debts.models import Debt
from profiles.models import UserProfile


def create_debt(sender_uid, receiver_uid, count):
    sender = UserProfile.objects.get_or_create(uid=sender_uid)[0]
    receiver = UserProfile.objects.get_or_create(uid=receiver_uid)[0]
    Debt.objects.create(sender=sender, receiver=receiver, count=count, is_confirm=False)
