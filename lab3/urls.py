from django.contrib import admin
from stocks import views as stock_views
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'toys', stock_views.ToyViewSet)
router.register(r'users', stock_views.UsersViewSet)
router.register(r'basket', stock_views.BasketViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls)
]
