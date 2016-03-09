"""Adimin configuration."""
from django.contrib import admin
from apps.cards.models import Cards

# Register your models here.


class CardsAdmin(admin.ModelAdmin):
    """Customising admin view of Cards class."""

    '''Displaying all the fields in admin in order.'''
    # fields = ['card_title', 'card_description', 'card_hero_image']

    '''Displaying all the fields in admin in different sections.'''
    readonly_fields = ['card_created_on', 'user_profile']
    fieldsets = [
        ('User Information', {'fields': ['user_profile']}),
        ('Card Information', {'fields': ['card_title', 'card_description', 'card_hero_image']}),
        ('Date information', {'fields': ['card_created_on'], 'classes': ['collapse']}),
    ]

    list_display = ['card_title', 'user_profile', 'card_created_on']
    list_filter = ['card_created_on']
    search_fields = ['card_title', 'user_profile__name']

    class Meta:
        """Information of this class."""

        model = Cards

admin.site.register(Cards, CardsAdmin)
