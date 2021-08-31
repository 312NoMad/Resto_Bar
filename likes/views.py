from django.shortcuts import render, redirect
from .models import Products, Like
def post_view(request):
    queryset = Products.objects.all()
    user = request.user
    context = {
        'queryset': queryset,
        'user': user,
    }
    return render(request)
def like_post(request):
    return redirect('post:post-list')
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        if user in post_obj.liked.all():
            post.obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        like, created = Like.objects.get-or_create(user=user, post_id=post_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'like'
        like.save()
    return redirect('posts:post-list')