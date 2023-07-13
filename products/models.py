from django.db import models
from accounts.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    SELLING_UNITS = [
        ("piece", "Piece"),
        ("package", "Pack"),
        ("kg", "Kilograms"),
        ("g", "Grams"),
    ]

    seller = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="product_list"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="product_list"
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price_unit = models.CharField(max_length=20, choices=SELLING_UNITS, default="piece")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/")
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    STARS = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    ]

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="review_list"
    )
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="review_list"
    )

    rating = models.CharField(max_length=1, choices=STARS, default="5")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.author} on {self.product.name}"
