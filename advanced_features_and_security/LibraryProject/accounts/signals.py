from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    if sender.name != 'accounts':
        return

    # Define roles
    roles = ['admin', 'librarian', 'member']
    for role in roles:
        Group.objects.get_or_create(name=role)

    # Add custom permissions (example)
    librarian_group = Group.objects.get(name='librarian')
    member_group = Group.objects.get(name='member')

    # For demonstration: Allow librarian to change and add users
    user_ct = ContentType.objects.get(app_label='accounts', model='customuser')
    change_user_perm = Permission.objects.get(codename='change_customuser', content_type=user_ct)
    add_user_perm = Permission.objects.get(codename='add_customuser', content_type=user_ct)

    librarian_group.permissions.add(change_user_perm, add_user_perm)

