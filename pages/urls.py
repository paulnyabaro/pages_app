from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    # path('', views.HomePageView, name='home'), # Function based view
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]