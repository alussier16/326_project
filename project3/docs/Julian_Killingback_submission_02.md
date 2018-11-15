I worked on many aspects of this submission. Specifically I helped to come up with the general model 
for how users and their subsequent posts would be modeled. I further helped by breaking up the project 
requirements into individual chunks and distributed them to the various members of the team based on what
parts they were interested in. To help the data modelling team I made an early data model for them to use as a base line. 

I additionally setup the template, static, and template tags folders for team use. I built the base template that 
imported all necessary css, fonts, javascript, and images from the static folder. Using the base template I then expanded 
on it to create a navbar template which would switch the active page in the navbar based on the passed in page variable. 
In addition I added a settings icon that appears only when on your account page or the settings page. 

Lastly I was the first to build a template for one of our pages, which had the correct URL mapping and worked 
with mock data from the views file. This allowed my team members to look at my work as an example for how to 
implement templates with the correct URL mapping and incorporating mock data. This template populates the main page 
with posts using the posts template. It iterates through passed in list of post variables and finds the associated 
comments and reactions. While also correctly linking to the accounts of commenters and posters. Additionally 
I made a filter that returns the reactions as a percentage of the largest reaction amount. The posts template 
is also used in the account page. I also built out two new UI pages that we realized would create a better user experience.
These were the add friend page and the settings page which both display mock data.  
