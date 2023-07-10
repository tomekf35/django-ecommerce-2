from django.shortcuts import render


def index_page_view(request):
    section = "index"
    return render(request, "core/index.html", {"section": section})


def shop_page_view(request):
    section = "shop"
    return render(request, "core/product_list.html", {"section": section})


def about_page_view(request):
    section = "about"
    return render(request, "core/about.html", {"section": section})


def contact_page_view(request):
    section = "contact"
    return render(request, "core/contact.html", {"section": section})


def vendor_page_view(request):
    section = "vendor"
    return render(request, "core/vendor.html", {"section": section})
