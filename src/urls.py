from django.urls import path
from .views import home, filter_values, specific_page
urlpatterns = [
    path('', home, name="home-page"),
    path('filtered/', filter_values, name="filtered-page"),
    path('specific_page/<int:sem>/<str:branch>/<str:type>/', specific_page, name="specific-page")
]
