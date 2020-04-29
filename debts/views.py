from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from debts.rest.serializer import DebtSerializer
from debts.services.get_processing import get_by_uid
from debts.services.post_processing import create_debt


class DebtView(APIView):
    permission_classes = []
    allowed_methods = ('GET', 'POST', 'DELETE')

    def get(self, request):
        data = get_by_uid(uid=request.GET.get("uid"), request=request)
        return Response(data)

    def post(self, request):
        new_debt = create_debt(
            sender_uid=request.POST.get("sender_uid"),
            receiver_uid=request.POST.get("receiver_uid"),
            count=request.POST.get("count"),
        )

        return Response("new_debt")
