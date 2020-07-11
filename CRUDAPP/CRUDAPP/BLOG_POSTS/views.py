from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentsSerializer
from .models import Students
from django.shortcuts import get_object_or_404
# Create your views here.

# GET


class StudentsView(APIView):

    def get(self, request):
        print(request.data)
        queryset = Students.objects.filter(Email=request.data.get('Email'))

        if queryset:
            if queryset.values('Password').first()['Password'] == request.data.get("Password"):
                return Response("Successfully Logged In")
            else:
                return Response("Password Incorrect")

        else:
            return Response("User not registered")

        return Response("Queried Successfully.")

    def post(self, request):
        queryset = request.data
        serializer = StudentsSerializer(data=queryset)

        if serializer.is_valid(raise_exception=True):
            save_data = serializer.save()

        return Response({"Success": "User {} created".format(save_data.name)})

    def delete(self, request, pk):
        queryset = get_object_or_404(Students.objects.all(), pk=pk)
        queryset.delete()
        return Response("User Deleted Successfully")
