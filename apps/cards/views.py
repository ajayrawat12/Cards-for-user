"""Views file, for all business logic."""
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from apps.cards.models import Cards
from apps.users.models import UserProfile


def all_cards(request):
    """Display all cards."""
    cards = Cards.objects.all()
    return render_to_response('all_cards.html', {'cards': cards})


def view_card(request, card_id=1):
    """Display specific card."""
    context = {}
    context = {'cards': Cards.objects.get(id=card_id), }
    context.update(csrf(request))
    return render_to_response('view_card.html', context)


@login_required(login_url='/users/login/')
def create_card(request):
    """Creating new cards."""
    context = {}
    if request.method == 'POST':
        try:

            card_title = request.POST.get('card_title')
            card_description = request.POST.get('card_description')
            card_picture = request.POST.get('card_picture')
            created_by = request.user
            created_by = UserProfile.objects.get(user=created_by)

            card_info = Cards(
                card_title=card_title,
                user_profile=created_by,
                card_description=card_description,
                card_hero_image=card_picture)

            card_info.save()
            context = {'success': True, 'message': 'Successfully Saved'}
        except:
            context = {'success': False, 'message': 'Saving failed', 'full_name': request.user.username}

    context.update(csrf(request))
    return render_to_response("create_card.html", context)
