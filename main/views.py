from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.views import APIView, status
from .serializers import *
from .models import *
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "add_actor":
            return ActorSerializer
        return self.serializer_class

    @action(detail=True, methods=['get'])
    def actors(self, request, pk):
        movie = get_object_or_404(Movie, id=pk)
        actors = movie.actors.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='add-actor')
    def add_actor(self, request, pk):
        movie = get_object_or_404(Movie, id=pk)
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            actor = serializer.instance
            movie.actors.add(actor)
            response = {
                "success": True,
                "data": serializer.data
            }
            return Response(response, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


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


class ReviewViewSet(MovieViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ReviewSafeSerializer
        return self.serializer_class




