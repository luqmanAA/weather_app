from django.http import HttpResponse
from django.views import View


class IndexView(View):

    def get(self, request, **kwargs):
        return HttpResponse('This is the homepage')


