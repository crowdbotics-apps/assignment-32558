from rest_framework import viewsets, mixins
from home.models import App, Plan, Subscription
from .serializers import AppSerializer, PlanSerializer, SubscriptionSerializer
from rest_framework import authentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# from home.api.v1.serializers import (
#     SignupSerializer,
#     UserSerializer,
# )


# class SignupViewSet(ModelViewSet):
#     serializer_class = SignupSerializer
#     http_method_names = ["post"]


# class LoginViewSet(ViewSet):
#     """Based on rest_framework.authtoken.views.ObtainAuthToken"""

#     serializer_class = AuthTokenSerializer

#     def create(self, request):
#         serializer = self.serializer_class(
#             data=request.data, context={"request": request}
#         )
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data["user"]
#         token, created = Token.objects.get_or_create(user=user)
#         user_serializer = UserSerializer(user)
#         return Response({"token": token.key, "user": user_serializer.data})


class AppViewSet(viewsets.ModelViewSet):
    serializer_class = AppSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = App.objects.all()


class SubscriptionViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = SubscriptionSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Subscription.objects.all()


class PlanViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PlanSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Plan.objects.all()
