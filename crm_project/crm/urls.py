from django.urls import path
from .views import ClientViewSet, CustomerViewSet, SalesRepresentativeViewSet, LocationViewSet, OpportunityViewSet
from rest_framework.routers import DefaultRouter

# Set up the router
router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'sales-representatives', SalesRepresentativeViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'opportunities', OpportunityViewSet)

urlpatterns = router.urls
