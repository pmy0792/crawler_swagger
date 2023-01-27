
from django.urls import path,include
from crawler_api import views


urlpatterns=[
    # DRF에서는 url name에 list와 detail 사용
    # url에 pk가 없는 경우에는 list
    #path('post/', views.PostListAPIView.as_view(), name='post-list'),
    #path('post/<int:pk>/', views.PostRetrieveAPIView.as_view(), name='post-detail'),
    #path('comment/', views.CommentCreateAPIView.as_view(), name='comment-list'),
    #path('post/<int:pk>/like/', views.PostLikeAPIView.as_view(), name='like-list'),
    
    path('project/', views.ProjectListCreateAPIView.as_view(), name='project-list'),
    path('project/<int:pk>', views.ProjectRetrieveAPIView.as_view(), name='project-detail'),
    path('crawler/',views.CrawlerListCreateAPIView.as_view(), name='crawler-list'),
    path('crawler/<int:pk>', views.CrawlerRetrieveUpdateAPIView.as_view(), name='crawler-detail'),
    path('image/', views.ImageListAPIView.as_view(),name='image-list'),
    path('image/<int:pk>',views.ImageRetrieveAPIView.as_view(),name='image-detail'),
]