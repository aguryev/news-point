
def create_groups(sender, **kwargs):
    #
    # creates thre default groups: users, editors, admins
    #
    
    from django.contrib.auth.models import Group
    group_app, created = Group.objects.get_or_create(name='users')
    group_app, created = Group.objects.get_or_create(name='editors')
    group_app, created = Group.objects.get_or_create(name='admins')