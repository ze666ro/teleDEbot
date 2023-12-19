import random

from django.http import HttpResponseNotFound
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Words
        fields = ['pk', 'gender', 'word']


class RandomWord(APIView):
    def get(self, *args, **kwargs):
        all_words = models.Words.objects.all()
        random_word = random.choice(all_words)
        serialized_random = WordSerializer(random_word,many=False)
        return Response(serialized_random.data)


class NextWord(APIView):
    def get(self, request, pk, format = None):
        word = models.Words.objects.filter(pk__gt=pk).first()
        if not word:
            return HttpResponseNotFound
        ser_word= WordSerializer(word, many=False)
        return Response(ser_word.data)