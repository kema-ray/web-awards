# Web-Awwards

#### Author: [Rachel Oyondi](https://github.com/kema-ray)


* Link to live site: [Web-Awwards]()

## Description

## User Stories
As a user I would like to:

## User Story  
  
* A user can view posted projects and their details.  
* A user can post a project to be rated/reviewed. 
* A user can rate/ review other users' projects.  
* Search for projects.  
* View projects overall score.
* A user can view their profile page. 


## Specifications

| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| Login	if already have an account |if you don't have , click on the sign up link and fill the form  | If login is successful, user is navigated to home page | Signs In/ Signs Up |
| Edit profile | On the account link, click on the   profile to update| Redirected to the profile page |
| Click on profile | Redirects to the profile page | User adds bio and profile picture |
|Add a new project|Click on the add project icon to be redirected to the new post form|the post will be rendered to the home page
| Click on log Out in the accounts| Redirects to the login form | Logs out user  |

## Setup and installations
* Fork the data onto your own personal repository.
* Clone Project to your machine
* Activate a virtual environment on terminal: `source virtual/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3.8 manage.py runserver`
* Access the live site using the local host provided



## Getting started

### Prerequisites
* python3.8
* virtual environment
* pip

#### Clone the Repo and rename it.
```bash
git clone https://github.com/kema-ray/web-awards.git
#### Initialize git and add the remote repository
```bash
git init
```
```git
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment
```git
python3.8 -m virtualenv virtual
```

```git
source virtual/bin/activate
```

#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations

* python3.8 manage.py check
* python manage.py makemigrations myawwards
* python3.8 manage.py sqlmigrate myawwards 0001
* python3.8 manage.py migrate


#### Run the app

python3.8 manage.py runserver


## Testing the Application
`python manage.py test myawwards`
        
## Built With

* Python3.8
* Django 4.0.5
* Postgresql 
* Boostrap
* HTML
* CSS


## Support and contact details
 Incase you come across errors, have questions, ideas ,concerns, or want to contribute to the application, feel free to reach me at :rachelkemuma99@gmail.com

### License

MIT License

Copyright (c) 2022 Rachel Oyondi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.