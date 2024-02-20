from users import models as UsersModels
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status

def object_is_exist(pk, model, exception="object not found"):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        return Response({'message' : f'{exception}'}, status=status.HTTP_404_NOT_FOUND)

def object_is_exist_for_sockets(pk, model, error_method, exception="object not found"):
    try:
        return model.objects.get(pk=pk)
    except:
        error_method(exception)


User = get_user_model()

def emailAlreadyExist(email):
    return User.objects.filter(email=email).exists()

def token_is_exist(token):
    return UsersModels.VerifyToken.objects.filter(token=token).exists()

def check_permission(permission_name, request):
    for group in request.user.groups.all():
        if group.permissions.filter(codename = permission_name):
            return True
    return False