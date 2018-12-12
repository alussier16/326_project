# Title: deep

# Subtitle: Closeknit

# Semester: Fall 2018

# Overview
Our application draws inspiration from other social media platforms like Facebook and Twitter, but instead of overwhelming you with posts from people you barely know, our app is for those you know in real life. We do this through a few key design choices. The biggest thing is that you are only able to send people a friend request if you have their friend code. People's friends codes are private so the only way for you to get their friend code is to ask them in person for it. When someone wants to become friends with another user, they can go to a page to add new friends, we call them "Ties", and enter the user's username and friend code, and if that user exists they will be able to add them as a friend.

The second design choice to keep our social network personal is to limit the number of friends you can have on our platform to 99 so you have to be selective with who you add. We call a user's friends "Ties" on our platform. All your ties are displayed from a Ties page and there is a link to each of your friends profile pages from the Ties page. If you add a new Tie, those users will also appear here, and anyone you cut ties with will no longer appear on this page. From the Ties page you are able to access a separate page from which you can add new Ties.

The final design choice of our application is in how we display posts. A user can make a post from the navbar when on any page. A history of their posts will be visible on their account page and anyone who is friends with them will be able to access their account from the ties page to view a friend's entire post history. From the users main page they are able to see a scrolling feed of their friends posts. Each post can have associated with it reactions and comments from their friends. Each user will be allowed one comment per post. On posts, we didn't want people competing for the number of likes/reactions they can get so instead we only show a progress bar for each reaction showing the proportion of each different reaction a post has received.

Other significant feature include the settings page. From the settings page, people will be able to change their account information such as their username, email, friend code, and password. Settings can be accessed from the navbar by clicking on the gear icon.

Through these core ideas driving our application we hope to innovate on the current state of social media offerings by providing a service that is designed to be personal, private, and closeknit.

# Team Members
* Sivan Myers, sivanmyers
* Vincent Pietropaolo, vpietropaolo
* Julian Killingback, jfkback
* Jordan Sheffield, jesheffie
* Gizem Cicekli, gcicekli
* Andy Lussier, alussier16

# User Interface
[Gizem]
A final up-to-date list/table describing your application’s user interface. This should include the name of the UI view and its purpose. 

You should include a screenshot of each of your UI views.

# Data Model
[Gizem]
A final up-to-date diagram of your data model 
including a brief description of each of the entities in your model and their relationships.

# URL Routes/Mappings
* closeknit/login
This route displays our login view from which users are able to sign in to our platform. If a user tries to access most pages of our application without being logged in, they get redirected here to login.
* closeknit/sign-up
This route displays our sign-up views from where users can create a new account with our platform. It is one of few pages which does not require you to be logged in, since you are creating a new account. When you've entered all the relevant information you can go on to the next page which notifies you your account has been created.
* closeknit/account-created
After a user signs up with our platform by submitting the relevant form they get sent to this url which notifies them their account has been created and prompts them to login.
* closeknit/
This url is used for our default main page which displays new posts from your friends. It requires you be logged in to an account to access since we are unable to display any relevant data without you having an account and being logged in.
* closeknit/ties
This url is used to display our ties view which shows a user all of their friends on our platform.  It requires you be logged in to an account to access since we are unable to display any friend data without you having an account and being logged in.
* closeknit/addfriend
This url is used to display our addfriend and removefriend form which allows you to add a new tie or remove an existing tie on our platform. It requires you be logged in to access as you would need to have an account whose data you are editing to add or remove friends to.
* closeknit/<viewed_account>/account
This url is used to display the specific user account which you are viewing. The url is dependent on the username of the user you are trying to look at which may include your own account, or a friends account. This url requires you be logged in to access to know who is viewing what account, and compile the relevant information.
* closeknit/settings
This url is used to display our settings form which allows a user to edit their account information. It requires you be logged in to access as it edits the account information of the user who is logged in.
* closeknit/add-post
This url displays the view for our form to create a new post on your account. It requires you be logged in to access, as the logged in user is recorded as the author of the post.
* closeknit/logout
When a user logs out of our application from the top navbar or from the settings page they get sent this page, with a link to log back in.

Additionally we have a get-post url which numbers posts and is used within our main page url and account pages to display posts with their associated comment and reaction data.

# Authentication/Authorization
To use our application, you must have an account. Thus if try to access any page of our application without being signed in you will be redirected to login. Once logged in, our application is tailored to your account and displays information relevant to you on each page. Thus on the main page you will see the posts of all of your ties, the Ties page will show all of your current ties and provides a link to add more, and the account page shows your post history. If you are intereseted in editing any of your account settings you can head to the settings page where you able to edit your user account fields. When you're ready to logout, you do this from the navbar under Account.

From the login page at the top you will see a link to signup. From the signup page, it asks you to fill out several fields necessary to create your account such as your name, username, email, friend code and password. The form on the backend uses this data to create a new user and associated UserAccount in the database. Once you've entered the account information and hit submit, it sends you to a page to let you know you've joined Closeknit and provides a link back to the login. Now you will be able to login with your new account!

Each of our UI views is tailored to your account information. Thus all pages require you be logged in to access them. The main page shows you a variety of post data from your friends, as well as their comment and reaction data. Meanwhile the ties page shows your friend data and displays the list of friends of the signed in user. From Ties you are able to access your friends account page to see their post history and you are also able to access your own account page from the navbar. Additionally from the settings page your are able to change any of your account data fields.

# Team Choice
For out team choice we implemented a lazy load functionality that continually loads new posts from your friends on the main page, allowing you to endlessly load new posts until you've seen all your friends posts. We used javascript client side to render the posts as needed, and JSON is used to send data from the server to the client which contains the post data. It works in conjunction with many aspects of our application to do this.

# Conclusion
 A conclusion describing your team’s experience in working on this project. This should include what you learned through the design and implementation process, the difficulties you encountered, what your team would have liked to know before starting the project that would have helped you later, and any other technical hurdles that your team encountered.
