from django.contrib import admin
from .models import Client, Customer, SalesRepresentative, Location, Opportunity

admin.site.register(Client)
admin.site.register(Customer)
admin.site.register(SalesRepresentative)
admin.site.register(Location)
admin.site.register(Opportunity)
