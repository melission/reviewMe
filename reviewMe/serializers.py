from rest_framework import serializers
from books.models import *
from movies.models import *
from reviews.models import ReviewBook


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


class ContributionSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = BookContributor
        fields = ['book', 'role']


class ContributorSerializer(serializers.ModelSerializer):
    bookcontributor_set = ContributionSerializer(read_only=True, many=True)
    number_contributions = serializers.ReadOnlyField()

    class Meta:
        model = Contributor
        fields = ['first_name', 'last_name', 'bookcontributor_set', 'number_contributions']


class ReviewBookSerializer(serializers.ModelSerializer):


    class Meta:
        model = ReviewBook
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

