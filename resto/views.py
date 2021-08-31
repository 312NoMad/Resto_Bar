from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm

#
# def product_detail(request, id, slug):
#     product = get_object_or_404(Products,
#                                 id=id,
#                                 slug=slug,
#                                 available=True)
#     cart_product_form = CartAddProductForm()
#     return render(request, 'shop/product/detail.html', {'product': product,
#                                                         'cart_product_form': cart_product_form})


