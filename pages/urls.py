from django.urls import path
from .views import HomePageView

urlpatterns = [
    # path('', views.HomePageView, name='home'), # Function based view
    path('', HomePageView.as_view(), name='home'),
]