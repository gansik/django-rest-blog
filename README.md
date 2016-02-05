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

### 5. REST API methods

Create user: POST to '/user/register/'
```
{
	"email": "test@example.com",
	"password": "qwerty"
}
```

Get user token: POST to '/user/api-token-auth/'
```
email=test@example.com&password=qwerty
```

