from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    # デフォルトのページ
    path('', views.post_list, name='post_list'),
    # n件目の投稿がhttp://127.0.0.1:8000/post/{n}/に表示されるようにする
    # <int:pk>→整数値がpkという名前の変数でビューに渡されることを期待
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/',views.post_new, name='post_new'),
    path('post/<int:pk>/edit/',views.post_edit, name='post_edit'),
]
