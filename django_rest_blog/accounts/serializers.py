from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model, authenticate

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    #password = serializers.CharField(write_only=True)
    email = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = get_user_model()
        fields = ('name', 'email', 'password')

    def create(self, validated_data):

        user = get_user_model().objects.create(
            name=validated_data['name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg)

        attrs['user'] = user
        return attrs

