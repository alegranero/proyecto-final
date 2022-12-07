from ejemplo.models import Familiar

Familiar(nombre="Roberto", direccion="Rio Parana 745", numero_pasaporte=123123).save()
Familiar(nombre="Mabel", direccion="Alberdi 805", numero_pasaporte=890890).save()
Familiar(nombre="Tatiana", direccion="Corrientes 1521", numero_pasaporte=345345).save()
Familiar(nombre="Florencia", direccion="Chaco 520", numero_pasaporte=567567).save()

print("Se cargo con éxito los usuarios de pruebas")

#para resetear la base, se borra sqlite3 y luego se crea una nueva con "python manage.py migrate"
#migrate crea la base de datos