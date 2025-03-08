
class User:
    def __init__(self, name):
        self.name = name
        self.is_user_logged =False

def is_authentic_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_user_logged == True:
            function(args[0])
        return wrapper

@is_authentic_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new bog post.")

new_user = User("SIVA")
create_blog_post(new_user)

