from orders.models import Cart
from core.models import Category
from home.models import Title
from footer.models import Footer
def shop(request):
    footer = Footer.objects.first()
    title = Title.objects.first()
    user = request.user
    cart = None
    items = None
    if user.is_authenticated:
        cart , created = Cart.objects.get_or_create(
            user = user,
            closed = False,
        )
        items = cart.items.all()
    root_cats = Category.objects.filter(level=0)
    # categories = Category.objects.all()
    
    kwargs = {
        'root_cats': root_cats,
        'cart':cart,
        'items':items,
        'site_title':title,
        'footer':footer,
    }
    return kwargs