from django.urls import path , include

from apis.routers import router

urlpatterns = [
    path('', include(router.urls)),
]
