from .models import Category

# context processor useful for accessing it in template(globally)
# alwayas return dict 
def menu_links(request):
    links = Category.objects.all()
    return dict(links = links)