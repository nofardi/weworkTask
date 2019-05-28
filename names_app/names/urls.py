from django.conf.urls import url
from names import views


urlpatterns = [
    url(r'', views.HomePageView.as_view()),
]
