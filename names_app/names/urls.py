from django.conf.urls import url
from names import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'', csrf_exempt(views.HomePageView.as_view())),
]
