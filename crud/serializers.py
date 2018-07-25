from rest_framework import serializers
from .models import Libro


class LibroSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    titulo = serializers.CharField()
    fecha_publicacion = serializers.DateField()
    autor = serializers.CharField()
    precio = serializers.DecimalField(max_digits=5, decimal_places=2)
    paginas = serializers.IntegerField()

    def create(self, validated_data):
        return Libro.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.titulo = validated_data.get('titulo', instance.titulo)
        instance.fecha_publicacion = validated_data.get('fecha_publicacion', instance.fecha_publicacion)
        instance.precio = validated_data.get('precio', instance.precio)
        instance.paginas = validated_data.get('paginas', instance.paginas)
        instance.save()
        return instance
    '''
    class Meta:
        model = Libro
        fields = ('id','titulo','fecha_publicacion','autor','precio','paginas')
    '''
