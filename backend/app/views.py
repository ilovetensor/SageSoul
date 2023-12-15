from rest_framework import views
from rest_framework.response import Response 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

''' Dummy, this view can be deleted because
 frontend doesn't need data on from backend '''
class HomeView(views.APIView):
    def get(self, request):
        data={"name":"R"}
        return Response(data)
    


@method_decorator(csrf_exempt, name='dispatch')
class similarityView(views.APIView):

    def post(self, request):
        user_input = request.data['user_input']
        # Call function to find similarity
        similar_output = "Dummy Text"
        numbers = [2,3,4,5]
        return Response({"output":similar_output, "numbers":numbers})
    


@method_decorator(csrf_exempt, name='dispatch')
class chatView(views.APIView):

    def post(self, request):
        user_query = request.data['question']
        # Call the function to return response
        chat_reponse = "dummy response"
        return Response({"chat_response":chat_reponse})