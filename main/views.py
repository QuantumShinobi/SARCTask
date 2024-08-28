from django.shortcuts import render
from django.views import View
# Create your views here.


def index(request):
    return render(request, './main/index.html')


class AddItemView(View):
    def get(self, request):
        return render(request, './main/add_items.html')
