from django.shortcuts import render, redirect
from product.models import Product, Category
from django.db.models import Q
from django.contrib.auth import login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

def index(request):
    products = Product.objects.all()[0:10]
    return render(request, 'core/index.html', {'products': products })


def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    get_active_category = request.GET.get('category', '')
    if get_active_category:
        products = products.filter(category__slug=get_active_category)

    query = request.GET.get('query', '')

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))


    context = {
        'categories': categories,
        'products': products,
        'get_active_category': get_active_category
    }

    return render(request, 'core/shop.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('/')
        
    else:
        form = SignUpForm()

    return render(request, 'core/signup.html', {'form': form})



@login_required
def account(request):
    return render(request, 'core/account.html')


@login_required
def edit_account(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.save()

        return redirect('account')
    return render(request, 'core/edit_account.html')