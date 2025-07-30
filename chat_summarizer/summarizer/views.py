from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SummarizeRequestSerializer
from .ollama_utils import generate_summary
import logging

logger = logging.getLogger("summarizer")

class SummarizeView(APIView):
    def post(self, request):
        logger.info(f"Incoming request: {request.data}") 
        serializer = SummarizeRequestSerializer(data=request.data)
        if serializer.is_valid():
            chat_data = serializer.validated_data["chat"]
            summary = generate_summary(chat_data)
            logger.info(f"Outgoing response: {{'summary': '{summary}'}}") 
            return Response({"summary": summary}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

