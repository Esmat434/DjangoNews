from django.shortcuts import render, HttpResponse,HttpResponseRedirect,get_object_or_404
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import Artical,SaveArtical,Category,Images,PageView,Like
from user_account.models import CustomUser

def Home(request):
    artical_lists = []
    categories = Category.objects.all()
    for category in categories:
        artical_lists.append(Artical.objects.filter(category=category).order_by('-published_date')[:5])
    if artical_lists and len(artical_lists[1]) >= 3:
        first = artical_lists[1][0]
        second = artical_lists[1][1]
        third = artical_lists[1][2]
        artical_lists[1] = artical_lists[1][3:]
    return render(request,'Home/home.html',{'articals':artical_lists,'first':first,'second':second,'third':third})

def Search(request):
    if request.method == 'POST':
        data = request.POST.get('search')
        content = Artical.objects.filter(Q(title__icontains = data) | Q(content__icontains=data))
        print(content)
        return render(request,'Home/search.html',{'contents':content})
    return render(request,'Home/search.html')
@login_required()
def like(request):
    path = request.path
    username = request.user.username
    liked,created = Like.objects.get_or_create(username=username,page_name=path)
    if not created:
        liked.delete()
        return False
    return True

def View(request):
    path = request.path
    view_count = PageView.objects.filter(page_name=path).count()
    return view_count

def Content(request,pk):
    path = request.path
    try:
        artical = Artical.objects.get(id=pk)
    except Artical.DoesNotExist:
        return render(request,'Account/some_error.html',{'status_code':400,'title':'News DoesNotExist','error':'This News Artical DoesNotExist Please Search another things!'})
    data = Images.objects.filter(artical=artical)
    view_count = View(request)
    is_save = SaveArtical.objects.filter(username=request.user.username,artical=artical).exists()
    is_like = Like.objects.filter(username=request.user.username,page_name=request.path).exists()
    like_count = Like.objects.filter(page_name=request.path).count()
    if request.method == 'POST':
        button = request.POST.get('button')
        created = SaveArtical.objects.filter(username=request.user.username,artical=artical).exists()
        if button == 'like':
            is_like = like(request)
        elif button == 'save':
            save_instance,created = SaveArtical.objects.get_or_create(username=request.user.username,artical=artical)
            if not created:
                save_instance.delete()
        return render(request,'Home/content.html',{'title':artical,'datas':data,'view_count':view_count,'is_like':is_like,'like_count':Like.objects.filter(page_name=path).count(),'is_save':created})
    return render(request,'Home/content.html',{'title':artical,'datas':data,'view_count':view_count,'is_like':is_like,'like_count':like_count,'is_save':is_save})

@login_required()
def saveArtical(request):
    saveArt = SaveArtical.objects.filter(username=request.user.username)
    if request.method == 'POST':
        item_id = request.POST.get('button')
        try:
            data = SaveArtical.objects.get(id=item_id)
            data.delete()
        except SaveArtical.DoesNotExist:
            return render(request,'Account/some_error.html',{'status_code':400,'title':'Item DoesNotExist','error':'This Artical DoesNotExist','url_page':'artical/saved'})
    return render(request,'Home/SaveArtical.html',{'articals':saveArt})

def CategoryView(request,category_name):
    category = get_object_or_404(Category,name=category_name.capitalize())
    data = Artical.objects.filter(category=category)
    first = data[0]
    second  = data[1]
    third = data[2]
    data = data[3:]
    return render(request,'Home/CategoryView.html',{'datas':data,'first':first,'second':second,'third':third,'name':category.name})

def update_user_settings(data, user):
    """
    Update user settings based on the button clicked.
    """
    btn = data.get('button')
    if btn == 'username':
        username = data.get('username')
        if username and user.username != username:
            user.username = username
            user.save()
    elif btn == 'email':
        email = data.get('email')
        if email and user.email != email:
            user.email = email
            user.save()
    elif btn == 'password':
        form = PasswordChangeForm(user, data)
        if form.is_valid():
            form.save()
        else:
            return 

@login_required()
def AccountView(request,name1,name2):
    name1,name2 = name1.lower(),name2.lower()
    pages = {
        "over-view":'Account/overView.html',
        'settings':'Account/settings.html',
        'comments':'Account/comment.html',
        'privacy-policy':'Account/privacyPolicy.html',
        'about-us':'Home/aboutUs.html',
        'contact':'Home/contact.html'
    }
    if name1 == 'account':
        if name2 == 'settings':
            try:
                user = CustomUser.objects.get(username=request.user.username)
            except CustomUser.DoesNotExist:
                return HttpResponseRedirect('/login/') 
            if request.method == 'POST':
                update_user_settings(request.POST,user)
            return render(request,'Account/settings.html',{'user':user})
        else:
            if name2 in pages:
                return render(request,pages[name2])

def custom_404_view(request,exception):
    return render(request,'Account/some_error.html',status=404)