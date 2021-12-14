from django.shortcuts import render, redirect
from .models import Category, Photo

def gallery(request):

    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()

    else:
        photos = Photo.objects.filter(category__name=category)
    name = request.GET.get('name')
    categories = Category.objects.all()
    context = { 'categories' : categories, 'photos': photos, 'name': name }
    return render(request, 'album/gallery.html' , context)

def viewPhoto(request, pk):
    name = request.GET.get('name')
    photo = Photo.objects.get(id=pk)    
    categories = Category.objects.all()
    return render(request, 'album/photo.html', {'photo': photo, 'categories': categories, 'name': name})


def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none' :
            category = Category.objects.get(id=data['category'])

        if data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])

        else:
            category = None

        photo = Photo.objects.create(
            # name = data['name'],
            category = category,
            description=data['description'],
            image = image,
        )

        return redirect('gallery')

    context = { 'categories' : categories }
    return render(request, 'album/add.html' , context)
