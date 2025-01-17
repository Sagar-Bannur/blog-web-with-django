from django.urls import path
from bloga import views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('blog/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
