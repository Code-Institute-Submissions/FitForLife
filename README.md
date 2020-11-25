# Fit For Life - Milestone 4 Project 
Fit For Life is an e-commerce website built using Django and Stripe. Fit For Life sells products and a membership which allows registered users to view fitness plans and receive a member discount. Fit For Life caters for all individuals with a selection of fitness plans from muscle building to weightloss to general fitness. The plans can be viewed on the website once a user purchases a membership. Both non-registered and registered users can view and purchase products such as protein bars and shakes. Registered users will have a profile where they can view their membership plan and previous orders.

# UX
## Project Goals
Create a fully fucnctional website using Django and Stripe that allows user to register to avail of a benefit while also allowing non-registered users the option to browse the site and make purchases. The overall goal for this website is to allow visitors to purchase products and encourage them to register by offering a discount and exclusive plans. Registered users have their own profile where they can view their membership details, view past orders and save delivery information. The design of this website was to keep it very simple yet eye-catching by incorporating in the bright orange which contrasts nicely with the black and grey used through-out the site.  I created a logo for the website and placed it on all the products as well as using the same orange colour in the product images to keep everything in theme. I used the Beba Neue font from
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
###### Products page
![Products Page](/Readme/MockUps/FFLMocupAllProductsPage.jpg) 
###### Individual Product page
![Individual Products Page](/Readme/MockUps/FFLMocupProductPage.jpg)
###### Profile page
![Profile Page](/Readme/MockUps/FFLMocupAllProfilePage.jpg)
###### Products page
![Plans Page](/Readme/MockUps/FFLMocupPlansPage.jpg)

# Features
Fit For Life comprises of a Homepage, products page, Individual Products Page, Plans Page, Plan Workout Page, Shopping Cart Page, Checkout Page and Profile page. The website is fully responsive.
### NavBar
This responsive  feature allows users to move from page to page. When a user is logged in it displays an option to visit a page called " MyProfile". There is also a link to "Logout" if a user is logged in. In the case that no user is logged in the NavBar simply displays a "Login/Register" Tab. For Mobile and Tablet devices -  a hamburger menu on the top-left expands a menu with links to all of the main pages. The navbar stays fixed at the top of each page for easy navigation at all times.
### Forms
Django Crsipy Forms were used for all forms on Fit For Life. These were installed using the following command - pip3 install django-crispy-forms. These forms allow users to submit their data and it then gets stored in the database or sent to email associated with the website. 
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
### Profile Page 
Registered users will have the option to view their profile page. This page will display their details (name, username etc), allow them to save shipping address details and to view their previous order details. 
### Stripe 
#### Integrating Stripe
* [Stripe Documentation](https://stripe.com/docs/payments/accept-a-payment?integration=elements)
Stripe works with what are called payment intents. The process will be that when a user hits the checkout page the checkout view will call out to stripe and create a payment intent for the current amount of the shopping bag. When stripe creates it. it'll also have a secret that identifies it. Which will be returned to us and we'll send it to the template as the client secret variable. Then in the JavaScript on the client side.
We'll call the confirm card payment method from stripe js. Using the client secret which will verify the card number.
And enter the stripe test card number. 424242424242, You can use any CVC, any date in the future for the expiration date. And any five-digit postal code.<br/>
#### Creating a Web Hook Endpoint
* Add a new endpoint with the URL of your site: https://8000-b..25............5.ws-eu01.gitpod.io/**checkout/wh**
* Register to receive all events and add the endpoint.
* This will take us to a page where we can reveal the web hook secret key. Add this to your: https://gitpod.io/settings/
* You can send a test event from this page: https://dashboard.stripe.com/test/webhooks/
* We can review logs here: https://dashboard.stripe.com/test/logs/
#### Testing a Web Hook Endpoint using CLI
* [Stripe Documentation](https://stripe.com/docs/webhooks/test)

# Deployment
### Enviroment Variables
The below environment variables were set up:

Variable name |	Used for	
------------ | -------------
EMAIL_HOST_USER	| Sending notification emails	
EMAIL_HOST_PASSWORD |	To login for sending notification emails	
STRIPE_PUBLIC_KEY |	Needed for the stripe payment system	
STRIPE_SECRET_KEY |	Needed for the stripe payment system	
STRIPE_WH_SECRET   |	Needed for the stripe payment system	
AWS_ACCESS_KEY_ID | Needed for the S3 Bucket static files	
AWS_SECRET_ACCESS_KEY | Needed for the S3 Bucket static files	
AWS	Deployment only | to tell Django to use s3 instead of local static files	
DATABASE_URL | Deployment only - sets hosted Postgres database	
SECRET_KEY | Used by Django as a salt to generate hashes

## Heroku
I used the following [guide](https://github.com/codingforentrepreneurs/Guides/blob/master/all/Heroku_Django_Deployment_Guide.md) to help with deploying my project to Heroku.
### Creating the Heroku Postgresql app
* heroku login -i
* heroku apps:create django-ffl-app --region eu
* checks its status with: heroku apps
* Now go to https://dashboard.heroku.com/apps/django-ffl-app/resources
* In the Add on section search for heroku-postgresql
* Install it then go to https://dashboard.heroku.com/apps/django-ffl-app/settings and click reveal config vars
* You can find the Database URL here and it will be something like; postgres://bmhukkzcvbrudo:f0...09b91a12d869da.........e90906bf522e82621b6a4b7a3...92d8a209@ec2-54-246-115-40.eu-west-1.compute.amazonaws.com:5..2/dcr08.......
* Now install pip3 install dj_database_url
* heroku config or heroku config -a django-ffl-app  will reveal the database string also
* Add the following to the top of the settings.py file: import dj_database_url
* Add the following definition for the postgreSQL cloud hosted database: <br>/
`DATABASES = {     'default':  dj_database_ur.parse('postgres://bmhu......do:f0efd09b91a1...............90906bf522e82621b6a4b7a3712c992d8a209@ec2-54-246-115-40.eu-west-1.compute.amazonaws.com:..32/dc......67p5k70')`
`}`<br>/
* Disable the requirement to collect static files: heroku config:set DISABLE_COLLECTSTATIC=1
* we now need to create a Procfile with the following content: <br>/
`web: gunicorn ffl.wsgi:application`<br>/
* Add the Heroku Hostname to our settings.py file: ALLOWED_HOSTS = ['django-ffl-app.herokuapp.com']"
* git add Procfile
* git add settings.py 
* git commit -m "Adding Procfile for Heroku and heroku hostname to allowed apps"
* we can now push to Heroku with: git push heroku master

### Connecting to Heroku Database from the Heroku CLI:
* heroku pg:psql
* It will select the default database
* You can issue SQL commands:  select product_name from public.products_product;
* A guide to using the cli is [Here](https://devcenter.heroku.com/articles/heroku-postgresql#using-the-cli)
* Dumping Database in plain Text format: [Here](https://stackoverflow.com/questions/22887524/how-can-i-get-a-plain-text-postgres-database-dump-on-heroku)

## MySQL
### Setting up MySQL with Python and Django
* sudo apt-get install libmysqlclient-dev
* sudo apt-get install libmysqlclient-dev python-dev
* pip3 install pymysql
* pip install mysqlclient

### Logging in to MySQL
* pip install mysqlclient
* sudo mysql -u root
* SHOW DATABASES;
* CREATE DATABASE ffl_database; #create a new database
* CREATE USER 'djangouser'@'localhost' IDENTIFIED WITH mysql_native_password BY 'djangouser90';
* GRANT ALL ON ffl_database.* TO 'djangouser'@'localhost';
* Add the following to the settings.py<br/>
`DATABASES = {`<br/>
    `'default': {`<br/>
        `'ENGINE': 'django.db.backends.mysql',`<br/>
        `'OPTIONS': {`<br/>
            `'read_default_file': '/etc/mysql/my.cnf',`<br/>
        `},`<br/>
    `}`<br/>
`}`<br/>
* sudo nano /etc/mysql/my.cnf
* Add this:
`[client]`<br/>
`database = hello_world`<br/>
`user = djangouser`<br/>
`password = djangouser90`<br/>
`default-character-set = utf8`<br/>
* Restart the mysql server
* sudo systemctl daemon-reload
* sudo systemctl restart mysql
* MariaDB's Strict Mode fixes many data integrity problems in MariaDB, such as data truncation upon insertion, by escalating warnings into errors. It is strongly recommended you activate it. [See here](https://docs.djangoproject.com/en/3.1/ref/databases/#mysql-sql-mode): 


# Technologies Used
* [HTML](https://html.com/) – the project uses html as the main language to build the website
* [Materalize](https://materializecss.com/) – Used as the main frontend framework.
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) – CSS is used to add individual style to the website
* [Javascript](https://www.javascript.com/) - JS was used to initate certain features of Materalize.
* [Font Awesome](https://fontawesome.com/) – this site was used to add icons to the site.
* [MongoBD](https://www.mongodb.com/cloud/atlas/register) - Used as the main database technology.
* [Jinga](https://jinja.palletsprojects.com/en/2.11.x/) - Used as the main templating language for template manipulation.
* [Heroku](https://signup.heroku.com/?c=70130000000NeLCAA0&gclid=Cj0KCQjw-uH6BRDQARIsAI3I-UcV96h-n1NbhCxrdQnrMSjNQ72hwiisldeoifqoNJDw0Bf6ekDhtvwaAq5iEALw_wcB) - Used to host the website.

# Testing

