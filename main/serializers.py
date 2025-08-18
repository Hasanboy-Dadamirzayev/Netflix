from itertools import count

from rest_framework import serializers
from .models import *

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    def validate_actors(self, name):
        if len(name) < 3:
            raise serializers.ValidationError(
                "Aktyorlar 3 tadan kam bolmasligi kerak"
            )
        return name


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class ReviewSafeSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    movie = serializers.CharField(source='movie.name', read_only=True)

    class Meta:
        model = Review
        fields = "__all__"

