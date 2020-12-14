from django.shortcuts import render


from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from  django.http import JsonResponse
from  django.views.decorators.http import require_POST
from  common.decorators import ajax_required
from .models import Contact
from django.contrib.auth.decorators import login_required


@ajax_required
@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(
                    user_from=request.user, user_to=user)
            else:
                Contact.objects.filter(user_from=request.user,
                                       user_to=user).delete()
            return JsonResponse({'status': 'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'error'})
    return JsonResponse({'status': 'error'})



@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)

    return render(request, 'account/list.html',
                  {'section': 'people',
                   'users': users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User,
                             username=username,
                             is_active=True)

    return render(request,
                  'account/detail.html',
                  {'section': 'people',
                   'user': user})
