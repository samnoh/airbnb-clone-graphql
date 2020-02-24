from .models import User


def resolve_user(root, info, id):
    return User.objects.get(id=id)


def resolve_me(root, info):
    user = info.context.user
    print(user)
    if user.is_authenticated:
        return user
    else:
        raise Exception("You need to be logged in")
