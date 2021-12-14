# PhotoAlbum
<h3> Photo Album in django - with S3 image Storage </h3>

At first, you must run:

```
pip install requirements.txt
```
In order to install all libs nescessary for this project to run smoothly.

After that, you should run:
```
cd WebAlbum
python manage.py makemigrations
python manage.py migrate
```
To generate a local db.sqlite3 file, which will be used as the NonRelational Database for Django.
right after, you should run 
```
python manage.py createsuperuser
```
And you will be prompted with the following questions:

> Username (leaves blank to use *****):

> Email address:

> Password:

> Password(again):

Once its done, you can run 

```
python manage.py runserver
```

But, there are a few changes you must do in order to be able to store your images in AWS S3

I'll skip the S3 Bucket Creation and Permission for now, but there will be a link here to teach you that (soon)

Well, now that you have your Bucker created, and a User able to access that Bucket, you must declare this user's credentials.

##There are two methods of doing so

### Method 1
  Declaring the credentials direclty in the settings.py file
  
in the **settings.py** file, do the following:

```
...
STATIC_URL = '/static/'

#AWS USER CREDENTIALS
AWS_S3_ACCESS_KEY_ID = 'your access key id here'
AWS_S3_SECRET_ACCESS_KEY = 'your secret access key id here'
AWS_STORAGE_BUCKET_NAME = 'your bucket name here'
AWS_QUERYSTRING_AUTH = False

...
```

### Method 2
  Creating a **.env** file, importing it in the **settings.py** file and referencig the VARIABLES to the values declared in the **.env** file
  
  In the **.env** file:
  ```
AWS_S3_ACCESS_KEY_ID=your access key id here
AWS_S3_SECRET_ACCESS_KEY=your secret access key id here
AWS_STORAGE_BUCKET_NAME=your bucket name here
```
Remember not to use any quotations mark (') ("), otherwise the environ won't be able to correctly read the Variables
And now, in the **settings.py**, do the following:

```
AWS_S3_ACCESS_KEY_ID = env("AWS_S3_ACCESS_KEY_ID")
AWS_S3_SECRET_ACCESS_KEY = env("AWS_S3_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
```

Once its done, if the bucket was correclty configured, it will run smoothly, and now you can deploy this project on Heroku, or any other CLoud Service you want ;)
Hope you enjoy this Album!
