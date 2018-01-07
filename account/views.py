from rest_framework import viewsets, permissions

from .models import Account
from .serializers import AccountSerializer


class AccountViewSet(viewsets.ReadOnlyModelViewSet):
    """Views of Account model.
    """

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.DjangoModelPermissions]
