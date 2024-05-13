from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import User


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


class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(max_value=None, min_value=1)
    occupation = serializers.CharField(max_length=50)
    date_of_birth = serializers.DateField()
    email=False

    class Meta:
        model = User
        fields = ['runner', 'team']

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'age': self.validated_data.get('age'),
            'occupation': self.validated_data.get('occupation'),
            'date_of_birth': self.validated_data.get('date_of_birth'),
        }

        # override save method of RegisterSerializer

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.age = self.cleaned_data.get('age')
        user.occupation = self.cleaned_data.get('occupation')
        user.date_of_birth = self.cleaned_data.get('date_of_birth')
        user.save()
        adapter.save_user(request, user, self)
        return user
