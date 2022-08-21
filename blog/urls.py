from blog.views import CreatePost, ListPost, MyList, Publish, PostDetail
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path("post/create/", CreatePost.as_view(), name='create-post'),
    path("post/all/", ListPost.as_view(), name='post-list'),
    path("post/my/", MyList.as_view(), name="my-post"),
    path("post/publish/", Publish.as_view(), name="publish-post"),
    path("post/<int:id>/", PostDetail.as_view(), name="post-detail"),
]
