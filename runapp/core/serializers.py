from allauth.account.adapter import get_adapter
from allauth.utils import get_username_max_length
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import User, Teams, CustomUser

from django.contrib.auth import get_user_model

try:
    from allauth.account import app_settings as allauth_settings
    from allauth.utils import (get_username_max_length)
    from allauth.account.adapter import get_adapter
    from allauth.account.utils import setup_user_email
    from allauth.socialaccount.helpers import complete_social_login
    from allauth.socialaccount.models import SocialAccount
    from allauth.socialaccount.providers.base import AuthProcess
except ImportError:
    raise ImportError("allauth needs to be added to INSTALLED_APPS.")

from rest_framework import serializers
from requests.exceptions import HTTPError

UserModel = get_user_model()
class RunnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)



    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],


        )

        return user

    class Meta:
        model = User
        # Tuple of serialized model fields (see link [2])
        fields = ( "username", "password" )

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_settings.USERNAME_MIN_LENGTH,
        required=allauth_settings.USERNAME_REQUIRED
    )

    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username


    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),

        }

class CustomRegisterSerializer(RegisterSerializer):
    runner_team = serializers.IntegerField(max_value=1000)
    runner_age = serializers.IntegerField(min_value=15, max_value=90)
    runner_category = serializers.ChoiceField(choices=CustomUser.CATEGORY)
    runner_gender = serializers.ChoiceField(choices=CustomUser.GENDER)
    zabeg22 = serializers.BooleanField()
    zabeg23 = serializers.BooleanField()

    # family = mod
    class Meta:
        model = UserModel
        fields = "__all__"

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'runner_team': self.validated_data.get('runner_team'),
            'runner_age': self.validated_data.get('runner_age'),
            'runner_category': self.validated_data.get('runner_category'),
            'runner_gender': self.validated_data.get('runner_gender'),
            'zabeg22': self.validated_data.get('zabeg22'),
            'zabeg23': self.validated_data.get('zabeg23'),
        }

        # override save method of RegisterSerializer

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.username = self.cleaned_data.get('username')
        user.runner_team = self.cleaned_data.get('runner_team')
        user.email=False
        user.runner_age = self.cleaned_data.get('runner_age')
        user.runner_category = self.cleaned_data.get('runner_category')
        user.runner_gender = self.cleaned_data.get('runner_gender')
        user.zabeg22 = self.cleaned_data.get('zabeg22')
        user.zabeg23 = self.cleaned_data.get('zabeg23')
        user.save()
        adapter.save_user(request, user, self)
        return user
