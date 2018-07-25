from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from crud.models import Libro
from crud.serializers import LibroSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def libro_listar(request):
    if request.method == 'GET':
        libros = Libro.objects.all().order_by('-pk')
        serializer = LibroSerializer(libros, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LibroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def libro_detalle(request, pk):
    try:
        libro = Libro.objects.get(pk=pk)
    except Libro.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LibroSerializer(libro)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LibroSerializer(libro, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        libro.delete()
        return HttpResponse(status=204)
