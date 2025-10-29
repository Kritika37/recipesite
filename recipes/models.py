from django.db import models

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('Vegetarian', 'Vegetarian'),
        ('Meaty', 'Meaty'),
        ('Fish', 'Fish'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
