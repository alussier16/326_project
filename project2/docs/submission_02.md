# Team Overview

* Sivan Myers, sivanmyers
* Vincent Pietropaolo, vpietropaolo
* Julian Killingback, jfkback
* Jordan Sheffield, jesheffie
* Gizem Cicekli, gcicekli
* Andy Lussier, alussier16

# Overview

Our application draws inspiration from other social media platforms like Facebook and Twitter, but instead of overwhelming you with posts from people you barely know our, our app is for those you know in real life. We do this through a few key design choices. The biggest thing is that you are only able to send people a friend request if you have their friend code. People's friends codes are private so the only way for you to get their friend code is to ask them in person for it. One big change since our last submission is that we've added another UI page to our application from which users can add other users. Now when someone wants to become friends with another user, they can go to this page and enter the user's username and friend code, and if that user exists they will be able to send them a friend request.

The second design choice to keep our social network personal is to limit the number of friends you can have on our platform to 99 so you have to be selective with who you add. We call a user's friends "Ties" on our platform. Since the last submission, we have overhauled the design of the Ties UI page, now all your ties are displayed and there is a link to each of your friends profile pages from the Ties page. If you add a new Tie, those users will also appear here, and anyone you cut ties with will no longer appear on this page.

The final design choice of our application is in how we display posts. A user can make a post from the navbar when on any page. A history of their posts will be visible on their account page and anyone who is friends with them will be able to access their account from the ties page to view a friend's entire post history. From the users main page they are able to see a scrolling feed of their friends posts. Each post can have associated with it reactions and comments from their friends. Each user is allowed one comment per post and a user will only see the comments on their friends posts of people they currently have a mutual connection to. On posts, we didn't want people competing for the number of likes/reactions they can get so instead we only show a progress bar for each reaction showing the proportion of each different reaction a post has received.

Other significant changes since our last submission include adding a settings UI page. From the settings page, people will be able to change their account information such as their username, email, friend code, and password. In addition we've also done an overhaul of our websites look, making stylistic font and color changes throughout the site. We've also edited the navbar to include a settings icon, on the account page, which links to the new setting page.

# Video Link
[Include Link Here]

# Design Overview
Our data model consists of four models, a UserAccount, Post, Comment, and Reaction model which we use to great effect to store a variety of different fields. Our UserAccount model has 7 fields, 5 of the fields, First Name, Last Name, Username, Friend Code, and Password are all character fields which we limit in size to appropriate lengths for each. We have one EmailField for the users email. Lastly the UserAccount has a ManyToMany symmetrical relationship with other UserAccounts because a friend connection is mutual between the two users. At this time, we do not limit the number of friends a UserAccount can have because we intend to do this programmatically later when a user tries to add a friend which would exceed the limit. 

The Post model has 4 fields. The first field is a ForeignKey field to a UserAccount so a UserAccount can have all of their posts related to to their account. The Posts model also has a text field for the text content of a post. There is also an image field for a possible image to be included in the post. Lastly there is a DateAndTime field to record when the post was created. Currently, the date and time of creation requirement has been removed for our submission in order to create mock data with different dates and times.

The Comment model also has 4 fields associated with it. A ForeignKey field for the post with which the comments is related. A ForeignKey field for the author of the comment. A text field for the text content of the comment, and a DateAndTime field to record a timestamp of when the comment was written, similarly we don't require the actual date and time of creation to allow for the creation of mock data.

Lastly, our reaction model has 4 fields associated with it. A ForeignKey to the post the reaction is associated with. A ForeignKey to the UserAccount which is creating the reaction to a post. A chair field which we use to set the status from an enumeration of 5 different options from no reaction to 4 other possible reactions, and lastly another DateAndTime field for the time the reaction was made, similarly altered for more varied mock data in this submission.

[the important URL routes (Vincent)]

We've implemented UI views for the 5 main UI pages of our application. To keep it consistent we pass along the UserAccount identified as "user=UserAccount.objects.get(pk=1)" as context for all of our views into the templates so the information on each is consistent across pages and the site can be viewed as if from one users perspective. The "Settings" and "Add Friend" page only have the user passed along as contextt which we use in the template on the settings page to render the current account information to be adjusted, and on the add friends page we use it to render the user's username and friend code.

[Navbar and Posts UI view and template (Julian)]

We also implemented a UI view for the account page, which passes along the current user, if a user is viewing their own account page, and the useraccount of another another user based on their username if someone is viewing a friend's account page. We pass this along as context to render the account page template. We also pass along the given UserAccounts posts as context so we can display their post history in order.

Lastly, we implemented a UI view for the ties page which passes along the user and all of their friends associated from the UserAccount friends ManyToMany field as context. This information is used to display the user themself on the ties page template at the top, and iterate through the users friends and render them as part of a table to display all the user's friends and links to their accounts. This is so a user can access all their friend's account pages from the ties page.

***From Spec***
A design overview of your data model as implemented in Django, 
[the important URL routes (Vincent)], and the implemented UI views. Please provide enough detail to demonstrate your team’s understanding of the material.

# Problems/Successes

Our team had a good amount of success when it came to communication. We were able to meet early on in the project to discuss a roadmap for the project and gain an understanding of what needed to be done first for other things to be completed later. We also discussed and divided up responsibilities in a clear manner and ensured that no one was confused about what their tasks were. The problems we encountered is that communication tended to lag towards the end of project as people's schedules became busy and we were not able to have a full team meeting. Also, we had some trouble with communicating about what people were submitting to the GitHub repository and how that worked on other people's machines, which I'll talk about further in implementation difficulties.

We had a lot of success implementing the project. Between different significant tasks we had someone go in and make sure everything done so far was working as intended and this helped when people moved on to the next step. We also merged features back into our master branch after they were complete and working, and this smoothed the overall process too. Our communication about how interrelated parts needed to be implemented for other portions to work also helped to smooth the implementation problems. Some of the issues of implementation came with trouble shooting different errors because people had limited time to meet in person, other than in class, helping each other out to troubleshoot different issues individuals were having was a slower than expected process. Also because the work was divided so different people would focus on different specific tasks there was sometimes difficulty in incorporating the work done by one person into other people's work. This especially happened after new features were added to github and then other people would have errors on their machines when they pulled and tried to work with the updated repository and as a group we were not able to troubleshoot face to face.

For the next submission, I think we can work on ironing out the kinks in how the group functions. Overall, we were fairly successful in communicating and implementing this project and in the future we just need to make slight improvements to increase communication a little more, and help each other incorporate features other people have implemented into our own work. We can do this by better explaining what we are doing as we are doing it so everyone is up to date on what people are working on, and the entire group understands it.
