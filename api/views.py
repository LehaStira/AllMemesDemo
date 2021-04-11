from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.decorators import action
from .serializers import MemeSerializer, TagSerializer
from .models import Meme, Tag
# Create your views here.


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class MemeViewSet(viewsets.ModelViewSet):
    serializer_class = MemeSerializer
    queryset = Meme.objects.all()

    @action(detail=False, methods=['GET'])
    def test_method(self, request):
        response = {'message':'hello'}
        return Response(response, status=status.HTTP_200_OK)

    @action(detail=False,  methods=['POST'])
    def searching(self, request):
        if 'searching_message' in request.data:
            message = request.data['searching_message']
            try:
                print(request.data['searching_message'])
                result = Tag.objects.get(name = message).memes.all()
                print(result)
                my_input = list()
                for meme in result:
                    my_input.append(meme.picture.path)
                print(my_input)
                response = {
                    'action': 'Pictures successfuly get',
                    'status': status.HTTP_200_OK,
                    'result': my_input
                }
                return Response(response)
            except:
                response = {
                    'action': "Pictures doesnt get",
                    'status': status.HTTP_200_OK,
                    'result': 0
                }
                return Response(response)
        else:
            response = {
                'data' : 'Bad data',
                'status' : status.HTTP_400_BAD_REQUEST
            }
            return Response(response)