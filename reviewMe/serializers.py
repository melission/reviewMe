from rest_framework import serializers


class PublisherSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    website = serializers.URLField()


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    publisher = PublisherSerializer()
    isbn = serializers.CharField()
    published_at = serializers.DateTimeField()
    description = serializers.CharField()
