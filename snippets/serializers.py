from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, User, Map, LocationInfo
from django.contrib.auth.models import User

class SnippetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance


# class UserAuthSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'snippets')


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, allow_blank=True, max_length=100)
    password = serializers.CharField(required=False, allow_blank=True, max_length=100)
    email = serializers.CharField(required=False, allow_blank=True, max_length=100)

    class Meta:
        model = User
        fields = ('id','username', 'password','email')

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.title)
        instance.password = validated_data.get('password', instance.code)
        instance.email = validated_data.get('email', instance.linenos)
        instance.save()
        return instance

    # owner = serializers.ReadOnlyField(source='owner.username')


class MapSerializer(serializers.ModelSerializer):

    lat = serializers.CharField(required=True, allow_blank=True, max_length=100)
    lon = serializers.CharField(required=True, allow_blank=True, max_length=100)
    addr = serializers.CharField(required=True, allow_blank=True, max_length=100)
    amenity = serializers.CharField(required=True, allow_blank=True, max_length=100)
    cuisine = serializers.CharField(required=True, allow_blank=True, max_length=100)
    name = serializers.CharField(required=True, allow_blank=True, max_length=100)
    opening_hours = serializers.CharField(required=True, allow_blank=True, max_length=100)
    website = serializers.CharField(required=True, allow_blank=True, max_length=100)


    class Meta:
        model = Map
        fields = ('id', 'lat', 'lon', 'addr', 'amenity', 'cuisine', 'name', 'opening_hours', 'website')

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        return Map.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.lat = validated_data.get('lat', instance.lat)
        instance.lon = validated_data.get('lon', instance.lon)
        instance.addr = validated_data.get('addr', instance.addr)
        instance.amenity = validated_data.get('amenity', instance.amenity)
        instance.cuisine = validated_data.get('cuisine', instance.cuisine)
        instance.name = validated_data.get('name', instance.name)
        instance.opening_hours = validated_data.get('opening_hours', instance.opening_hours)
        instance.website = validated_data.get('website', instance.website)
        instance.save()
        return instance

