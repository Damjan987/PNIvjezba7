from django.conf.urls import url
from vjezba7app import views

app_name = "vjezba7app"

urlpatterns = [
    url('index/', views.index, name='index'),
    url('register/', views.register, name='register'),
    url('user_login/', views.user_login, name='user_login'),
    url(r'^$', views.ProjectionListView.as_view(), name="list"),
    url(r'^(?P<pk>\d+)/$', views.ProjectionDetailView.as_view(), name='detail'),
    url(r'^create/$', views.CardCreateView.as_view(), name="create")
]