from django.apps import apps


def get_default_category():
    category_class = apps.get_model('products.category')
    return category_class.objects.first().id
