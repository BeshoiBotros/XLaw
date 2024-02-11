from django.shortcuts import render
from . import models
from . import serializers
from rest_framework.views import APIView
from XLaw import shortcuts
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from . import filters

class CategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):

        if pk:
            instance = shortcuts.object_is_exist(pk, models.Category, "Category not found")
            serializer = serializers.CategorySerializer(instance=instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        queryset = models.Category.objects.all()
        
        filterset = filters.CategoryFilters(request.GET, queryset=queryset)
        
        if filterset.is_valid():
            queryset = filterset.qs
        
        serializer = serializers.CategorySerializer(queryset, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        
        can_add_category = shortcuts.check_permission('add_category', request)
        
        if can_add_category:
            serializer = serializers.CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'message' : 'you can not perform this action.'}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        
        can_update_category = shortcuts.check_permission('change_category', request)
        
        instance = shortcuts.object_is_exist(pk, models.Category, 'Category not found')
        
        if can_update_category:
            serializer = serializers.CategorySerializer(instance=instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({'message' : 'you can not perform this action.'}, status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, pk):
        
        can_delete_category = shortcuts.check_permission('delete_category', request)
        
        instance = shortcuts.object_is_exist(pk, models.Category, "Category not found")

        if can_delete_category:    
            instance.delete()
            return Response({'message' : 'the category has been deleted successfully.'}, status=status.HTTP_200_OK)
        
        return Response({'message' : 'you can not perform this action.'}, status=status.HTTP_400_BAD_REQUEST)


class NewView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        
        if pk:
            instance = shortcuts.object_is_exist(pk, models.New, "New not found")
            serializer = serializers.NewSerializer(instance=instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        queryset = models.New.objects.all()
        
        filterset = filters.CategoryFilters(request.GET, queryset=queryset)
        
        if filterset.is_valid():
            queryset = filterset.qs

        serializer = serializers.NewSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        
        can_add_new = shortcuts.check_permission('add_new', request)
        
        if can_add_new:
            serializer = serializers.NewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'message' : 'you can not perform this action.'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        
        can_update_new = shortcuts.check_permission('change_new', request)
        
        instance = shortcuts.object_is_exist(pk, models.New, 'New not found')
        
        if can_update_new:
            serializer = serializers.NewSerializer(instance=instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({'message' : 'you can not perform this action.'}, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        
        can_delete_new = shortcuts.check_permission('delete_new', request)
        
        if can_delete_new:
            instance = shortcuts.object_is_exist(pk, models.New, "New not found")
            if instance.user.pk is not request.user.pk:
                return Response({'message' : 'you can only delete your news.'})
            instance.delete()
            return Response({'message' : 'the New has been deleted successfully.'}, status=status.HTTP_200_OK)
        
        return Response({'message' : 'you can not perform this action.'}, status=status.HTTP_400_BAD_REQUEST)

class CaseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        
        if pk:
            instance = shortcuts.object_is_exist(pk, models.Case, "Case not found")
            serializer = serializers.CaseSerializer(instance=instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        queryset = models.Case.objects.all()
        
        filterset = filters.CategoryFilters(request.GET, queryset=queryset)
        
        if filterset.is_valid():
            queryset = filterset.qs
            
        serializer = serializers.CaseSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):

        can_add_case = shortcuts.check_permission('add_case', request)
        
        if can_add_case:
            serializer_data = request.data.copy()
            serializer_data['user'] = request.user.pk
            serializer = serializers.CaseSerializer(data=serializer_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({'message' : 'you can not perform this action.'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):

        can_update_case = shortcuts.check_permission('change_case', request)
        
        instance = shortcuts.object_is_exist(pk, models.Case, 'Case not found')
        
        if instance.user.pk != request.user.pk:
            return Response({'message' : 'you can only update your cases.'})
        if can_update_case:
            serializer = serializers.CaseSerializer(instance=instance, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({'message' : 'you can not perform this action.'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        can_delete_case = shortcuts.check_permission('delete_case', request)
        
        if can_delete_case:
            instance = shortcuts.object_is_exist(pk, models.Case, "Case not found")
            if instance.user.pk is not request.user.pk:
                return Response({'message' : 'you can only delete your cases.'})
            instance.delete()
            return Response({'message' : 'the Case has been deleted successfully.'}, status=status.HTTP_200_OK)
        
        return Response({'message' : 'you can not perform this action.'}, status=status.HTTP_400_BAD_REQUEST)

