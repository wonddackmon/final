from django.contrib import admin
from django.urls import path
from .views import *

app_name='main'

urlpatterns=[
    path('admin/', admin.site.urls),
    # 웹사이트의 첫화면은 index 페이지이다 + URL이름은 index이다
    path('', index, name='index'),
    # URL:80/blog에 접속하면 blog 페이지 + URL이름은 blog이다
    path('board/', board, name='blog'),
    # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('board/<int:pk>', posting, name="posting"),
    # 글쓰기 페이지
    path('board/writing', new_post),
    # 삭제 페이지
    path('board/<int:pk>/remove/', remove_post),
]