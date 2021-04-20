from .models import Trains

import django_filters

class TrainsFilter(django_filters.FilterSet):
    class Meta:
        model = Trains
        fields = ['source','destination','types','date']
      
