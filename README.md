# Fit For Life - Milestone 4 Project 
Fit For Life is an e-commerce website built using Django and Stripe. Fit For Life sells premium branded products and a membership which allows registered users to view fitness plans and receive generous member discount on our  exclusive range of specialised products. Fit For Life caters for all individuals with a selection of fitness plans from muscle building to weightloss to general fitness. The plans can be viewed on the website once a user purchases a membership. Both non-registered and registered users can view and purchase products such as protein bars and shakes. Registered users will have a profile where they can view their membership plan and previous orders. The website can be viewed [here](https://django-ffl-app.herokuapp.com/).

# UX
## Project Goals
Create a fully fucnctional website using Django and Stripe that allows user to register to avail of a benefit while also allowing non-registered users the option to browse the site and make purchases. The overall goal for this website is to allow visitors to purchase products and encourage them to purchase membership by offering a significant discount and exclusive plans. Registered users have their own profile where they can view their membership details, view past orders and save delivery information. The design of this website was to keep it very simple yet eye-catching by incorporating in the bright orange which contrasts nicely with the black and grey used through-out the site.  I created a logo for the website and placed it on all the products as well as using the same orange colour in the product images to keep everything in theme. I used the Beba Neue font from
Google Fonts which I believe suits the fitness industry. 

## User Stories
The site was designed with three users in mind: admin, registered user and non-registered user.
### Admin User 
* As a site Admin I want to be able to upload new products and plans
* As an admin I want to be able to edit/update products and plans.
* As an admin I want the ability to delete products/plans.
### Registered User
* As a registered user I want to be able to login.
* As a registered user I want to be able to update and save my information.
* As a registered user I want to be able to see my previous purchases.
* As a registered user I want to be able to view fitness plans.
* As a registered user I want to be able to buy products with a member discount.
### Non-registered User 
* As a non-registered user I want to be able to Navigate to different pages of the website .
* As a non-registered user I want to be able to browse products.
* As a non-registered user I want to be able to buy products.
* As a non-registered user I want to be able to search for products.

## Mock-Ups 
I created the Mock-Ups for the website by using Figma. There are Mock-ups for all devices in the following [folder]. Please see the main pages below.
#### Products page
![Products Page](/Readme/MockUps/FFLMocupAllProductsPage.jpg) 
#### Individual Product page
![Individual Products Page](/Readme/MockUps/FFLMockupProductPage.jpg)
#### Profile page
![Profile Page](/Readme/MockUps/FFLMockupProfilePage.jpg)
#### Plans page page
![Plans Page](/Readme/MockUps/FFLMochupPlansPage.jpg)

# Features
Customer Facing Pages: Fit For Life consists of a Homepage, products page, Individual Products Page, Plans Page, Plan Workout Page, Shopping Cart Page, Checkout Page, About Page and Profile page. The website is fully responsive.
Admin Facing Pages: In addition to the user facing pages, an admin or superuser has access to a number of specific pages to assist administartion of the site. Access is also provided to the Django provided administration interface for lower level control of data.
## Site Elements
### NavBar
This responsive  feature allows users to move from page to page. When a user is logged in it displays an option to visit a page called " MyProfile". There is also a link to "Logout" if a user is logged in. In the case that no user is logged in the NavBar simply displays a "Login/Register" Tab. For Mobile and Tablet devices -  a hamburger menu on the top-left expands a menu with links to all of the main pages. The navbar stays fixed at the top of each page for easy navigation at all times.
### Forms
Django Crsipy Forms were used for the majority of forms on Fit For Life; support for these was provided by the crispy forms app and was installed using the following command - pip3 install django-crispy-forms. These forms allow users to submit their data and it then gets stored in the database or sent to email associated with the website. 
### Footer
The Footer has links to the associated social media pages along with the credits for the web designer.
### Home Page
The home page displays a landing image under the NavBar. This is a striking image used to grab a website visitors attention. An image of a gym is used which fits in nicely with the products for sale on the website. There is a button which allows visitors to access the "about" page to learn more about the brand and website. The next section of the home page gives visitors a quick overview of the type of products for sale.
### Products Page
The products page displays all products for sale on Fit For Life - this can be broken down into catagories in the navbar. 
* Pagination is implemented in this page so the page is not overloaded with products. 
* Each product card has a button that brings a user to an Individual product page which displays more detail about the product and allows the user add the product to their cart. 
### Plans Page 
The plans page displays three cards, one for each different style of plan: weightloss, muscle building and cardio. Javascript is used on the card to display some details on the plan when the card is hovered over. There is a see more button which allows users to see each plan workout if they are a registered member. 
### Plan Workout Page
This page displays serveral cards. Each card is a detailed how-to guide on an individual excercise. There is also an image relating to the excercise on each card. It is important to note that only registered users who have purchased a membership can view this page. 
The workouts are created as seperate entries in a SQL table so that they can be assigned to one or more workout plans.
### Profile Page 
Registered users will have the option to view their profile page. This page will display their details (name, username etc), allow them to save shipping address details and to view their previous order details. 

### About Page
Provides information about our site and a contact form.

### Stripe 
#### Integrating Stripe
* [Stripe Documentation](https://stripe.com/docs/payments/accept-a-payment?integration=elements)
Stripe works with what are called payment intents. The process will be that when a user clicks a link on the checkout page the checkout view will begin a series of transactions with Stripe. We exchange the following intents:
* balance.available
* payment_intent.succeeded
* charge.succeeded

We only confirm the order if the payment_intent from Stripe is confirmed as sucessful from Stripe. This is done using a webhook (see below) on the Fit For Life site which listens for the encoded response from the Stripe server.
We are using the Stripe Test Interface so the credit card entry form can take a card number of 424242424242 and also use this repeating sequence for the date, CVC number and Zip code.
We secure communication with Stripe by using a combination of a private and public key. These are configured as part of the site's environment variables.

### Webhook
A webhook is a means of providing a form of asynchronous confirmation from an external server. We send an event to the server and when it is finished processsing the event it confirms success or failure by calling our webhook and communicating the status of the process.
The Fit For Life site usea a single webhook at **checkout/checkout/wh.**
<br>
![All Products Page](https://github.com/johnosbb/FullStackDeveloper/blob/master/webhookflow.jpg)
<br>
To additionally secure the webhhok we use a webhook secret provided by Stripe. This is used to sign the incomming data so that any modification of the message is easily detected. The signing process also incorporates a time stamp to prevent replay attacks.
Strip provide an interface for both testing the weebhook and checking the status of webhooks sent from Stripe toour site.
![Stripe Logs](diagrams/strip_intent_logs.png)
* We can review logs and test intents on: https://dashboard.stripe.com/test/logs/
* Webhook testing is available at (https://stripe.com/docs/webhooks/test) <br>/
![Stripe Webhook Testing](diagrams/testwebhook.png)

#### Testing a Web Hook Endpoint using CLI
For more complex problems with webhooks it is possible to test locally using the Srtipe CLI
* [Stripe Documentation](https://stripe.com/docs/webhooks/test)

# Application Structure
* - model, data associated with the page
* - view, how we present the data to the user through html
* - urls, how the site routes the user to the relevant page
* - forms, (optional) how the user can input data
## Applications

### ffl - main application

### about - An about page with a contact form
### cart - facilitates orders and purchase
### checkout - pages associated with secure payment
### home - default homepage

### plans - Pages exclusive to members
### workouts - individual worksout instructions detailed used by the plans page
### planowrkouts - established many to many relationship between plans and workouts

### profile - user profile data
### products - pages for products, product detail, and product admin

### Utility scripts (will not appear in final commit)
* run.sh - runs the application locally
* sync.sh - pulls the latest git
* commit.sh - pushes to the repository

### diagrams - database diagrams for reference


# Database Design
## Key relationships
![Main Database Design](diagrams/maindiagramcompact.png)

## Main Tables
### Products Table
![Products Table Design](diagrams/products_product.1degree.png)
### Plans Table
Plans and workouts have a Many To Many relationship. A plan can have many workouts and that workout can feature in many plans.
![Plans Table Design](diagrams/plans_plan.1degree.png)
### User Profile Table
![User Profile Table Design](diagrams/profiles_userprofile.1degree.png)

## Databse Design
Mot of the tables have simple foreign relationships toother tables, but the Plans and workouts have a Many To Many relationship. This is covered in the Django documentation at https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/.


## Database Diagrams
The database diagrams in this document were generated by schemaspy (available from http://schemaspy.org/).
### Installation Procedure
```sudo apt install default-jre```
### Instructions for setting it up
```Launching is as follows: java -jar schemaspy-6.0.0-rc2.jar -t pgsql -db database_name -host myhost:myport -u username -p password -o ./schemaspy -dp postgresql-9.3-1100.jdbc3.jar -s public -noads```
The script produces a fully indexed set of database diagrams and documentation.

# Development
Several steps were taking setting up so that this project could be developed:
### Enviroment Variables
The below environment variables were set up:

Variable name |	Used for	
------------ | -------------
EMAIL_HOST_USER	| Sending notification emails	
EMAIL_HOST_PASSWORD |	To login for sending notification emails	
STRIPE_PUBLIC_KEY |	Needed for the stripe payment system	
STRIPE_SECRET_KEY |	Needed for the stripe payment system	
STRIPE_WH_SECRET   |	Needed by the webhook for encryption of the payment confirmation
AWS_ACCESS_KEY_ID | Needed for the S3 Bucket static files	
AWS_SECRET_ACCESS_KEY | Needed for the S3 Bucket static files	
AWS	Deployment only | to tell Django to use s3 instead of local static files	
DATABASE_URL | Deployment only - sets hosted Postgres database	
SECRET_KEY | Used by Django as a salt to generate hashes

### Requirements.txt
All the projects dependencies will need to be installed before beginning: type pip install -r requirements.txt or pip3 install -r requirements.txt. If you add or update any packages in the project or add any new ones then use pip freeze --local > requirements.txt to update the requirements.txt file with the new dependencies.

# Deployment

## Heroku
I used the following [guide](https://github.com/codingforentrepreneurs/Guides/blob/master/all/Heroku_Django_Deployment_Guide.md) to help with deploying my project to Heroku.
### Creating the Heroku Postgresql app
* heroku login -i
* heroku apps:create django-ffl-app --region eu
* I checked its status with: heroku apps
* I then went to https://dashboard.heroku.com/apps/django-ffl-app/resources
* In the Add on section I searched for heroku-postgresql
* After install I went to https://dashboard.heroku.com/apps/django-ffl-app/settings and clicked reveal config vars to see the default environment variables.
* The Database URL will be available here and it will be something like; postgres://bmhukkzcvbrudo:f0...09b91a12d869da.........e90906bf522e82621b6a4b7a3...92d8a209@ec2-54-246-115-40.eu-west-1.compute.amazonaws.com:5..2/dcr08.......
* I installed an app for support of the postgres database inteface with:  pip3 install dj_database_url
* You can also find the postres database reference directly on the heroku cli by using: heroku config -a django-ffl-app: this will reveal the database string also
* I then added the necessary include to the top of the settings.py file: import dj_database_url
* I added a database definition for the postgreSQL cloud hosted database: 
```
`DATABASES = {     'default':  dj_database_ur.parse('postgres://bmhu......do:f0efd09b91a1...............90906bf522e82621b6a4b7a3712c992d8a209@ec2-54-246-115-40.eu-west-1.compute.amazonaws.com:..32/dc......67p5k70')`
`}`
```
* I initially disabled the requirement to collect static files: heroku config:set DISABLE_COLLECTSTATIC=1. This will later be enabled when AWS is set up to serve the static files.
* I then created a Procfile with the following content: <br>/
```web: gunicorn ffl.wsgi:application```
* I added the heroku hostname to the allowed hosts section of my settings.py file: ALLOWED_HOSTS = ['django-ffl-app.herokuapp.com']"
* After commiting all of these I pushed the changes: git push heroku master

### Connecting to Heroku Database from the Heroku CLI:
It is often usefull to connect to the Heroku database from your local machine or gitpod. Heroku provide a postgres interface throught their CLI.
* heroku pg:psql
* It will select the default database
* You can issue SQL commands:  select product_name from public.products_product;
* A guide to using the cli is [Here](https://devcenter.heroku.com/articles/heroku-postgresql#using-the-cli)
* Dumping Database in plain Text format: [Here](https://stackoverflow.com/questions/22887524/how-can-i-get-a-plain-text-postgres-database-dump-on-heroku)



# Technologies Used
* [HTML](https://html.com/) – the project uses html as the main language to build the website
* [Bootstrap](https://getbootstrap.com/) – Used as the main frontend framework.
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) – CSS is used to add individual style to the website
* [Javascript](https://www.javascript.com/) - JS was used to initate certain features of Materalize.
* [Font Awesome](https://fontawesome.com/) – this site was used to add icons to the site.
* [Django](https://djangoproject.com/) - Django is used as main python framework.
* [MySQL](https://www.mysql.com/) - Used as the main database technology.
* [Jinga](https://jinja.palletsprojects.com/en/2.11.x/) - Used as the main templating language for template manipulation.
* [Heroku](https://signup.heroku.com/?c=70130000000NeLCAA0&gclid=Cj0KCQjw-uH6BRDQARIsAI3I-UcV96h-n1NbhCxrdQnrMSjNQ72hwiisldeoifqoNJDw0Bf6ekDhtvwaAq5iEALw_wcB) - Used to host the Website and Database.
* [AWS/S3](https://s3.console.aws.amazon.com) - Used to host static files and media.

# Testing
In order to assure that the website performs efficiently and the features carry out the functions that they are created to, I conducted several tests which are outlined in a seperate [document](/test.md).
