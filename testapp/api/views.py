from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from api.models import Author, Book


class AuthorList(APIView):
    renderer_classes = (TemplateHTMLRenderer, )
    template_name = 'author_list.html'

    def get(self, request):
        queryset = Author.objects.all()
        return Response({
            'authors': queryset
        })
