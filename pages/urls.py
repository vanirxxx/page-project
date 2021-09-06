from django.urls import path
from .views import aboutPageView, homePageView

urlpatterns = [
    path('', homePageView.as_view(), name='home'),
    path('about/', aboutPageView.as_view(), name='about')
]