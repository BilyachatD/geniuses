from django.shortcuts import render
from django.views.generic.base import View

class MainChoiseView(View):
    def get(self, request):
        return render(request, 'mainChoiseTemplate.html')
