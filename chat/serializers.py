from rest_framework import serializers

from chat.models import Message


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    author = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    author_username = serializers.ReadOnlyField(source='author.username')
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    pub_date = serializers.ReadOnlyField()
    message = serializers.ReadOnlyField()
    image_file = serializers.FileField()

    class Meta:
        model = Message
        fields = ('id', 'author', 'pub_date', 'image_file',
                  'message', 'author_username', 'author_first_name',
                  'author_last_name')
