# django-rest-blog

django-rest-blog is a test application for demonstrate knowledge in the [Django framework](https://www.djangoproject.com/) and [Django REST framework](http://www.django-rest-framework.org/).

## Installation

### 1. virtualenv / virtualenvwrapper
You should already know what is [virtualenv](http://www.virtualenv.org/), preferably [virtualenvwrapper](http://www.doughellmann.com/projects/virtualenvwrapper/) at this stage. So, simply create it for your own project, where `django-rest-blog` is the name of your project:

`$ mkvirtualenv --clear django-rest-blog`

### 2. Download
Now, you need the *django-rest-blog* project files in your workspace:

    $ cd /path/to/your/workspace
    $ git clone git://github.com/gansik/django-rest-blog.git django-rest-blog && cd django-rest-blog

### 3. Requirements
Right there, you will find the *requirements.txt* file that has all the great debugging tools, django helpers and some other cool stuff. To install them, simply type:

`$ pip install -r requirements.txt`



### 4. Source of requirements.txt
```
Django>=1.9
djangorestframework>=3.3.1
```

### 5. API methods

	`/api/user/register/` - Create User
	`/api/user/api-token-auth/` - Get Auth Token
	`/api/user/profile/` - User Profile (need token)
	`/api/post/` - List of posts (need token, by page view)
	`/api/post/my/` - List of user posts (need token, by page view)

For any method with token, it can be passed in querystring like:

`/api/user/profile/?auth_token=e9f63d33591014f3915af5b36c2148f1d6cfdf3c`

For create new post, send POST request to `/api/post/` (of course, with token)
