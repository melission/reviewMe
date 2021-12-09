from rest_framework import serializers
from books.models import *


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'
    # id = serializers.IntegerField()
    # name = serializers.CharField()
    # website = serializers.URLField()


class BookSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        # fields = '__all__'
        exclude = ('cover',)

    # id = serializers.IntegerField()
    # title = serializers.CharField()
    # isbn = serializers.CharField()
    # published_at = serializers.DateTimeField()
    # description = serializers.CharField()
