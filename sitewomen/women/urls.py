from django.urls import path, re_path, register_converter, include
from . import views
from . import converters
from rest_framework import routers
from .views import CategoryApiView, ItemsApiView

app_name = 'women'
router = routers.DefaultRouter()
router.register(r'api/cat', CategoryApiView)
router.register(r'api/Items', ItemsApiView)


urlpatterns = [
    path('', views.index, name='home'),  # http://127.0.0.1:8000
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('category/<slug:cat_slug>/', views.show_category, name = 'category'),
    path('',include(router.urls)),
]
