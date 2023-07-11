from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator

# View에 Model(Post 게시글) 가져오기
from .models import Post

from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request,'main/index.html')

def board(request):
    all_boards = Post.objects.all().order_by("-postdate") # 모든 데이터 조회, 내림차순(-표시) 조회
    paginator = Paginator(all_boards, 5)
    page = int(request.GET.get('page', 1))
    board_list = paginator.get_page(page)
    return render(request, 'main/board.html', {'title':'Board List', 'board_list':board_list})
    '''
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Post.objects.all()
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다
    return render(request, 'main/board.html', {'postlist': postlist})'''

# blog의 게시글(posting)을 부르는 posting 함수
def posting(request, pk):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = Post.objects.get(pk=pk)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'main/posting.html', {'post':post})

def new_post(request):
    if request.method == 'POST':
        new_article=Post.objects.create(
            postname=request.POST['postname'],
            contents=request.POST['contents'],
            user=request.user,
            )
        return redirect('./')
    return render(request, 'main/writing.html')


def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/board')
    return render(request, 'main/remove_post.html', {'Post': post})