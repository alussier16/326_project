# Team Overview

* Sivan Myers, sivanmyers
* Vincent Pietropaolo, vpietropaolo
* Julian Killingback, jfkback
* Jordan Sheffield, jesheffie
* Gizem Cicekli, gcicekli
* Andy Lussier, alussier16

# Overview
Our application draws inspiration from other social media platforms like Facebook and Twitter, but instead of overwhelming you with posts from people you barely know, our app is for those you know in real life. We do this through a few key design choices. The biggest thing is that you are only able to send people a friend request if you have their friend code. People's friends codes are private so the only way for you to get their friend code is to ask them in person for it. When someone wants to become friends with another user, they can go to a page to add new friends, we call them "Ties", and enter the user's username and friend code, and if that user exists they will be able to add them as a friend.

The second design choice to keep our social network personal is to limit the number of friends you can have on our platform to 99 so you have to be selective with who you add. We call a user's friends "Ties" on our platform. All your ties are displayed from a Ties page and there is a link to each of your friends profile pages from the Ties page. If you add a new Tie, those users will also appear here, and anyone you cut ties with will no longer appear on this page. From the Ties page you are able to access a separate page from which you can add new Ties.

The final design choice of our application is in how we display posts. A user can make a post from the navbar when on any page. A history of their posts will be visible on their account page and anyone who is friends with them will be able to access their account from the ties page to view a friend's entire post history. From the users main page they are able to see a scrolling feed of their friends posts. Each post can have associated with it reactions and comments from their friends. Each user will be allowed one comment per post and a user will only see the comments on their friends posts of people they currently have a mutual connection to in the finished product. On posts, we didn't want people competing for the number of likes/reactions they can get so instead we only show a progress bar for each reaction showing the proportion of each different reaction a post has received.

Other significant feature include the settings page. From the settings page, people will be able to change their account information such as their username, email, friend code, and password. Settings can be accessed from the navbar by clicking on the gear icon.

For this submission we have not made any substanative changes to our proposed idea. Instead, we worked on implementing login and logout, and the forms, all of which are central to the functionality of our application.

# Video Link

# Design Overview
To use our application, you must have an account. Thus if try to access any page of our application without being signed in you will be redirected to login. Once logged in, our application is tailored to your account and displays information relevant to you on each page. Thus on the main page you will see the posts of all of your ties, the Ties page will show all of your current ties and provides a link to add more, and the account page shows your post history. If you are intereseted in editing any of your account settings you can head to the settings page where you able to edit your user account fields. When you're ready to logout, you also do this from the Settings page at the bottom where there is a clearly labeled Logout button.

There are many ways to interact with our application. First and foremost, you are able to create new users. From the login page at the top you will see a link to signup. From the signup page, it asks you to fill out several fields necessary to create your account such as your name, username, email, friend code and password. The form on the backend uses this data to create a new user and associated UserAccount in the database. Once you've entered the account information and hit submit, it sends you to a page to let you know you've joined Closeknit and provides a link back to the login. Now you will be able to login with your new account!

After you've signed in, you'll be taken to the home page. Here is where you'll be able to see all the posts by your friends and also interact with them. You can click on the Comment button next to any post and fill out your comment in the comment form. When you hit the comment button your message is now visible in the comments section of the post. Additionally, from the comments section you are also able to create and modify reactions to the post. Press any of the emoticon icons to create a new reaction on the post. If at any time you want to change your reaction you just have to go back and select a different one. Additionally, from the navbar you can click on post which will take you to a post form where you can write your post and then post it. Then you will be able to see your post history, including your new post, from your accounts page.

If you want to add new friends, you can go to the ties page, and then click on the "Add Friend" link. This takes you to a form where you can modify your Ties by adding a new friend. You'll just need to know their username and their private friend code they will need to give you personally, then you can enter the information, and if everything matches they'll be added as a Tie and you can go back to the Ties page and checkout your new friend.

Lastly, you can interact with our application and modify any of your account information from the settings page, accessible from the navbar. [TODO Gizem]

# Problems/Successes
Our team communicated fairly well without many hiccups. Due to Thanksgiving break in the middle of the project, we layed out much of the responsibilities beforehand, and communicated sparsely over the actual break. We discussed the submission amply beforehand and this was very successful to figuring out specific responsibilities and delegating the work evenly. This meant communication was clear for everyone beforehand, but during break we did not communicate much which was an issue specific to the circumstances of this submission and will not be an issue for the next submission.

Implementation was a bit bumpier. Figuring out how to implement forms which fit within our templates and how they worked together was difficult and we had a lot of issues implementing them. Due to the break, we were unable to help each other problem solve as much as we could have because the specific issues and error we were facing were difficult to explain what are problems were over text. Ultimately though, we were able to implement the forms we wanted to and implementing user authentication went smoothly. For the next submission, collaborating to solve implementation errors will be easier because we will be here in person to help each other trouble shoot.

# Team Choice
For out team choice we intend to implement a lazy load functionality that will continually load new posts from your friends on the main page, allowing you to endlessly load new posts. [TODO Julian]
