from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from ator.models import Ator
from ator.serializers import AtorSerializer

class AtorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer

class AtorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser,)
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer