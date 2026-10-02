from django.db import models

# Create your models here.

class PerfilUsuario(models.Model):
    ROLES = [
        ('AUTOR', 'Autor'),
        ('LECTOR', 'Lector'),
        ('ADMIN', 'Administrador'),
    ]
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()
    bio = models.TextField(blank=True, null=True)
    rol = models.CharField(max_length=15, choices=ROLES, default='LECTOR')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Publicacion(models.Model):
    ESTADOS = [
        ('BORRADOR', 'Borrador'),
        ('REVISION', 'En Revisión'),
        ('PUBLICADO', 'Publicado'),
        ('ARCHIVADO', 'Archivado'),
    ]
    VISIBILIDAD = [
        ('PUBLICA', 'Pública'),
        ('PRIVADA', 'Privada'),
    ]
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(PerfilUsuario, on_delete=models.RESTRICT, related_name='publicaciones')
    estado_actual = models.CharField(max_length=15, choices=ESTADOS, default='BORRADOR')
    visibilidad = models.CharField(max_length=10, choices=VISIBILIDAD, default='PUBLICA')
    class Meta:
        verbose_name_plural = "Publicaciones"
        
    def __str__(self):
        return self.titulo

class HistorialEstado(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='historial')
    estado_anterior = models.CharField(max_length=15)
    estado_nuevo = models.CharField(max_length=15)
    fecha_cambio = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.publicacion.titulo}: {self.estado_anterior} -> {self.estado_nuevo}"

class Interaccion(models.Model):
    TIPOS = [
        ('LECTURA', 'Lectura'),
        ('GUARDADO', 'Guardado'),
        ('COMPARTIDO', 'Compartido'),
    ]
    lector = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    tipo_interaccion = models.CharField(max_length=15, choices=TIPOS)
    fecha_interaccion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Interacciones"
    
    def __str__(self):
        return f"{self.lector.nombre} - {self.tipo_interaccion}"