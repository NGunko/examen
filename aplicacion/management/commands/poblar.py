from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

import django
import random
django.setup()

from aplicacion.models import vendedor, prenda, venta
#models
VENDEDOR = 'vendedor'
PRENDA = 'prenda'
VENTA = 'venta'
# The name of this class is not optional must  be Command
# otherwise manage.py will not process it properly
class Command(BaseCommand):
    #  args = '<-no arguments>'
    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = 'This scripts populates de workflow database, no arguments needed.' \
           'Execute it with the command line python manage.py populate'

    # handle is another compulsory name, This function will be
    # executed by default
    def handle(self, *args, **options):
        self.cleanDatabase()
        self.addVendedor(3)
        self.addPrenda(4)
        self.addVenta(1001,1001,1001)
        self.addVenta(1002,1001,1003)
        self.addVenta(1003,1003,1003)
        self.addVenta(1004,1003,1001)
        self.addVenta(1005,1002,1002)

    def cleanDatabase(self):
        # delete all
        # workflows and  categories
        vendedor.objects.all().delete()
        prenda.objects.all().delete()
        venta.objects.all().delete()
        pass

    def addVendedor(self, noVendedores):
        for i in range(noVendedores):
            nombre = 'vendedor' + str(i+1)
            x = 1001 + i
            c = vendedor.objects.get_or_create(id = x, nombreV=nombre)[0]
            c.save()

    def addPrenda(self, noPrendas):
        for i in range(noPrendas):
            if i != 3:
                nombre = 'prenda' + str(i+1)
            else:
                nombre = ''
            x = 1001 + i
            c = prenda.objects.get_or_create(id = x, nombreP=nombre)[0]
            c.save()

    def addVenta(self, idVent, idVend, idPrend):
            v = venta.objects.get_or_create(id=idVent)[0]
            v.vendedor = vendedor.objects.filter(id=idVend)
            v.prenda = prenda.objects.filter(id=idPrend)
            v.save()
