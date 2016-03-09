from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from apps.comments.models import Comments
from apps.cards.models import Cards
from apps.users.models import UserProfile
import ipdb
# Create your views here.


@login_required(login_url='/users/login/')
def comment(request, card_id):
    """Business Logic for Comment."""
    context = {}
    ipdb.set_trace()
    if request.method == 'POST':
        try:
            created_by = request.user
            created_by = UserProfile.objects.get(user=created_by)
            comment = request.POST.get('card_comment')

            comment_info = Comments(
                user_profile=created_by,
                cards=Cards.objects.get(id=card_id),
                comments=comment)

            comment_info.save()
            context = {'success': True, 'message': 'Successfully Saved'}
        except:
            context = {'success': False, 'message': 'Saving failed'}

    context.update(csrf(request))
    return HttpResponseRedirect("/cards/%s/" % card_id, context)