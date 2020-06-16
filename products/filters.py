import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    manufacturer = django_filters.AllValuesFilter(
        field_name="manufacturer"
    )
    make = django_filters.AllValuesFilter(
        field_name="make"
    )
    model = django_filters.AllValuesFilter(
        field_name="model"
    )

    o = django_filters.OrderingFilter(
        fields={
            ('build_year', 'build_year'),
            ('price', 'price')
        }
    )

    class Meta:
        model = Product
        fields = ['manufacturer', 'make', 'model']
