from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from filme.models import Filme
from filme.serializers import FilmeSerializer

class FilmeCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer

class FilmeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer