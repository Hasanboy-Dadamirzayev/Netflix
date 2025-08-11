from rest_framework.response import Response
from rest_framework.views import APIView, status
from .serializers import *
from .models import *
from rest_framework.generics import get_object_or_404

class ActorsAPIView(APIView):
    def get(self, request):
        actors = Actors.objects.all()
        serializer = ActorSerializer(actors, many=True)
        response = {
            'successfully': True,
            'data': serializer.data
        }
        return Response(response, status=200)

    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            Actors.objects.create(
                name = serializer.data['name'],
                country = serializer.data['country'],
                gender = serializer.data['gender'],
                birthdate = serializer.data['birthdate']
            )
            response = {
                'successfully': True,
                'message': 'Actors created successfully',
                'data': serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActorRetrieveUpdateAPIView(APIView):
    def get(self, request, pk):
        actor = get_object_or_404(Actors, id=pk)
        serializer = ActorSerializer(actor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        actor = get_object_or_404(Actors, id=pk)
        serializer = ActorSerializer(actor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                "successfully": True,
                "message": "Actor update successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=400)


    def delete(self, request, pk):
        actor = get_object_or_404(Actors, id=pk)
        actor.delete()
        response = {
            "message": "delete"
        }
        return Response(response)


class MoviesAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        response = {
            "message": "Successfully",
            "data": serializer.data
        }
        return Response(response)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "Message": "Successfully",
                "data": serializer.data
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieRetrieveUpdateAPIView(APIView):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, id=pk)
        serializer = MovieSerializer(movie)
        response = {
            "message": "Successfully",
            "data": serializer.data
        }
        return Response(response)

    def put(self, request, pk):
        movie = get_object_or_404(Movie, id=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

    def delete(self, request, pk):
        movie = get_object_or_404(Movie, id=pk)
        movie.delete()
        response = {
            "message": "Movie deleted successfully"
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)

class SubscriptionAPIView(APIView):
    def get(self, request):
        subscription = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscription, many=True)
        response = {
            "message": "Successfully",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubscriptionRetrieveUpdateAPIView(APIView):
    def get(self, request, pk):
        subscription = get_object_or_404(Subscription, id=pk)
        serializer = SubscriptionSerializer(subscription)
        response = {
            "message": "Successfully",
            "data": serializer.data
        }
        return Response(response, status=status.HTTP_200_OK)

    def put(self, request, pk):
        subscription = get_object_or_404(Subscription, id=pk)
        serializer = SubscriptionSerializer(subscription, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Successfully",
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        subscription = get_object_or_404(Subscription, id=pk)
        subscription.delete()
        response = {
            "message": "Subscription deleted successfully"
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)

