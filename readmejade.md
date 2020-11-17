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
<img src="(/Readme/MockUps/FFLMocupAllProductsPage.jpg) style="margin: 0;">
###### Individual Product page
<img src="(/Readme/MockUps/FFLMocupProductPage.jpg) style="margin: 0;">
###### Profile page
<img src="(/Readme/MockUps/FFLMocupAllProfilePage.jpg) style="margin: 0;">
###### Products page
<img src="(/Readme/MockUps/FFLMocupPlansPage.jpg) style="margin: 0;">

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



