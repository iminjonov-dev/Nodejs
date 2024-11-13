from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairView):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token[]