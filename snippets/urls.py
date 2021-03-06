from django.conf.urls import url, include
from snippets import views
from rest_framework.authtoken import views as authtokenviews
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^search/$', views.SearchView.as_view(), name='search'),
    url(r'^api-token-auth/', authtokenviews.obtain_auth_token)
]
