from rest_framework import static, status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Message
from .serializers import MessageSerializer


class MessageAPI(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all().order_by('-pub_date')
    pagination_class = PageNumberPagination

    @action(methods=['get'], detail=False, name="get_object")
    def get_object(self, request):
        pk = request.GET.get('pk')
        try:
            message = Message.objects.get(id=pk)
            serializer = MessageSerializer(message)
            return Response(serializer.data)
        except Message.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    @action(methods=['get'], detail=False, name="delete")
    def delete(self, request):
        pk = request.GET.get('pk')
        message = Message.objects.get(id=pk)
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], detail=False, name="delete")
    def new_messages(self, request):
        last_message_id = request.GET.get('last_message_id')
        return Response(data=Message.objects.filter(id__gt=last_message_id).exists())

