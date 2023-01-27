from rest_framework import serializers
from django.contrib.auth.models import User
from crawler.models import Project, Crawler, Image

# Serializer: 출력 포맷이나 출력 내용에 관한 것 다 포함시킴

class ProjectListCreateSerializer(serializers.ModelSerializer): # HyperlinkedModelSerializer보다 ModelSerializer를 더 많이 사용
    class Meta:
        model = Project
        fields = '__all__' # Client에게 보낼 field 지정
        #fields=['id','title','image','like','category']
    
class ProjectRetrieveSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Project
        fields = '__all__' # Client에게 보낼 field 지정
        #fields=['id','title','image','like',' category']    
        # exclude = ['create_dt'] # 해당 field 제외하고 나머지 field 모두 client에게 보내줌
        
class CrawlerListCreateSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Crawler
        fields = '__all__'
        
        
class CrawlerRetrieveUpdateSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Crawler
        fields = '__all__'
    
class ImageListSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Image
        fields = '__all__'
        
class ImageRetrieveSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Image
        fields = '__all__'