from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Вью для собак


class DogList(APIView):
    """
    get:
    Возвращает список всех собак.

    post:
    Создает новую запись о собаке.
    """

    @swagger_auto_schema(
        operation_description="Получить список всех собак",
        responses={200: DogSerializer(many=True)}
    )
    def get(self, request) -> Response:
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Создать новую собаку",
        request_body=DogSerializer,
        responses={201: DogSerializer}
    )
    def post(self, request) -> Response:
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogDetail(APIView):
    """
    get:
    Получить информацию о конкретной собаке по ID.

    put:
    Обновить информацию о собаке по ID.

    delete:
    Удалить запись о собаке по ID.
    """

    @swagger_auto_schema(
        operation_description="Получить собаку по ID",
        responses={200: DogSerializer}
    )
    def get(self, request, id) -> Response:
        dog = get_object_or_404(Dog, id=id)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Обновить собаку по ID",
        request_body=DogSerializer,
        responses={200: DogSerializer}
    )
    def put(self, request, id) -> Response:
        dog = get_object_or_404(Dog, id=id)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Удалить собаку по ID",
        responses={204: 'Собака успешно удалена'}
    )
    def delete(self, request, id) -> Response:
        dog = get_object_or_404(Dog, id=id)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Вью для пород
class BreedList(APIView):
    """
    get:
    Возвращает список всех пород.

    post:
    Создает новую запись о породе.
    """

    @swagger_auto_schema(
        operation_description="Получить список всех пород",
        responses={200: BreedSerializer(many=True)}
    )
    def get(self, request) -> Response:
        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Создать новую породу",
        request_body=BreedSerializer,
        responses={201: BreedSerializer}
    )
    def post(self, request) -> Response:
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BreedDetail(APIView):
    """
    get:
    Получить информацию о конкретной породе по ID.

    put:
    Обновить информацию о породе по ID.

    delete:
    Удалить запись о породе по ID.
    """

    @swagger_auto_schema(
        operation_description="Получить породу по ID",
        responses={200: BreedSerializer}
    )
    def get(self, request, id) -> Response:
        breed = get_object_or_404(Breed, id=id)
        serializer = BreedSerializer(breed)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Обновить породу по ID",
        request_body=BreedSerializer,
        responses={200: BreedSerializer}
    )
    def put(self, request, id) -> Response:
        breed = get_object_or_404(Breed, id=id)
        serializer = BreedSerializer(breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Удалить породу по ID",
        responses={204: 'Порода успешно удалена'}
    )
    def delete(self, request, id) -> Response:
        breed = get_object_or_404(Breed, id=id)
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
