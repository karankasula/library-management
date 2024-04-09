from django.shortcuts import render
from django.views import View
# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        response = render(request, "index.html", {})
        response.headers["X-Frame-Options"] = None
        return response
