from django.shortcuts import render


def index_page_view(request):
    return render(request, "core/index.html")


def shop_page_view(request):
    return render(request, "core/product_list.html")


def about_page_view(request):
    return render(request, "core/about.html")


def contact_page_view(request):
    return render(request, "core/contact.html")


def vendor_page_view(request):
    return render(request, "core/vendor.html")
