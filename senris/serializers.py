from pyexpat import model
from xml.dom.minidom import Entity
from attr import field, fields
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from sqlalchemy.sql.functions import mode
from .models import Incident, Damage, SensitiveEntity
from drf_extra_fields.fields import Base64ImageField
from django.contrib.auth import authenticate



class DamageSerializer(serializers.ModelSerializer):

    class Meta:
        model=Damage
        fields="__all__"


class SensitiveEntitySerializer(serializers.ModelSerializer):

    class Meta:
        model=SensitiveEntity
        fields="__all__"


class IncidentSerializer(GeoFeatureModelSerializer):
    image1 = Base64ImageField(max_length=None, use_url=True)
    image2 = Base64ImageField(max_length=None, use_url=True)
    image3 = Base64ImageField(max_length=None, use_url=True)
    image4 = Base64ImageField(max_length=None, use_url=True)


    # damage = serializers.CharField(source='damage.name', read_only=True)
    # entity = SensitiveEntitySerializer()

    class Meta:
        model=Incident
        geo_field="location"
        fields="__all__"
        #fields=('id', 'gnd_dsd', 'damage', 'entity', 'siviarity', 'location_ref', 'note', 'image1', 'image2', 'image3', 'image4', 'collected_location',)
        


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        None,
                                        validated_data['password'])
        return user

    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")
