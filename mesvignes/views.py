from django.shortcuts import render
from django.views.generic import View


# Create your views here.

class ParcelleDetail(View):

    """ Detail d'une parcelle """

    template_name = "parcelle_detail.html"

    def get(self, request, *args, **kwargs):
        context = {} 

        context['data'] = "data"

        return render(request, self.template_name, context)


