from rest_framework import serializers

from rest_framework.validators import UniqueValidator

from .models import Genre, Book

class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance: Genre, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    pages = serializers.IntegerField(default=100, min_value=1)
    published_year = serializers.IntegerField(default=2020)
    genre = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), required=False, allow_null=True
    )

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance: Book, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.author = validated_data.get("author", instance.author)
        instance.pages = validated_data.get("pages", instance.pages)
        instance.published_year = validated_data.get("published_year", instance.published_year)
        instance.genre = validated_data.get("genre", instance.genre)
        instance.save()
        return instance
