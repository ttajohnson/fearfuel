from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('movies', views.MovieViewSet, basename="movies")
router.register('users', views.UserViewSet, basename='users')

urlpatterns = router.urls + [
    path('currentuser/', views.CurrentUserViewSet.as_view())
]