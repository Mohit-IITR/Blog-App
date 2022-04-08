from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('User', views.UserView)
router.register('Tags', views.TagsView)
router.register('Blogs', views.BlogsView)

urlpatterns = [
    path('', include(router.urls)),
]