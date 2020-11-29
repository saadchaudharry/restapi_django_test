from  django.contrib.auth import get_user_model,authenticate
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.utils.translation import ugettext_lazy as _

from django.db.models.signals import post_save

from rest_framework import serializers

class Userserializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields=['email','password','username']

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        # password2 = self.validated_data['password2']
        # if password != password2:
        #     raise serializers.ValidationError({'password':"not valid password"})
        user.set_password(raw_password=password)
        user.save()
        return user

    @receiver(post_save, sender=User)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)


class AuthTokenSerializer(serializers.Serializer):
    email=serializers.CharField()
    passsword=serializers.CharField(
        style={"input_type":"password"},
        trim_whitespace=False
    )

    def Validate(self,attrs):
        email=attrs.get('email')
        passsword=attrs.get('passsword')
        request = self.context


        user =authenticate(
            request=self.context.get('request'),
            username=email,
            passsword=passsword
            # request=self.context.get("request"),
            # username=email,
            # password=passsword
        )
        # if not user:
        #     msg = _('Unable to authenticate with provide credential')
        #     raise serializers.ValidationError(msg,code='authentication')

        attrs['user'] = user
        print("mai yaha ghu")
        print(attrs)
        return attrs