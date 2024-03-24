from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ClaimsSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["user_id"] = user.id
        token["username"] = user.username

        return token
