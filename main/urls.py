from django.urls import path,include
# from rest_framework import routers
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.DefaultRouter()
# router.register('User', views.UserView)
# router.register('Tag', views.TagsView)
# router.register('Blogs', views.BlogsView)

urlpatterns = [
    # path('api-root/', include(router.urls)),
    path('api-root/blog/', views.BlogsView,),
    path('api-root/tag/', views.TagsView),
    path('api-root/user/', views.UserView),
    path('blog/',views.Blog, name='Blog'),
    path('form/',views.Form, name='Form'),
    path('blog/<int:pk>',views.View_blog, name='View_blog'),
    path('blog/update/<int:pk>',views.Update, name='Update'),
    path('blog/delete/<int:pk>',views.Delete, name='Delete'),
]

urlpatterns = format_suffix_patterns(urlpatterns)