from django.conf.urls import url, include
from reactapp import views

app_name = 'reactapp'

urlpatterns = [
    # list users.
    url(r'^$', views.IndexView.as_view(), name='index_view'),
]
