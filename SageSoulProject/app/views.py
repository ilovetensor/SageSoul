from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class ChatPageView(TemplateView):
    template_name = 'chatPage.html'


@method_decorator(csrf_exempt, name='dispatch')
class getAnswerView(View):
    def post(self, request):

        # Result generated from algorithm
        result = "You should exercise more and eat nutritious food"
        print(request.POST.get('question'))
        return HttpResponse(result)