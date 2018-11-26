import random, pytz
from django.contrib.auth.models import User
from faker import Faker
from closeknit.models import UserAccount, Post, Comment, Reaction

fake = Faker()

users = []
for i in range(1,25):
    u_fname = fake.first_name()
    u_lname = fake.last_name()
    u_email = fake.email()
    u_username = fake.user_name()
    u_password = fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
    user = User(first_name=u_fname,last_name=u_lname,email=u_email,username=u_username,password=u_password,is_superuser=False)
    user.save()
    users.append(user)

user_accounts = []
for u in users:
    u_frcode = fake.ean(length=8)
    user_account = UserAccount(user=u,friend_code=u_frcode)
    user_account.save()
    user_accounts.append(user_account)

for u in user_accounts:
    new_friends = random.sample(user_accounts, fake.random_int(1,20))
    u.friends.set(new_friends)
    u.save()

posts = []
for u in user_accounts:
    for i in range(0,fake.random_int(1,5)):
        p_author = u
        p_text = fake.text(max_nb_chars=250, ext_word_list=None)
        p_timestamp = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=pytz.utc)
        post = Post(author=p_author, text_content=p_text, time_stamp=p_timestamp)
        post.save()
        posts.append(post)

comments = []
for p in posts:
    for i in range(1,4):
        c_content = fake.text(max_nb_chars=50, ext_word_list=None)
        c_post = p
        c_author = random.choice(user_accounts)
        c_timestamp = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=pytz.utc)
        comment = Comment(content=c_content,post=c_post,author=c_author,time_stamp=c_timestamp)
        comment.save()
        comments.append(comment)

reactions = []
for p in posts:
    for i in range(1,fake.random_int(1,6)):
        r_post = p
        r_user = random.choice(user_accounts)
        r_timestamp = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=pytz.utc)
        r_status = fake.random_int(0,4)
        reaction = Reaction(post=r_post, user=r_user, time_stamp=r_timestamp,status=r_status)
        reaction.save()
        reactions.append(reaction)

username = "admin"
password = "admin"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
admin_account = UserAccount(user=adminuser)
admin_account.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
message = f"""
====================================================================
The database has been setup with the following credentials:

  username: admin
  password: admin
  email: admin@326.edu

You will need to use the username admin and password admin
to login to the administrative webapp in Django.

Please visit http://localhost:8080/admin to login to the admin app.
Run the django server with:

  $ python3 manage.py runserver 0.0.0.0:8080"
====================================================================
"""
print(message)
