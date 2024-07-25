import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import  get_object_or_404
from genero.models import Genero
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genero.serializers import GeneroSerializer

#Com django rest framework
class GeneroCreateListView(generics.ListCreateAPIView):
    #valida o token JWT, tornando obrigatorio informar token
    permission_classes = (IsAuthenticated,)
    #retonar todos os objetos
    queryset = Genero.objects.all()
    #retonar objetos filtrado
    #queryset = Genero.objects.filter(name='Ação')
    serializer_class = GeneroSerializer

class GeneroRetrivieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

#Sem django rest framework
# @csrf_exempt
# def lista_cria_genero(request):
#     if request.method == 'GET':
#         generos = Genero.objects.all()
#         data = [{'id': genero.id, 'name': genero.name} for genero in generos]
#         return JsonResponse(data, safe=False)
#     elif request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))
#         novo_genero = Genero(name=data['name'])
#         novo_genero.save()
#         return JsonResponse({'id': novo_genero.id,'name': novo_genero.name},
#                             status=201,
#                             )
    
# @csrf_exempt
# def detalhe_genero(request, pk):
#     genero = get_object_or_404(Genero, pk=pk)
#     if request.method == 'GET':
#         data = {'id': genero.id,'name':genero.name}
#         return JsonResponse(data)
#     elif request.method == 'PUT':
#         data = json.loads(request.body.decode('utf-8'))
#         genero.name = data['name']
#         genero.save()
#         return JsonResponse({'id': genero.id,'name': genero.name},
#                             status=201,
#                             )
#     elif request.method == 'DELETE':
#         genero.delete()
#         return JsonResponse({'message':'Gênero excluído com sucesso.'},
#                             status=204)
