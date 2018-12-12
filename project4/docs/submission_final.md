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
Please refer to the user_interface_screenshots.pdf (https://github.com/sivanmyers/326_project/blob/master/project4/docs/user_interface_screenshots.pdf) under our docs file to view the UI views shown with screenshots and included descriptions.

# Data Model
Our data model consists of four models, a UserAccount, Post, Comment, and Reaction model which we use to great effect to store a variety of different fields. Our UserAccount model has 3 fields, the first is a OneToOne field which is associated with a provided django user model used for authentication. Then the UserAccount model also has a char field for  Friend Code. Lastly the UserAccount has a ManyToMany symmetrical relationship with other UserAccounts because a friend connection is mutual between the two users.

The Post model has 3 fields. The first field is a ForeignKey field to a UserAccount so a UserAccount can have all of their posts related to to their account. The Posts model also has a text field for the text content of a post.  Lastly there is a DateAndTime field to record when the post was created. Currently, the date and time of creation requirement has been removed for our submission in order to create mock data with different dates and times.

The Comment model also has 4 fields associated with it. A ForeignKey field for the post with which the comments is related. A ForeignKey field for the author of the comment. A text field for the text content of the comment, and a DateAndTime field to record a timestamp of when the comment was written, similarly we don't require the actual date and time of creation to allow for the creation of mock data.

Lastly, our reaction model has 4 fields associated with it. A ForeignKey to the post the reaction is associated with. A ForeignKey to the UserAccount which is creating the reaction to a post. A chair field which we use to set the status from an enumeration of 5 different options from no reaction to 4 other possible reactions, and lastly another DateAndTime field for the time the reaction was made, similarly altered for more varied mock data in this submission.

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
Our team learned a lot through the design and implementation process. Coming into the class many of us had very little background knowledge on the subject matter and all of us were completely unfamiliar with server side programming and django. Through the design process we learned a lot about collaborating and also communicating specific design ideas and how to create a standardized cohesive design for the platform. Through the implementation of our project we learned all of the subject matters in the class since we had no prior background, and also learned a lot about troubleshooting and working with git for version control. We ran into some bumps along the way with communication and debating the idea and design of our project. Specifically, sometimes decisions early on were made by parts of the group when some people were unable to be present and thus unable to provide their input. We worked to reconcile these differences and try to build a project with added input from everyone. We ran into many implementation challenges along the way, specifically in fixing bugs on our main page and how it displays data, and also in using forms and incorporating them into existing templates. Similarly, we had issues incorporating our team choice aspect into the template we built earlier. Ultimately we were able to overcome those challenges. Before starting the project and each submission, we would have liked to known more how each submission was going to be built on by future submissions because many of the hurdles we ran into came from trying to alter our existing work at the start of each new submission to accomodate the requirements of the problem. We would have liked to try and account for future submissions by incorporating into our design earlier things that would eventually be implemented later.
