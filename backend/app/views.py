from rest_framework import views
from rest_framework import status
from rest_framework.response import Response 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class similarityView(views.APIView):

    def post(self, request):
        user_input = request.data.get('user_input')
        if not user_input:
            return Response({"error":"User Input not provided"}, status = status.HTTP_400_BAD_REQUEST)
        # Call function to find similarity
        similar_output = "Dummy Text"
        numbers = [2,3,4,5]
        return Response({"output":similar_output, "numbers":numbers}, status=status.HTTP_200_OK)
    


class chatView(views.APIView):

    def post(self, request):
        user_query = request.data.get('question')
        if not user_query:
            return Response({"error":"User query not provided"}, status = status.HTTP_400_BAD_REQUEST)
        
        # Call the function to return response
        chat_reponse = "dummy response"
        return Response({"chat_response":chat_reponse}, status=status.HTTP_200_OK)