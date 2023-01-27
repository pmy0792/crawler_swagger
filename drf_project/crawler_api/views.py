from django.shortcuts import render


from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,RetrieveAPIView,ListCreateAPIView, UpdateAPIView
from crawler_api.serializer import ProjectListCreateSerializer, ProjectRetrieveSerializer, CrawlerListCreateSerializer,CrawlerRetrieveUpdateSerializer, ImageListSerializer, ImageRetrieveSerializer
from crawler.models import Project, Crawler, Image
from rest_framework.response import Response


# Create your views here.
class ProjectListCreateAPIView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListCreateSerializer


class ProjectRetrieveAPIView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectRetrieveSerializer


class CrawlerListCreateAPIView(ListCreateAPIView):
    queryset = Crawler.objects.all()
    serializer_class = CrawlerListCreateSerializer


class CrawlerRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Crawler.objects.all()
    serializer_class = CrawlerRetrieveUpdateSerializer

class ImageListAPIView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageListSerializer

class ImageRetrieveAPIView(RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageRetrieveSerializer