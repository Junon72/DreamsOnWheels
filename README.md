# DreamsOnWheels

## Travis

[![Build Status](https://travis-ci.com/Junon72/DreamsOnWheels.svg?branch=master)](https://travis-ci.com/Junon72/DreamsOnWheels)

## E-commerce site for model cars

Heroku App: [DreamsOnWheels](https://dreamsonwheels.herokuapp.com)

GitHub: [DreamsOnWheels GitHub](https://github.com/Junon72/DreamsOnWheels)

The project was created as Milestone project for the Full Stack Development module in Code Institute run Full Stack Web Development course program.

---

## Index

1. [Project brief](#Project-brief)
2. [Project overview](#Project-overview)
3. [User stories](#User-stories)
4. [UX/UI](#UX-UI)
5. [Wireframes](#Wireframes)
6. [Planned features and functions](#Planned-features-and-functions)
7. [Planning](#Planning)
8. [Database schema](#Database-schema)
9. [Functional flow and Features](#Functional-Flow-And-Features)
10. [Admin site](#Admin-site)
11. [Technologies Used](#Technologies-Used)
12. [Project Setup](#Project-Setup)
13. [Testing](#Testing)
14. [Media and Content Origin](#Media-and-Content-Origin)
15. [References](#References)
16. [Special Thanks](#Special-Thanks)

## Project brief

**DreamsOnWheels** is an e-commerce site for exclusive model car collectables.

The site sells dreams in form of model cars:

- as a gift for a car lover.
- as a reminder of a goal to own the real dream car.
- to add to the collection of other dreams cars.
- to decorate the empty place on a shelve with something classy.
- to adore.

For the project I will combine two suggestions provided for the project:

*Project Idea 0*

Bring your own idea(s) to life, based on providing value to users to address a specific real or imagined need.
And a modified.

*Project Idea 2*

Build an e-commerce place to sell collectable items.

**External user’s goal:**

- Find, learn about and acquire collectable items they are interested in.

**Site owner's goal:**

- Earn money on selling collectables (the site owner is the seller)
and share the passion with other enthusiasts.

**Potential features to include:**

- Create an online store focused on selling exclusive collectable items.
In this case model cars from real dream cars.
- Allow users to search for artifacts based on various fields.
- Allow users to see the price, image and other basic details about a collectable.
- Users would be able to learn about the original dream car and its history.
- Allow users to vote for a model, they would like to see promoted (Users have to be registered).

**Advanced potential feature (nice-to-have)**

- Allow registered users to write comments to the blogs about dream cars and models.
- Expand the search functionality to allow users to sort results based on price
and other parameters in both ascending and descending order.
- Include pagination and/or other dynamic display actions using javascript.
- Use javascript polling to update the page whenever there's a new vote.

## Project Overview

DOW - DreamsOnWheels user is able to:

- Create an account with a username and password.
- Sign-in with a registered username and password.
- Reset password.
- Create a profile.
- Search models cars by make, model and other terms, and order them by price or build year.
- View details about the car models.
- Vote for a monthly highlighted dream car to be promoted or taken in to the collection.
- Read about the original cars behind the models.
- Read blogs.
- Comment on blogs.
- Add collectables in a shopping cart.
- View shopping cart.
- Purchase items in their shopping cart.

[Back to index](#index)

## User stories

The application is for dream car and model car enthusiasts.

### Possible users types

- Model car collectors.
- Model car enthusiasts.
- Hobbyists on all ages and demographics.
- Professionals.
- Friends and families of all above.

### Their stories stories

1. I'm a model car collector interested in high quality model cars and rare occasions.
I look for high quality products and good deals. On website I would like to read about
the models I am interested in purchasing and be introduced to new interesting collectables.

2. I'm a car and model car enthusiast who likes to read articles, stories and trivia about
all cars and car models. I often encage in discussion with like minded in car
and model car blogs.

3. I'm a car and model car enthusiast. My day job is a civil engineer, but I like
writing articles about car and collector cultures, which I research on my free time.
Occasionally I might buy an item myself, if I come across something nice with reasonable price.

4. I'm an advertising director for a classic car reseller chain. Our company is serving
high end clients, and we run loyalty programs. Sometimes we give gifts for our clients
for good measure or as rewords for loyal and long term customer relations.
I use different websites in search for unique and individualized items.

5. I'm a model car hobbyist, crown up with cars and technology. My dad was a devoted folkracer,
sparking my passion for cars. My passion for building models I can thank for my brothers.
As a female with a hobby traditionally dominated by males, I value web communities which
are inclusive and offer more than just the same old.

6. I know nothing about cars, or model cars for that matter, but my hubby is a devotee.
All he is talking about lately is Chevrolet Camaro this, Camaro that. I want to get him one,
not a real one, but a small version he can stare at and shut up. No, seriously,
he has a birthday coming, thought he would like something like that.
Where is the webshop of really cool model cars!

[Back to index](#index)

## UX UI

### CSS

Project uses Bootstrap 4 framework for responsive design.

### Typography

Three different font faces are used through out the project:

- [Lato](https://fonts.google.com/specimen/Lato?query=lato) for the content texts, links and details.
- [Arvo](https://fonts.google.com/specimen/Arvo?query=arvo) for the navigation buttons and logo.
- [Jost](https://fonts.google.com/specimen/Jost?query=jost) for page and article titles.

### Icons

For icons project uses [fontawesome](https://fontawesome.com/) free icon sets.

### Colors

The color schema is kept minimal and uses [Bootstrap dark, warning and light colors](https://getbootstrap.com/docs/4.5/utilities/colors/) as the main color set.

## Wireframes

For wireframes see [Wireframes](docs/documents/Wireframes.pdf).

To try out elements and layout I created a side project DOWstyle, which can be found [here].

[Back to index](#index)

## Planning

For planning see [Planning](docs/documents/Planning.pdf).

## Database Schema

For complete database schema see [Database ERD Chart](docs/documents/DatabaseERD.pdf).

## Functional flow and Features

Except for error pages 404 and 500, navigation bar appears on all pages.

[Back to index](#index)

### Before login user has access to the following pages

- Sales, Blogs, Blog, Highlight (Car highlight of the month) Login (+ Reset password), Register and Shopping cart.

- Through Products user can access Original pages.

### After login user has access to the following pages

- Sales, Blogs, Highlight (Car highlight of the month), Cart, Logout, Profile, Contact and Checkout.

- Through Blog page user can also add, edit and delete his/her own comments.

- Through Profile page user can add and edit his/her user profile.

Additionally, if user is accepted to become a contributor, he/she has access to admin post section for writing blogs.

### The site has the following pages and features

**General**

*Navigation bar*
Navigation bar is available on each and every page, except for error pages.

*Footer*
Footer is displayed on each and every page. Footer contains contact information and a link to the contact page.
It also has a link to social meadi site, but because the company is imaginary, the Facebook link does not work.
Alos footer is not displayed on error pages.

*Header section*
All pages have a header section with a page title and a extra navigation link. The link either return back to home page
or one page back. Also the logo and header image are displayed on each page (excluding the error pages,
which visually and functionally are their own class). Error pages do not have separate header sections.

*Content sections*
The main content of the page is presented always under the header section.

**Site Pages**

1.1. **Landing page/ Home**

Landing page presents the main content of the site, invites user to read about the monthly highlights they can
vote for and read blogs. About section tells about the company, its mission, values and people behind.

Sales preview section:

- Carousel of items on sale.
- Back/ forward carousel nav.
- Clicking  the image users is directed to the sales page.

Car Highlight preview section:

- Image (right / stacked on smaller screens).
- Title.
- Text.
- Button to view the highlights page.

Blogs preview section:

- Image (left / stacked on smaller screens).
- Title.
- Text.
- Button to view the page.

2.1. **Sales page**

Sales page contains all the products that are on the sales. The products are presented in product cards.
The user can add products to their cart by clicking add button in the cards. The cards display product image,
price and other information about the products. They also tell the user if the product is in promotion,
sold out or just out of stock. User can search product with several criteria and order the products bases
on price or model year. Products that are out of stock or sold out cannot be added to the cart.

Search filter:

- product by make/ model/ manufacturer...

*Product cards:*

Item card:

- Image.
- Product info section.
- Price and quantity section.
- Link to description modal giving more information about the product.
- Add to cart button. Button will be disabled if the product is sold out or out of stock.
- Read about original button.

Description modal:

- Image.
- Content text.
- Close button.

2.2. **Original page**

On Original page user can read about the original car the model car in sale is modeling.
The cars are presented in a form of article. they have title, image section and content section.
They also display estimate market value of the real cars.

- Image carousel.
- Title.
- Content text.

3.1. **Highlight page**

Highlights page presents every month a selection of dream cars. The formate is the same as in
Original pages.Users are invite to cast a vote for their favorite. At the end of th month,
the winning car mode is coming to promotion or the car model is introduced to the collection.
User can vote only once for a highlight. user can vote for all the cars in highlights,
but that reduces the chances for one of them winning. Only winner will be promoted.

Highlight section:

- Image carousel.
- Title.
- Content text.

User engagement section (login required)
Allows user to vote for a highlight.

- Vote button.

4.1. **Blogs page**

On blogs section user can read blogs about model cars, collecting, original cars,
car culture, history, stories and trivia.

*Blog cards:*

- Image.
- Author info.
- Title.
- Text excerpt.
- See more button directing user to the blog page.
- Comments counter.
- Views counter.

4.2. **Blog**

Blog is in article format. The blog authors profile image, username, username and
contributor type is displayed with the blog.

*Blog section*

- Title.
- Image.
- Text.
- Button to open the comment section.
- Comments counter in the button.

Blog has a comment section where users can leave comments.
Login is required to leave, edit and delete comments.

*Comment section*

- Leave a comment form (login required).
- Submit comment button.
- Edit comment modal form/ Save comment button/ Cancel button.
- Delete comment modal/ Delete comment button/ Cancel button.

6.1. **Profile** (login required)

- Profile image.
- Profile info.
- Edit profile button directing user to the edit profile page.

6.2. **Edit profile** (Login required)

On update profile page user can add or update information and add a profile picture.
Profile information will be used to profile the order form at checkout.
Information and image is also displayed with the users comments in blogs.

- Attach profile image.
- Profile form.
- Update profile button.

7.1. **Login**

Login page allows user to login to access pages for registered users.

- Login form.
- Submit button.
- Reset password link directing user to the reset password page.
- Register link directing user to the register page.

8.1. **Reset password page**

Reset password pages allows user to reset their password using their email.
They will be send an email with a link they can follow to set a new password.

- Reset password page with a form asking for their email address to send an
email with link to reset the password.
- Submit button which sends the user an email with a link and a token.

8.2. **Reset password email send declaration**

Confirms user email with the line has been send to the email address provided by the user.

- Confirmation page email has been send.

8.3. **Reset password email**

Email user will receive to reset his/ her password.

- Email with the link.

8.4. **Reset password confirmation page**

User can set a new password by filling in password form. Form will validate that user
has provided same password twice and that the token is valid.

- New password page with a form.
- Submit button.
- A message in case the token Was not valid asking user to fill in reset password form again.

8.5. **Reset complete page**

User is informed that the password has been changed successfully.

- Completed page informing user that the password has been changed.

9.1. **Register**

Register page allows user to register.

- Registration page with a form.
- Submit button.

10.1. **Cart** (Login required)

Cart displays the products user has added to the cart on Sales page. The carts are otherwise
similar to the product cards on Sales pages, except for link to the originals.
By setting the quantity of the product to 0,user can remove items from the cart.
If the cart is empty, user is informed cart is empty and given an option to go to the sales pages.
Page has a totals card that displays the total price of product totals.
If user is not logged in the cart will display a message user has to login to proceed to
checkout and a navigation button to the login page. The cart content count is displayed
next tot he cart navigation button.

*Cart item cards*

- Image.
- Title.
- Product info section.
- Link to open a product details modal.
- Unit price.
- Old price and reduced price if product is on promotion.
- Promotion badge.
- Quantity form order button.
- Total price.

*Checkout section*

- Login button and info message (for users not logged in).
- Total of totals.
- Make purchase button.
- Back to sales button.

11.1. **Checkout** (Login required)

Checkout allows user to purchase hte products placed in the cart.
Page has a form for order and for payment. Payment function uses Stripe API.
Information user has added to their user profile will be used to pre fille the order form.
On big screens, next to the forms are displayed the product cards in the cart.
On smaller screens products list is not presented separately.
Grand total is displayed at the bottom of the page.

- Order form.

*Stripe payment API*

- Payment form.
- Submit payment button.

12.1. **Logout**

After logout user will be directed back to home page.

13.1. **Contact**

At contact page, User can fill in a message form to contact the company.

- Contact form.
- Submit button.

[Back to index](#index)

## Admin site

### Users and groups

In all there are five authorization and access levels in the application:

1. Superuser, who is the main administrator and has access to everything.
2. Employees with staff status with limited administrative access.
3. Contributors with staff status and narrow access to some content in administration.
4. Registered users with access to all pages on the site.
5. Non registered users with access to some pages on the site.

The admin site functionality follows a business logic of an imaginary enterprise.
The site admin pages give the users with admin credentials practical interphase to created and manipulate data.

*Superuser*
Has superuser status and access to all admin functionality, including ability to add,
chang and delete, log entries, goups, permissions, sessions and the site itself.

*Staff - Employees*
Have staff status and access to all pages accept for ability to add, change or delete log entries,
group authorizations, sessions, and site, where the superuser has the sole control over.
The employees can add data to the database, e.c. add Products and Posts.
They are instructed with the requirements for the content and formate of the media,
and as employees are bind to good practice by a contract. Employees are responsible for adding,
editing and deleting content, e.c. Products, Posts and Originals.

Since the company is imagined to be small,
further division or authorization categories were not considered essential.

*Staff - Contributors*
Have limited staff status and access only to add, change and view posts.
Contributors consists of group of guest writers, contributing to the blogs.
The contributors would be vetted and bind by a contract to protect the site from
malice intends and follow the requirements for the content, media formats and good practice.
The contributor status is set by Employees or superuser in User profile.
User profile is expected to be completed, with contact information and profile image,
before contributor status is admitted. Contributors themselves cannot set contributor status.
The blog Posts go through review process before publishing.
Posts can be drawn for example for corrections etc. The default value of a post is Draft.

### Admin model views

Contributor related models:
*Users (parent)*
Users are listed by Username, Email address, First Name, Last Name and Staff Status.
Users can be filtered by Staff status, Superuser status, Active status, and Group.

*Profiles (child)*
Profiles are listed by Username, Contributor status, Phone number, Zipcode, or/and Country.
Contributor status can be changed only on profile page.
Profiles can be filtered by Contributor status.

Posts are connected to Contributors and other Staff who are possible Posts authors:
*Posts (parent)*
Posts are listed by Status (Draft, Review, Published, Drawn), Author, Title,
Created date and Tag. Status can be updated from general Posts admin view.
Posts can also be filtered by Status, Publishing data and Tag.

To the Posts are connected Comments, where any user who is registered can be a Comment owner:
*Comments (child)*
Comments are listed by Publish status (Moderate, Published, Suspended). Default value is Moderate.
All comments are moderated at beginning. For now the comment status is not changed back to
Moderate after editing, but this would ideally be the case. Moderation would be performed
by the Employees. The task could easily be allocated for a third party, for example by creating
a new staff Group with authorization to edit Comments in general admin Comments view and
view Posts. the comment status can be updated from the general view.
Besides the status the list displays Comment owner, Content, Post to which the Comment belongs to
and Created date. Comments can be searched by Status and Created date.

Posts and comments constitute the sites social part. Products and Originals make up the
e-commerce part of the site.

*Originals (parent)*
The models sold on the site have an Original counterpart, a real or conceptual car the models emulate.
On admin site the Originals are listed by Status (Active, Highlight, Draft and Inactive), Make, Model and Votes
The Status default is active. Highlight status is used to publish the selected Originals on the Highlights page.
Draft and Inactive statuses are added for the site in future to include a separate page for the Originals.
The categories would give more control over the Originals states, being either published, or still a draft,
or perhaps archived. The status can be changed in the general Originals admin view. Originals can be filtered by
Status, Make, Model or Build year.

*Votes (child)*
When a user casts a vote for a highlighted original, the vote is registered in votes counter and in the Votes.
Votes are listed by Model in Votes admin view. They are connected to the Original and User models.

*Products (child)*
Products are added by the staff and they are listed by Status (On sales, Promotion, Sold out, Out of stock,
Not on sales), In stock, Make, Model, Built year, Manufacturer and Color.
Default status is On sales. Products with Promotions status are in promotion.
For Sold out products there is no expectation of them coming back sales anymore.
Out of stock products will likely return despite momentarily not being available.
Not on sales products are for any given reason not meant to be on the sales page, but are neither
deleted from the database. The status can be changed from th general Products admin page.
Products can be filtered by Status, Make, Model, Build year, Manufacturer and Color.
Product is always connected to an Original, which is one of the core tenants of the companies business model.

Products are connected to the Orders consisting of Order (parent) model and OrderLineItem (child) models.
They are connected to the Products.
In admin site the models are combined under Orders.
*Orders*
Orders are displayed with the Date of the order, Full name and Email address. The entries are ordered by date.
There is no filter.

Contact messages the users are sending can also be found in admin.
*Contacts*
Contacts are listed by Status, Date, Subject, Message, Name and From email.
The status default value is New, meaning the message has not been read yet.
After the read the status are divided to three main categories:

- one for contacts to sales (Sales read, Sales follow, Sales done).
- one for contacts from user who want to become contributors (Contributor request, Contributor in exchange, Contributor done).
- one for other contacts (Other read, Other follow, Other done).
The status can be changed from the Contacts general admin view.
Contacts can be filtered by Status and Date.

## Planned features and functions

- Features and functions planned but not implemented yet.

1. Ordered items listing on user's Profile page, so user can see what items he/ she has purchased.
2. Email response after checkout with order confirmation.
3. Pagination on Sales page.
4. Integration of social media platform, such as Facebook on blogs section for likes, links and commenting.
5. Comment section for the Originals.
6. Pagination of the comment section.
7. Separate Originals section.
8. Search posts function on Blogs page.
9. Add dynamic posts tags for searching Posts by tags, as well as by Author, Date, and Title on Blogs page.
10. On deletion of Vote, the vote counter of the related Original would be subtracted by 1.

[Back to index](#index)

## Technologies Used

### Languages

- [CSS3](https://developer.mozilla.org/en-US/docs/Archive/CSS3 "CSS3") is a style sheet language used for describing the presentation of a document written in a markup language like HTML.
- [HTML5](https://html.com/html5/) is code that describes web pages.
- [JavaScript](https://www.javascript.com/ "JavaScript") is an interpreted programming language used for Web pages.
- [Python 3.7.6](https://www.python.org/ "Python 3.4.3") is an interpreted, high-level, general-purpose programming language.

### Frameworks and libraries

- [Bootstrap 4](https://getbootstrap.com/ "Bootstrap") is a free and open-source CSS framework directed at responsive, mobile-first front-end web development.
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) is the AWS SDK for Python that is used to connect to AWS S3 buckets.
- [coverage](https://coverage.readthedocs.io/en/coverage-5.1/) is a tool for measuring code coverage of Python programs,
used to gauge the effectiveness of tests and showing which parts of your code are being exercised by tests, and which not.
- [dj-database-url](https://pypi.org/project/dj-database-url/) allows the use of 12factor inspired DATABASE_URL environment variable to configure Django applications.
- [Django 3](https://docs.djangoproject.com/en/3.0/releases/3.0/) is a Python-based free and open-source web framework.
- [django-bootstrap-modal-forms](https://pypi.org/project/django-bootstrap-modal-forms/) is a Django plugin for creating AJAX driven forms in Bootstrap modal.
- [django-countries](https://pypi.org/project/django-countries/) is a Django application that provides country choices for use with forms.
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) is an API to control the rendering behavior of Django forms.
- [django-filter=](https://django-filter.readthedocs.io/en/stable/) a filter API to filter down a query set based on a model’s fields.
- [django-storages](https://django-storages.readthedocs.io/en/latest/) is a storage backend utility, used to connect to S3 in this project.
- [django-widget-tweaks](https://pypi.org/project/django-widget-tweaks/) is an API to tweak the form field rendering in templates.
- [flake8](https://pypi.org/project/flake8/) is a toolkit for checking that the code is PEP8 compliant, for programming errors and code complexity.
- [Font Awesome 5](https://fontawesome.com/changelog/latest) is a font and icon toolkit based on CSS and LESS.
- [Google fonts](https://fonts.google.com) is a Google owned library of free licensed fonts.
- [Gunicorn](https://pypi.org/project/gunicorn/) takes care of everything which happens in-between the web server and your web application,
making sure that web servers and python web applications can talk to each other.
- [jQuery](https://jquery.com/) is a JavaScript library designed to simplify HTML DOM tree traversal, manipulation and event handling, CSS animation, and Ajax.
- [Pillow](https://pypi.org/project/Pillow/) is a Python Imaging Library.
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/) is a PostgreSQL database adapter for Python.
- [Slick](https://kenwheeler.github.io/slick/) is a JSDeliver free public CDN open-source project for clean, responsive and easy to manage carousel element.
- [stripe](https://stripe.com/) is an e-commerce API provider, used for handling payments (on test mode) in this project.

### Tools

- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)  is a set of web developer tools built into Chrome.
- [Firefox Developer Tools](https://developer.mozilla.org/en-US/docs/Tools) is a set of web developer tools built into Firefox.
- [Git](https://git-scm.com/ "Git") is a distributed version-control system for tracking changes in source code during software development.
- [GitHub](https://github.com/ "GitHub") is a Web-based hosting service for version control using Git.
- [VSCode](https://code.visualstudio.com/ "VSCode") IDE, is a free source-code editor used for the development.
- [Django secret key generator](https://miniwebtool.com/django-secret-key-generator/) to generate fresh django secret key.

### Databases and services

- [SQLite3](https://www.sqlite.org/index.html) is the default Django database used during the application development.
- [PostgreSQL](https://www.heroku.com/postgres) is a production database provided by Heroku, used for the deployment and production.
- [AWS S3](https://aws.amazon.com/s3/) is an Amazon provided object storage service, used for storing  static and dynamic files.

### Deployment platform

- [Heroku](https://www.heroku.com/ "Heroku") is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

[Back to index](#index)

## Project Setup

### Setting up IDE

The project was developed using [VSCode IDE](https://code.visualstudio.com/ "VSCode IDE") with Mac OS High Sierra operating system.
For the version control, the code was pushed to local git repository and then to [GitHub](https://github.com/ "GitHub") repository.
The application was then auto-deployed through [Heroku](https://www.heroku.com "Heroku") from the GitHub Master.

To work with python, Python3 library has been first installed locally to the root directory with [Homebrew package manager](https://brew.sh/ "Homebrew package manager").
[Install Homebrew](https://brew.sh/#install "Install Homebrew") has instructions how to install brew to Mac.

To check if and which version of Python you have installed (Mac comes Python2 preinstalled) globally, you can open the Terminal and type:

`$ python --version`  # this will normally give you the version of python2 unless you have Python3 already installed.

To see if you have Python3 installed, type:

`$ python3 --version`

I wrote the application using Python 3.7.6.

### Setting up git for version control and connecting to GitHub

For version control I have used GirHub open source version control system. You can also yous Git or any other version control system provider.
To make a GitHub account you can [follow the instructions here](https://help.github.com/en/github/getting-started-with-github).

It is good to acknowledge the fact that [from 2020 January on, Python2 does not receive further official support](https://wiki.python.org/moin/Python2orPython3 "from 2020 January on, Python2 does not receive further official support").
Here you can find instructions [how to install the latest version of Python on your Mac](https://docs.python-guide.org/starting/install3/osx/ "how to install the latest version of Python, or to upgrade to Python3").

VSCode uses Python interpreter extensions to read Python code. Extensions include helpful features for the developers,
such as [editing helpers, debugging, linting and testing.](https://code.visualstudio.com/docs/python/python-tutorial "editing helpers, debugging and linting.").

Application uses Python libraries and package modules to accomplish the needed functions. After setting up the IDE to your liking,
and creating your working directory, but before starting to code and using Python modules, it is important to isolate your development environment.
Otherwise, there might rise conflicts between dependencies in different Python projects.
Python3 comes with a build in tool 'venv' to create a [virtual environments](https://realpython.com/python-virtual-environments-a-primer/ "virtual environments") for this purpose.

#### Virtual environment

To create a virtual environment in VSCode on Mac, in VSCode Terminal type:

`$ python3 -m venv <virtual_environment_folder_name>`

This will create a virtual environment folder to the root directory of your project.
Often the folder is named either env, venv or .venv, but you can name the folder to your liking. I used foo.

The folder contains the following sub-folders:

- bin: files that interact with the virtual environment.
- include: C headers that compile the Python packages.
- lib: a copy of the Python version along with a site-packages folder where each dependency is installed.

To activate the virtual environment, type:

`$ source <virtual_environment_folder_name>/bin/activate`

This will activate the environment. After activation you will see the environment name in brackets
front of the command line in which context the system now operates.

`(<virtual_environment_folder_name>) $ <your code>`

Now the Python version is run from the virtual environment file, rather than from the global install
and the Python packages imported using pip3 are isolated to the this environment only.

To exit the environment type:

`$ deactivate` which will return back to the 'system' context.

You would want to do the development work in your virtual environment! From Python3.6 on this is the
recommended method of using virtual environments.

### Creating a local git repository

In virtual environment activated initialize a local git:

`git init` # creates a git file for the project.

Add README.md file:

`git add README.md`

Before adding the files on the workspace to the repository create a .git ignore file. Add
files folders you do not want to be pushed to the GitHub or be seen by public to your .gitignore file. Such files include VSCode
settings, environment files, database and files containing sensitive information, like secret keys, passwords etc.

You can create a .gitignore file by typing:

`echo '<virtual_environment_folder_name>' > .gitignore`

As this is a Django project, I used [Gitignore pages](#https://www.gitignore.io/) to produce .gitignore file
specifically for Django, which I copied and pasted to the .gitignore file.
VSCode specific settings I copied from [ofthelit GitHub pages](#https://github.com/github/gitignore/blob/master/Global/VisualStudioCode.gitignore).

After adding Django and VSCode files and folder to the .gitignore file,
stage and commit the current file, byt typing:

`git add .` # adds all the current files, excluding the files defined in .gitignore.

`git commit -m "Initial commit"` # commits the files into the local git repository.

### Creating a GitHub repository

In Github create a new depository and push the project to the repository:

```bash
git remote add origin https://github.com/<username>/<name_of_your_repository>.git
git push -u origin master
```

You will be asked to sign in to your GitHub repository and give your password before push!

After this you can push using just `git push`.

I have installed VSCode GitHub extension, which makes committing changes slightly easier,
by skipping username and password inquiry with each new commit.

### Installing packages

To install packages to your environment you need to update your pip, which is a Python package installer:

`pip install --upgrade pip`

Install Django:

`pip3 install Django`

To help with code writing and for Python pep compliance I installed pep8,
autopep8 and pylint packages:

`pip3 install pep8 autopep8 pylint`

At this point it is good to create the requirements file, which will be updated regularly after
installing new packages while developing the application:

`pip3 freeze > requirements.txt`

Now the IDE workspace is set and at this point the file tree should look like this:

```bash
<project>
├─ <virtual_environment_folder_name>
│  ├─ bin
│  ├─ include
│  ├─ lib
│  └─ pyvenv.cfg
├─ .gitignore
├─ README.md
└─ requirements.txt
```

If you click bin, you will find the packages you have installed from there.

### Starting a Django project

The workspace is now ready to start a Django project:

`django-admin startproject <project_name> .`

The full stop at the end places the manage.py file to the root directory.

To be able to run the project locally, provide a server address for local server.

The address depends on which kind of setup you are working. For VSCode on Mac the address is '127.0.0.1`.

Open `<project_name>` folder and settings.py file. Add the address to allowed hosts:

```bash
ALLOWED_HOSTS = [
    '127.0.0.1'
]
```

Before running the application to test Django it has to be migrated to initialize it. I terminal type:

`python3 manage.py migrate`

Then run the project:

`python3 manage.py runserver 127.0.0.1:8000`

`cmd` + click the link provided in terminal to open the project in a browser:

`Starting development server at http://127.0.0.1:8000/`

In browser you'll see the Django welcome page which confirms everything is configured properly.

![Image of Django project page](docs/images/Django-page.png)

[Back to index](#index)

## Deployment

If you want to deploy the app in Heroku, I recomment first deploying the app locally.
This way you already know what you need for running the app.

### Local deployment

To deploy the project locally you will need to have minimum Python 3.7 and Django 3 installed.
It is also recommended to update PIP and use pip3 command to install packages and libraries.
The following instructions are for MacOS and VSCode, but the steps are pretty much the same
for other setups too, with slight differences in commands. Consult the documentations of your IDE
and GitHub to alter the steps to suit your own setup. There is a good tutorial for VSCode and
Django at [vscode-docs](https://github.com/Microsoft/vscode-docs/blob/master/docs/python/tutorial-django.md), with well written and practical instructions to get started with Django in VSCode IDE.
I sure wish I had come across this resource at beginning of of project rather than at the end.

Steps to deploy project from GItHub to VSCode on MacOS.

1. Clone or download a copy of the GitHub repo to your machine. Cloning is perhaps the easiest way
as VSCode has build in helper functions to work with gits.
a. To clone the project, copy the project URL using the Clone button provided in the GitHub repo.
b. Open VSCode and in `View` tab, select `Command Palette`. This will open a select menu in VSCode window.
c. Select `Git: Clone` option and paste the URL into the provided URL input field. Press Enter.
d. Create a source folder in location of your liking. Just be aware that the source folder should always
reside higher in the folder tree than any global installation you intend to use with the VSCode projects.
It is recommended to create a virtual environment though, to keep the required dependencies isolated from one another.

2. Create a virtual environment by typing `python3 -m venv <virtual_environment_folder_name>`.
You can find further instructions for this step in [here](#Virtual-environment).
3. Activate the environment `source bin/<virtual_environment_folder_name>/activate`.
4. Install the required modules and libraries `pip3 install -r requirements.txt`.
They can be found in your virtual environment folder now.
5. In root directory, create env.py file to set the local environment as follows:

```bash
import os

# Django
os.environ.setdefault("SECRET_KEY", "<Enter Django secret key>")

# Postgres
os.environ.setdefault("DATABES_URL", "<Enter Heroku Postgres URI here>")

# Stripe keys
os.environ.setdefault("STRIPE_PUBLISHABLE", "<Enter Stripe publishable key - starts with pk>")
os.environ.setdefault("STRIPE_SECRET", "<Enter Stripe secret key - starts with sk>")

# Email settings
os.environ.setdefault("EMAIL_HOST_USER", "<Email address used for sending emails>")
os.environ.setdefault("EMAIL_PORT_PASSWORD", '<Password for the email>')
os.environ.setdefault("EMAIL_HOST", "<Outgoing mail server - e.c. smtp.gmail.com>")
os.environ.setdefault("EMAIL_PORT", "<smpt port - e.c. gmail is 465 or 587>")
```

- If you are running the app locally, the media files will be also saved locally. Setting up AWS S3
to serve static and media files won't be needed.

6. Create SQLite3 database.
a. In terminal run `python3 manage.py runserver`.
b. Then close the server with CTRL + c.

7. Migrate the data models in apps by running `python3 manage.py migrate` in terminal.
8. Create a superuser.
a. In terminal run `python3 manage.py createsuperuser`.
b. Enter username and password. Password will be asked twice for confirmation.
9. Start the server again, this time using port so you can open the project in browser and login to the admin.
a. In terminal run `python3 manage.py runserver 127.0.0.1:8000`.
b. In your browser url tab navigate to `http://127.0.0.1:8000/admin`.
c. Login with your superuser credentials.

#### Admin panel

- If you want to emulate the setup as it has been thought out in real life scenario,
you would need to create minimum of two groups: Employees and Contributors. You can find more about the
groups authorization and access levels from [here](#Users-and-groups).
- To make a user a contributor, go to the user profile of that user, and select Contributor.
- On that users User page, add the user to the Contributors group.

10. To use Stripe, you need to create a [Stripe account](https://stripe.com/en-nl). Up to date instructions for setting up Stripe account, how to obtain Stripe keys and make test purchases can be found [here](https://testdriven.io/blog/django-stripe-tutorial/).

After completing these steps, you should be able to run the project on your machine.

### Heroku deployment

To deploy the app in Herpku, push the app to your own GitHub repo. You will also need to have [AWS account](https://aws.amazon.com/), and [create and confugure an AWS S3 Bucket](https://aws.amazon.com/s3/getting-started/) to serve static and media files.

Note, that the setting are currently written for the bucket I have created for the project, so it might be that you need to chang the bucket name in setting.py to correspond yours.

1. To deploy the project on heroku, go to [Heroku](https://www.heroku.com/ "Heroku") and create an account.
2. create a new app, using `NEW` button.
a. Give app a name.
b. Choose a region.
c. Click `Create an app`.

3. Got dashboard and click `Resources` tab, to create a Postgres database. You can start typing Postgres in the input field,
till you see `Heroku Postgres`.
a. Select Heroku Postgres from the list.
b. In the modal window choose `Hobby -Free` and click `Provision`.

4. For your env.py, you will need the DATABASE_URL vars, whic you can find from the Resources tab.
a. In recourses click `Heroku Postgres` to open Heroku Data window.
b. Click `View Credentials...`. The URI address in the list is your `DATABASE_URL` value.

4. Back in Heroku dashboard, go to Settings, and click `Reveal Config Vars`.

#### Heroku vars

| KEY               | VALUE |
|-------------------|-------|
| SECRET_KEY | Django secret key |
| EMAIL_HOST_USER | Email address you want to use to send emails |
| EMAIL_HOST_PASSWORD | PAssword for that emailaddress |
| EMAIL_HOST | smpt server name. e.c. smtp.gmail.com |
| EMAIL_PORT | SMTP port, usually 465 or 587 for gmail |
| USE_EMAIL | True |
| AWS_ACCESS_KEY_ID | Your AWS access key |
| AWS_SECRET_ACCESS_KEY | Your AWS secret key |
| USE_AWS | True |
| STRIPE_PUBLISHABLE | Your Stripe publishable key |
| STRIPE_SECRET | Your Stripe secret key |

5. In your env.py file add the DATABASE_URL vars - strting with `postgres://`.

- After this step the project should be connected to Heroku Prostgres database.

6. To initiate the database migrate and create a new superuser.
a. `python3 manage.py migrate`.
b. `python3 manage.py createsuperuser`, give username and twice a password.
7. Delete the DATABAE_URL from your env.py. The database is now migrated, and in devlopment environment SQLite3 will be used.

8. Complete the deployment in Heroku.
a. Click Deploy tab, and in `Deployment method` section select Use GitHub.
b. Serach for your GitHub repo and connect.
c. In `Manual Deploy` further down on the page, click `Deploy branch`. Wait while Heroku builds the project.
d. When building is comlete, click `View` button under the build log.

9. To use the app as intended follow the recommendations and instructions [here](#Admin-panel).

[Back to index](#index)

## Testing

Some automated testing was written for applications. The current overall coverage is 87%.
Python code was tested with [flake8](https://pypi.org/project/flake8/).
HTML code was tested with [W3 validator](https://validator.w3.org/).
CSS code was tested with [Jigsaw validator](https://jigsaw.w3.org/css-validator/).
JS code was tested with [JShint](https://jshint.com/).

All the functionality, features and pages were tested manually. The forms were tried with unqualified inputs, to test
form validation, input validation and error messaging as well as valid inputs and messaging where messaging was relevant.
Email functionality were tested, both with console backend and using smtp server.

The application was also tested by friend and family, who I instructed to make account, login, vote for highlight,
leave a comment and to make a purchase. I also was asking if they would try to reset their password, edit and delete a comment,
after they've been published. Adjustments were made to features that appeared confusing of not self explanatory after discussion
with the testing individuals.


### Bugs

In deployment phase to Heroku, I suddenly lost ability to login to the Admin page. The admin login stopped showing up.

I got a message on console when trying to access admin login stating:

```GET https://dreamsonwheels.herokuapp.com/admin/login/?next=/admin/ 500 (Internal Server Error)```

On local server the message was:

```bash
DoesNotExist at /admin/login/
Site matching query does not exist.
```

With the assistance from Code Institute tutor Kevin Lorey, the bug was resolved by removing `django.contrib.sites` from the `INSTALLED_APPS` in project settings.py file.


[Back to index](#index)

## Media and Content Origin

[Wikipedia](https://www.wikipedia.org/) was used to create content for the products, originals and blogs, and images.

Most product images were downloaded from following.

- [Pexels](https://www.pexels.com/).
- [Free images](https://www.freeimages.com).
- [Unsplash](https://unsplash.com/).
- [Mad4Wheels](https://www.mad4wheels.com/).

Some model cars origins are not definite. If there is any copyright frictions, I would like to be contacted at juno.athome@gmail.com, so I can remove the content.

- [icon-icons](https://icon-icons.com/icon/avatar-default-user/92824) - for the default user avatar / profile image.

[LorryIpsu](http://www.lorryipsum.com/), [DeLorean Ipsum](https://idsgn.dropmark.com/107/1458166) and [Social Good Ipsum](http://socialgoodipsum.com/#/) were used given a go in comments section.

Favicon icon links were created using a [online HMTL generator](https://codepen.io/fuzzywalrus/pen/BWWMjJ) by [Greg Gant](https://codepen.io/fuzzywalrus).

The icon is from [Icon Library](http://icon-library.com/icon/car-png-icon-16.html). The provided attribution link was flagged faulty and possibly harmful, for why I have not included the link here or on the website. The site appears to have an obsolete certification.
Attribution should go to icon-library.net.

[Back to index](#index)

## References

### Comments section in blogs

To build the comments functionality I modified the examples from these two sources to fit DOW app.
Neither of them was build on Django 3, but they gave some understanding of the principles.

- [Django Builds a Personal Blog: Comment on the Blog](https://developpaper.com/django-builds-a-personal-blog-comment-on-the-blog/).
- [Creating Comments System With Django](https://djangocentral.com/creating-comments-system-with-django/).

Comments edit and delete were build using django-bootstrap-modal-forms package, which refused to co-operate in the environment I gave it.
We did find tune together after sorting out few issues of being little different.

- [In an UpdateView with the form_valid over-written, how does django know where to redirect to?](https://stackoverflow.com/questions/47429203/in-an-updateview-with-the-form-valid-over-written-how-does-django-know-where-to).
- [DeleteView with a dynamic success_url dependent on id](https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id).

These two helped to decide what should happen with related models on delete.

- [Django: ForeignKey's on_delete handlers](https://jilles.me/django-foreignkeys-on_delete-handlers/).
- [Django database integrity: ForeignKey on_delete options](https://medium.com/@inem.patrick/django-database-integrity-foreignkey-on-delete-option-db7d160762e4).

Vote function came together with the little help from these guys.

- [what is reverse() in Django](https://stackoverflow.com/questions/11241668/what-is-reverse-in-django).
- [Django - How to make an upvote button?](https://stackoverflow.com/questions/55158202/django-how-to-make-an-upvote-button).

In my attempts to wrestle testing with Django, I studied Code Institute alumni works and more than few other sources.
From these sources I am sure I have traces in my testing code.

- [Testing in Django (Part 1) – Best Practices and Examples](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/).
- [PCSwimming](https://github.com/hschafer2017/PCSwimming).

To test error handling this stack post was most helpful.

- [How to test 500.html error page in django development env?](https://stackoverflow.com/questions/2740003/how-to-test-500-html-error-page-in-django-development-env).

To extend the django user model I asked from Victor, because Simpleisbetterthancomplex.

- [How to Extend Django User Model](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html).

[Back to index](#index)

## Special Thanks

Thank you for you patience and support my lovely family. I wish nothing more than I will have a chance to pay you back the time away from you while climbing this mountain, and to be fully present with you again.
Thank you for Code Institute tutor team who helped me sort out few hiccups on the way,
and of course Code Institute Slack community who I know go through the same ups and downs.
And heartfelt thank you for Brian Macharia for mentoring me and having my back.
