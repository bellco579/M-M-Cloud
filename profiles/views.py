from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles.models import UserProfile
from profiles.rest.serializer import ProfileSerializer


class ProfileView(APIView):
    permission_classes = []
    allowed_methods = ('GET', 'POST', 'DELETE')

    def get(self, request):
        data = ProfileSerializer(UserProfile.objects.all(), many=True).data
        return Response(data)

    def post(self, request):
        user = UserProfile.objects.get_or_create(
            uid=request.POST.get("uid"),
        )[0]
        data = ProfileSerializer(user).data
        return Response(data)
