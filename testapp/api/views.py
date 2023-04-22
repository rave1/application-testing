from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from api.models import Author


class AuthorList(APIView):
    renderer_classes = (TemplateHTMLRenderer, )
    template_name = 'author_list.html'

    def get(self, request):
        queryset = Author.objects.all()
        return Response({
            'authors': queryset
        })


class UserList(APIView):
    renderer_classes = (TemplateHTMLRenderer, )
    template_name = 'user_list.html'

    def get(self, request):
        queryset = get_user_model().objects.all()
        return Response({'users': queryset})
