from debts.models import Debt
from profiles.models import UserProfile


def create_debt(sender_uid, receiver_uid, count, timestamp, is_confirm=0, last_update_timestamp=0, ):
    sender = UserProfile.objects.get_or_create(uid=sender_uid)[0]
    receiver = UserProfile.objects.get_or_create(uid=receiver_uid)[0]
    try:
        debt = Debt.objects.get(pk=timestamp)
        if debt.last_update_timestamp < last_update_timestamp:
            debt.last_update_timestamp = last_update_timestamp
            debt.is_confirm = bool(is_confirm)
            debt.save()
    except:
        Debt.objects.create(sender=sender, receiver=receiver, count=count, is_confirm=False, timestamp=timestamp)
