from django.urls import path

from hw_8_1.views import person


urlpatterns = [
    path('', person),
    # path('<int:pk>/', person_pk),
]
