import django_filters
from django_filters import CharFilter


from .models import Claim


class ClaimFilter(django_filters.FilterSet):
    sender = CharFilter(field_name='sender', lookup_expr="icontains", label='Sender')

    class Meta:
        model = Claim
        fields = ['sender']
