# DreamsOnWheels

## Travis

[![Build Status](https://travis-ci.com/Junon72/DreamsOnWheels.svg?branch=master)](https://travis-ci.com/Junon72/DreamsOnWheels)

## Exclusive model cars e-commerce site

Heroku App:

Heroku git:

GitHub: https://github.com/Junon72/DreamsOnWheels

The project was created as Milestone project for the Full Stack Development module in  Code Institute run Full Stack Web Development course program.

---

## Index

1. [Project brief](#Project-brief)
2. [UX](#UX)
3. [User stories](#User-stories)
4. [Planning](#Planning)
5. [Database schema](#Database-schema)
6. [Functional flow and Features](#Functional-Flow-And-Features)
7. [Accessing the app](#Accessing-the-app)
8. [Technologies Used](#Technologies-Used)
9. [Project Setup](#Project-Setup)
10. [Testing](#Testing)
11. [Media and Content Origin](#Media-and-Content-Origin)
12. [References](#References)
13. [Special Thanks](#Special-Thanks)

## Project brief

**DreamsOnWheels** is an e-commerce site for exclusive model car collectables.

The site sells dreams in form of model cars:

- as a gift for a car lover
- as a reminder of a goal to own the real dream car
- to add to the collection of other dreams cars
- to decorate the empty place on a shelve with something classy
- to adore

For the project I will combine two suggestions provided for the project:

*Project Idea 0*

Bring your own idea(s) to life, based on providing value to users to address a specific real or imagined need.
And a modified.

*Project Idea 2*

Build an e-commerce place to sell collectable items

**External user’s goal:**

- Find, learn about and acquire collectable items they are interested in

**Site owner's goal:**

- Earn money on selling collectables (the site owner is the seller) and share the passion with other enthusiasts.

**Potential features to include:** 

- Create an online store focused on selling exclusive collectable items. In this case model cars from real dream cars.

- Allow users to search for artifacts based on various fields.

- Allow users to see the price, image and other basic details about a collectable.

- Users would be able to learn about the original dream car and its history.

- Allow users to vote for a model, they would like to see promoted. Users have to be registered for this.

**Advanced potential feature (nice-to-have)**

- Allow registered users to write comments to the blogs about dream cars and models.

- Expand the search functionality to allow users to sort results based on price and other parameters in both ascending and descending order.

- Include pagination and/or other dynamic display actions using javascript.

- Use javascript polling to update the page whenever there's a new vote.

## Project Overview

DOW - DreamsOnWheels user is able to:

- Create an account with a username and password
- Sign-in with a registered username and password
- Reset password
- Create a profile
- Search models cars by make, model and other terms, and order them by price or build year.
- View details about the car models
- Vote for a monthly highlighted dream car to be promoted or taken in to the collection
- Read about the original cars behind the models
- Read blogs
- Comment on blogs
- Add collectables in a shopping cart
- View shopping cart
- Purchase items in their shopping cart

## Who is this application for?

The application is for dream car and model car enthusiasts

### Possible users types

### User stories

## Planning

## Database Schema

## Functional flow and Features

Navigation bar is visible on all pages.

Before login user has access to:  Sales, Blogs, This month (Car highlight of the month) Login (+ Reset password), Register (and create a user profile) and Shopping cart

After login user has access to: Sales, Blogs, This month (Car highlight of the month), Shopping cart Logout, Comment on This month (Car highlight), Comment on blogs, Profile (View, Edit, Delete user)

The site has following pages and features

1. **Landing page/ Home**

Header section

- Logo
- Hero image

About section

- What is the site about in nutshell

Sales preview section

- Carousel of items on sale
- Back/ forward carousel nav

Car Highlight preview section

- Image (right)
- Title
- Text
- Button to view the page

Blogs preview section

- Image (left)
- Title
- Text
- Button to view the page

2. **Sales**

Header section

- Logo
- Extra navigation to home

Search filter:

- product by name/ price/ brand

*Model cars in sale (cards - full width. In rows)*
Item card:
Section left

- Image
- Price
- Add to cart button (adding an item to cart requires login)

Section Right

- Title
- Text (info about the model, specs)
- Read about original button ( opens a modal)

Writing about the original car (modal - full screen)

User can read about the actual car the model is made from, with an actual price range of a real car

- Image
- Title
- Text
- Close button

 3. **This month (Car highlight)**

Header section

- logo
- Extra navigation to home

Highlight section

- Title
- Image
- Text
- Open comments button
- Comments counter in button

User engagement section (login required)

Allows user to vote for the car. If aim is reached at the end of the month, the car model will be added to the sales with a promo, or promo will be added to the highlighted car already in sales items to boost sales and enhance user engagement.

- Vote up button
- Vote down button
- Vote counter
- Aim

Leave a comment section

Allows user to leave comments about the car and other users comments (chat) to enhance user engagement.

- Leave a comment form
- Submit comment button
- Edit comment form/ Save comment button

Question: Is vote feature a model or a view function?

4. **Blogs**

Header section

- Logo
- Extra navigation to home

Blog carts (columns)

- Image
- Title
- Text excerpt
- See more button

5. *Blog*

Navigation back to Blogs

Blog section

- Title
- Image
- Text

User engagement section (login required)

Leave a comment

- Leave a comment form
- Submit comment button
- Edit comment form/ Save comment button

6. **Profile** (login required)

Header section

- Logo
- Extra navigation to home

Profile section

- Edit profile form
- Attach profile image
- Save profile button
- Delete profile button

Confirm deletion dialogue modal

- Cancel button
- Delete button

7. **Login**

Header section

- Logo
- Extra navigation to home

Login section

- Login form
- Submit button
- Reset password link

8. **Reset password**

Header section

- Logo
- Extra navigation to home

Reset password section

- Reset password form
- Submit button

9. **Register**

Header section

- Logo
- Extra navigation to home

Registration section

- registration from
- submit button

10. **Cart** (Login required)

Header section

- Logo
- Extra navigation to home

Cart section

Selected items in cards

- Image
- Title
- Unit price
- Quantity form
- Modify order button
- Total price

Make purchase section

- Total of totals
- Make purchase button
- Back to sales button

11. **Payment** (Login required)

Header section

- Logo
- Extra navigation to home

Stripe payment

- Payment form
- Submit payment button
- Back to cart button

12. Logout takes the user back to Home page

## Accessing the app

## Features and functions planned but not implemented yet

## Technologies Used

## Project Setup

### Setting up IDE

The project was developed using [VSCode IDE](https://code.visualstudio.com/ "VSCode IDE") with Mac OS High Sierra operating system.
For the version control, the code was pushed to local git repository and then to [GitHub](https://github.com/ "GitHub") repository. The application was then auto-deployed through [Heroku](https://www.heroku.com "Heroku") from the GitHub Master.

To work with python, Python3 library has been first installed locally to the root directory with [Homebrew package manager](https://brew.sh/ "Homebrew package manager"). [Install Homebrew](https://brew.sh/#install "Install Homebrew") has instructions how to install brew to Mac.

To check if and which version of Python you have installed (Mac comes Python2 preinstalled) globally, you can open the Terminal and type:

`$ python --version`  # this will normally give you the version of python2 unless you have Python3 already installed.

To see if you have Python3 installed, type:

`$ python3 --version`

I wrote the application using Python3.7.6.

### Setting up git for version control and connecting to GitHub

For version control I have used GirHub open source version control system. You can also yous Git or any other version control system provider. To make a GitHub account you can [follow the instructions here](https://help.github.com/en/github/getting-started-with-github).

It is good to acknowledge the fact that [from 2020 January on, Python2 does not receive further official support](https://wiki.python.org/moin/Python2orPython3 "from 2020 January on, Python2 does not receive further official support"). Here you can find instructions [how to install the latest version of Python on your Mac](https://docs.python-guide.org/starting/install3/osx/ "how to install the latest version of Python, or to upgrade to Python3").

VSCode uses Python interpreter extensions to read Python code. Extensions include helpful features for the developers, such as [editing helpers, debugging, linting and testing.](https://code.visualstudio.com/docs/python/python-tutorial "editing helpers, debugging and linting.").

Application uses Python libraries and package modules to accomplish the needed functions. After setting up the IDE to your liking, and creating your working directory, but before starting to code and using Python modules, it is important to isolate your development environment. Otherwise, there might rise conflicts between different package versions you might use for different Python projects. Python3 comes with a build in tool 'venv' to create a [virtual environments](https://realpython.com/python-virtual-environments-a-primer/ "virtual environments") for this purpose.

To create a virtual environment in VSCode on Mac, in VSCode Terminal type:

`$ python3 -m <virtual_environment_folder_name>`

This will create a virtual environment folder to the root directory of your project.
Often the folder is named either env, venv or .venv, but you can name the folder to your liking. I used foo.

The folder contains the following sub-folders:

- bin: files that interact with the virtual environment
- include: C headers that compile the Python packages
- lib: a copy of the Python version along with a site-packages folder where each dependency is installed

To activate the virtual environment, type:

`$ source <virtual_environment_folder_name>/bin/activate`

This will activate the environment. After activation you will see the environment name in brackets front of the command line in which context the system now operates.

`(<virtual_environment_folder_name>) $`

Now the Python version is run from the virtual environment file, rather than from the global install and the Python packages imported using pip3 are isolated to the this environment only.

To exit the environment type:

`$ deactivate` which will return back to the 'system' context.

You would want to do the development work in your virtual environment! From Python3.6 on this is the recommended method of using virtual environments.

### Creating a local git repository

In virtual environment initialize a local git:

`git init` # creates a git file for the project.

Add README.md file:

`git add README.md`

Before adding the files on the workspace to the repository create a .git ignore file. In .gitignore add files folders you do not want to be pushed to the GitHub or be seen by public. Such files include VSCode settings, environment files, database and files containing sensitive information, like secret keys, passwords etc.

You can create a .gitignore file by typing:

`echo '<virtual_environment_folder_name>' > .gitignore`

As this is a Django project, I used [Gitignore pages](#https://www.gitignore.io/) to produce .gitignore file specifically for Django, which I copied and pasted to the .gitignore file.
VSCode specific settings I copied from [ofthelit GitHub pages](#https://github.com/github/gitignore/blob/master/Global/VisualStudioCode.gitignore).

After adding Django and VSCode files and folder to the .gitignore file, stage and commit the current file, byt typing:

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

I have installed VSCode GitHub extension, which makes committing changes slightly easier, by skipping username and password inquiry with each new commit.

### Installing packages

To install packages to your environment you need to update your pip, which is a Python package installer:

`pip install --upgrade pip`

Install Django:

`pip3 install Django`

To help with code writing and for Python pep compliance I installed pep8, autopep8 and pylint packages:

`pip3 install pep8 autopep8 pylint`

At this point it is good to create the requirements file, which will be updated regularly after installing new packages while developing the application:

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

If you click bin, you will find the packages you have installed from there

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

## Testing

## Media and Content Origin

## References

## Special Thanks





