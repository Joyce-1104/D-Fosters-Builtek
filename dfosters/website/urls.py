from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('services/',views.services,name="services"),
    path('projects/',views.projects,name ="projects"),
    path('contact/', views.contact_view, name='contact'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
