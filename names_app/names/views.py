from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

names2 = ['Jhon', 'Elton', 'Michael']
names = "Jhon, Elton, Micheal"
# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        html = "<html><body><div><p1>Names:</p1>" + ','.join(names2) + "</br></br></br></div><form method=\"post\" action=\"http://localhost:8000\"> Name:<input type=\"text\" name=\"name\" /><input type=\"submit\" value=\"Submit\" /></form></body></html>"
        return HttpResponse(html);

    def post(self, request, **kwargs):
        name = request.POST.get("name");
        names2.append(name);
        return HttpResponse(200);
