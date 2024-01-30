from users import models as UsersModels
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model

    
def object_is_exist(pk, model, exception="object not found"):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise ValidationError({'message' : f'{exception}'})
    

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