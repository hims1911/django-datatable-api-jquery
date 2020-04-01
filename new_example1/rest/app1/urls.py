from django.urls import path, include
from .views import PostList,index,PostDetail,PostDetails_view,FormatList

urlpatterns = [
    path('Post/', PostList),
    path('Post/index',index),
    path('Post/<int:pk>/',PostDetail),
    path('Post/detail/<int:pk>', PostDetails_view),
    path('Format/', FormatList),
]