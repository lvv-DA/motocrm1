from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from crm.views import ClientViewSet, CustomerViewSet, SalesRepresentativeViewSet, LocationViewSet, OpportunityViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.views import APIView
from rest_framework.response import Response

# Optionally, a simple API root view
class APIRoot(APIView):
    def get(self, request):
        return Response({
            'clients': '/api/clients/',
            'customers': '/api/customers/',
            'sales-representatives': '/api/sales-representatives/',
               'locations': '/api/locations/',
            'opportunities': '/api/opportunities/',
        })

# Set up the router
router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'sales-representatives', SalesRepresentativeViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'opportunities', OpportunityViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', APIRoot.as_view(), name='api-root'),  # The new root endpoint
    path('api/', include(router.urls)),
    # Token-based authentication routes
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
