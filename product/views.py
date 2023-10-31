from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Review
from cart.cart import Cart
from .forms import AddToCartForm
from django.contrib import messages

def product(request, slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=slug)

    form = AddToCartForm()

    if request.method == 'POST':
        rating = request.POST.get('rating', 3)
        content = request.POST.get('content', '')

        if content:
            reviews = Review.objects.filter(created_by=request.user, product=product)

            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.content = content
                review.save()
            else:
                review = Review.objects.create(
                    product=product,
                    rating = rating,
                    content = content,
                    created_by = request.user
                )
            messages.success(request, 'Your review has been submmitted successfully')

        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)
            messages.success(request, 'The product has been added to cart')

        return redirect('product', slug=slug)

    return render(request, 'product/product.html', {'product':product, 'form': form})


