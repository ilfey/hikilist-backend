from django.db.models import Q

from drf_spectacular.utils import extend_schema, extend_schema_view

from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from accounts import models

from accounts.serializers.accounts import AccountListSerializer
from accounts.serializers.rates import RateListSerializer
from accounts.serializers.lists import ListListSerializer


@extend_schema_view(
    list=extend_schema(
        summary="List accounts",
    ),
    retrieve=extend_schema(
        summary="Details of accounts",
    ),
    accounts_lists_list=extend_schema(
        summary="Get lists of an account",
    ),
    accounts_lists_retrieve=extend_schema(
        summary="Get details of a list",
    ),
    accounts_rates_list=extend_schema(
        summary="Get rates of an account",
    ),
    accounts_rates_retrieve=extend_schema(
        summary="Get details of a rate",
    ),
    logout=extend_schema(
        summary="Logout from the account",
    ),
    refresh=extend_schema(
        summary="Refresh access token",
    ),
    accounts_rates_import=extend_schema(
        summary="Import rates (Not implemented)",
        responses={
            501: "Not implemented",
        },
    ),
)
class AccountViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = AccountListSerializer
    queryset = models.User.objects.all()
    lookup_url_kwarg = "account_pk"

    def get_queryset(self):
        pk = self.kwargs.get("account_pk")
        super().get_queryset()
        return models.User.objects.filter(id=pk)

    @action(methods=["GET"], detail=True, url_path="rates")
    def accounts_rates_list(self, request, account_pk):
        # If account not exists
        if not models.User.objects.filter(id=account_pk).exists():
            return Response(
                {
                    "detail": "Account not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        data = models.Rate.objects.filter(user_id=account_pk)
        serializer = RateListSerializer(data, many=True)

        return Response(serializer.data)

    @action(methods=["GET"], detail=True, url_path="rates/(?P<rate_pk>[^/.]+)")
    def accounts_rates_retrieve(self, request, account_pk, rate_pk):
        # If account not exists
        if not models.User.objects.filter(id=account_pk).exists():
            return Response(
                {
                    "detail": "Account not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        try:
            data = models.Rate.objects.get(user_id=account_pk, id=rate_pk)
        except models.Rate.DoesNotExist:
            data = None

        # If rate not exists
        if not data:
            return Response(
                {
                    "detail": "Rate not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = RateListSerializer(data)

        return Response(serializer.data)

    @action(methods=["POST"], detail=True, url_path="rates/import")
    def accounts_rates_import(self, request, account_pk):
        # If account not exists
        if not models.User.objects.filter(id=account_pk).exists():
            return Response(
                {
                    "detail": "Account not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(
            {
                "detail": "Not implemented",
            },
            status=status.HTTP_501_NOT_IMPLEMENTED,
        )

    @action(methods=["GET"], detail=True, url_path="lists")
    def accounts_lists_list(self, request, account_pk):
        # If account not exists
        if not models.User.objects.filter(id=account_pk).exists():
            return Response(
                {
                    "detail": "Account not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        data = models.List.objects.filter(Q(user_id=account_pk) | Q(is_primary=True))
        serializer = ListListSerializer(data, many=True)

        return Response(serializer.data)

    @action(methods=["GET"], detail=True, url_path="lists/(?P<list_pk>[^/.]+)")
    def accounts_lists_retrieve(self, request, account_pk, list_pk):
        # If account not exists
        if not models.User.objects.filter(id=account_pk).exists():
            return Response(
                {
                    "detail": "Account not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        try:
            data = models.List.objects.get(
                (Q(user_id=account_pk) | Q(is_primary=True)) & Q(id=list_pk)
            )
        except models.List.DoesNotExist:
            data = None

        # If list not exists
        if not data:
            return Response(
                {
                    "detail": "List not found",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = ListListSerializer(data)

        return Response(serializer.data)
