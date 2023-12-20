from rest_framework import views
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .utils import get_para_from_index, get_encoding
import pinecone

''' Dummy, this view can be deleted because
 frontend doesn't need data on from backend '''


class HomeView(views.APIView):
    def get(self, request):
        data = {"name": "R"}
        return Response(data)


@method_decorator(csrf_exempt, name='dispatch')
class similarityView(views.APIView):

    def post(self, request):
        user_input = request.data['user_input']
        pinecone.init(
            api_key='e66692b7-057f-47db-b61f-79e085cf8b54',
            environment='gcp-starter'
        )


        # Get index from faiss data
        index_name = INDEX_NAME
        query_encoding = get_encoding(user_input)
        faiss_index = pinecone.Index(index_name=index_name)

        # fetch text from database
        output = get_para_from_index(query_encoding, faiss_index)

        return Response({"output": output})


@method_decorator(csrf_exempt, name='dispatch')
class chatView(views.APIView):

    def post(self, request):
        user_query = request.data['question']
        # Call the function to return response
        chat_response = "dummy response"
        return Response({"chat_response": chat_reponse})
