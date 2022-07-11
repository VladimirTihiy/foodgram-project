#import pdb

from recipe.models import Recipe 
from django_filters.rest_framework import (
    AllValuesMultipleFilter,
    BooleanFilter,
    CharFilter,
    FilterSet
)
class RecipeFilter(FilterSet):
    #tags = CharFilter(method='get_tags')
    is_favorited = BooleanFilter(method='get_is_favorited')
    class Meta:
        model = Recipe
        fields = ('author',)
    #def get_is_favorited(self, queryset, name, value):
    #    if not value:
    #        return queryset
    #    favorites = self.request.user.favorite.all()
    #    return queryset.filter(
    #        pk__in=(favorite.recipe.pk for favorite in favorites)
    #    )




    def get_is_favorited(self, queryset, name, value):
        #pdb.set_trace()
        if not value:
            return queryset
        favorites = self.request.user.favorite.all()
        return queryset.filter(
            pk__in=(favorite.favorite.pk for favorite in favorites)
        )
