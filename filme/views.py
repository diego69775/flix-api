from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from filme.models import Filme
from filme.serializers import FilmeSerializer

class FilmeCreateListView(generics.ListCreateAPIView):
    #IsAuthenticatedOrReadOnly caso for get, head e options não é necessário autenticar.
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer

class FilmeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer