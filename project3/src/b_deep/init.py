import random, pytz
from django.contrib.auth.models import User
from faker import Faker
from django.contrib.auth.models import Group
from closeknit.models import UserAccount, Post, Comment, Reaction

fake = Faker()

users = []
test_users, created = Group.objects.get_or_create(name='test_users')

test_user = User(first_name="Vincent",last_name="Pietropaolo",email="vpietropaolo@umass.edu",username="vpietropaolo",is_superuser=False)
test_user.set_password("umass326")
test_user.save()
test_users.user_set.add(test_user)
users.append(test_user)
test_user = User(first_name="Andy",last_name="Lussier",email="alussier@umass.edu",username="alussier",is_superuser=False)
test_user.set_password("umass326")
test_user.save()
test_users.user_set.add(test_user)
users.append(test_user)
test_user = User(first_name="Sivan",last_name="Myers",email="smyers@umass.edu",username="smyers",is_superuser=False)
test_user.set_password("umass326")
test_user.save()
test_users.user_set.add(test_user)
users.append(test_user)
test_user = User(first_name="Julian",last_name="Killingback",email="jkillingback@umass.edu",username="jkillingback",is_superuser=False)
test_user.set_password("umass326")
test_user.save()
users.append(test_user)
test_user = User(first_name="Gizem",last_name="Cizeckli",email="gcizeckli@umass.edu",username="gcizeckli",is_superuser=False)
test_user.set_password("umass326")
test_user.save()
test_users.user_set.add(test_user)
users.append(test_user)
test_user = User(first_name="Jordan",last_name="Sheffield",email="jsheffield@umass.edu",username="jsheffield",is_superuser=False)
test_user.set_password("umass326")
test_user.save()
test_users.user_set.add(test_user)
users.append(test_user)

'''
for i in range(1,25):
    u_fname = fake.first_name()
    u_lname = fake.last_name()
    u_email = fake.email()
    u_username = fake.user_name()
    u_password = fake.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
    user = User(first_name=u_fname,last_name=u_lname,email=u_email,username=u_username,password=u_password,is_superuser=False)
    user.save()
    users.append(user)
'''
user_accounts = []
for u in users:
    u_frcode = "christmaself"
    user_account = UserAccount(user=u,friend_code=u_frcode)
    user_account.save()
    user_accounts.append(user_account)

user_accounts[1].friend_code="zoomass"
for u in user_accounts:
    new_friends = random.sample(user_accounts, 3)
    u.friends.set(new_friends)
    u.save()

posts = []
p_author = user_accounts[0]
p_text = "The best way to spread Christmas Cheer, is singing loud for all to hear."
p_timestamp = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=pytz.utc)
post = Post(author=p_author, text_content=p_text, time_stamp=p_timestamp)
post.save()
posts.append(post)
p_author = user_accounts[0]
p_text = "I planned out our whole day: First, we'll make snow angels for two hours, and then we'll go ice skating, and then we'll eat a whole roll of Toll House cookie dough as fast as we can."
p_timestamp = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=pytz.utc)
post = Post(author=p_author, text_content=p_text, time_stamp=p_timestamp)
post.save()
posts.append(post)
p_author = user_accounts[0]
p_text = "Buddy the Elf, what's your favorite color?"
p_timestamp = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=pytz.utc)
post = Post(author=p_author, text_content=p_text, time_stamp=p_timestamp)
post.save()
posts.append(post)
p_author = user_accounts[1]
p_text = "If you can sing alone, you sing in front of other people. There's no difference."
p_timestamp = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=pytz.utc)
post = Post(author=p_author, text_content=p_text, time_stamp=p_timestamp)
post.save()
posts.append(post)
p_author = user_accounts[1]
p_text = "I am a cotton-headed ninny-muggins!"
p_timestamp = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=pytz.utc)
post = Post(author=p_author, text_content=p_text, time_stamp=p_timestamp)
post.save()
posts.append(post)
p_author = user_accounts[1]
p_text = "I just like to smile; smiling's my favorite."
p_timestamp = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=pytz.utc)
post = Post(author=p_author, text_content=p_text, time_stamp=p_timestamp)
post.save()
posts.append(post)
p_author = user_accounts[1]
p_text = "So, Buddy, how'd you sleep?" "Great! I got a full 40 minutes!"
p_timestamp = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=pytz.utc)
post = Post(author=p_author, text_content=p_text, time_stamp=p_timestamp)
post.save()
posts.append(post)
p_author = user_accounts[2]
p_text = "So, good news, I saw a dog today."
p_timestamp = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=pytz.utc)
post = Post(author=p_author, text_content=p_text, time_stamp=p_timestamp)
post.save()
posts.append(post)
p_author = user_accounts[2]
p_text = "We elves try to stick to the four main food groups: candy, candy canes, candy corns, and syrup."
p_timestamp = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=pytz.utc)
post = Post(author=p_author, text_content=p_text, time_stamp=p_timestamp)
post.save()
posts.append(post)
p_author = user_accounts[3]
p_text = "Of course you're not an elf. You're 6-foot-3 and had a beard since you were 15."
p_timestamp = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=pytz.utc)
post = Post(author=p_author, text_content=p_text, time_stamp=p_timestamp)
post.save()
posts.append(post)
p_author = user_accounts[3]
p_text = "I'm sorry I ruined your lives and crammed 11 cookies into the VCR."
p_timestamp = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=pytz.utc)
post = Post(author=p_author, text_content=p_text, time_stamp=p_timestamp)
post.save()
posts.append(post)
p_author = user_accounts[3]
p_text = "Son of a nutcracker!"
p_timestamp = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=pytz.utc)
post = Post(author=p_author, text_content=p_text, time_stamp=p_timestamp)
post.save()
posts.append(post)
p_author = user_accounts[3]
p_text = "How'd you like to be dead, huh? Ho, ho, just kidding."
p_timestamp = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=pytz.utc)
post = Post(author=p_author, text_content=p_text, time_stamp=p_timestamp)
post.save()
posts.append(post)
p_author = user_accounts[4]
p_text = "I passed through the seven levels of the Candy Cane forest, through the sea of swirly-twirly gum drops, and then I walked through the Lincoln Tunnel."
p_timestamp = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=pytz.utc)
post = Post(author=p_author, text_content=p_text, time_stamp=p_timestamp)
post.save()
posts.append(post)
p_author = user_accounts[4]
p_text = "Have you seen these toilets? They're ginormous!"
p_timestamp = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=pytz.utc)
post = Post(author=p_author, text_content=p_text, time_stamp=p_timestamp)
post.save()
posts.append(post)
p_author = user_accounts[4]
p_text = "You sit on a throne of lies!"
p_timestamp = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=pytz.utc)
post = Post(author=p_author, text_content=p_text, time_stamp=p_timestamp)
post.save()
posts.append(post)
p_author = user_accounts[5]
p_text = "This place reminds me of Santa's workshop… except it smells like mushrooms and everyone looks like they want to hurt me."
p_timestamp = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=pytz.utc)
post = Post(author=p_author, text_content=p_text, time_stamp=p_timestamp)
post.save()
posts.append(post)
p_author = user_accounts[5]
p_text = "I'm singing, I'm in a store and I'm siiiiiingiiiiing! I'm in a store and I'm siiiiiingiiiiing!"
p_timestamp = fake.date_time_between(start_date="-1y", end_date="now", tzinfo=pytz.utc)
post = Post(author=p_author, text_content=p_text, time_stamp=p_timestamp)
post.save()
posts.append(post)
'''
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
'''
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
