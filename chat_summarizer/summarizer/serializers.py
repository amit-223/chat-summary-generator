from rest_framework import serializers

class ChatMessageSerializer(serializers.Serializer):
    role = serializers.ChoiceField(choices=["user", "bot"])
    message = serializers.CharField()

class SummarizeRequestSerializer(serializers.Serializer):
    chat = ChatMessageSerializer(many=True)
