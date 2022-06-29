# Uses default Django developemnt server

1. Build the images and run the containers:

```dockerfile
    $ docker-compose up -d --build
```

if needed stop docker use 
```dockerfile
    $ docker-compose stop
```

### migrations:
 creating a migration
```dockerfile
    $ docker-compose exec web python manage.py makemigrations
```
applying migration
```dockerfile
    $ docker-compose exec web python manage.py migrate
```
 

#### create super-user
```dockerfile
    $ docker-compose exec web python manage.py createsuperuser
```

Test it out at http://0.0.0.0:8000/admin/ in our browser

# Manipulation with API

### CRUD image

1. method [get]

end-point 0.0.0.0:8000/api/v1/image/

2. method [post]

end-point 0.0.0.0:8000/api/v1/image/

    {
        "img": "name_your_img.png"
        "name": "any_name"
    }

return:
    
    {
        "id": int,
        "name": "any_name",
        "img": "http://0.0.0.0:8000/media/name_your_img.png"
    }    

3. method [put/patch]

(`int:pk` is the id of the image to be updated)

end-point 0.0.0.0:8000/api/v1/image/<int:pk>/

    

4. method [delete]
(`int:pk` is the id of the image to be delete)

end-point 0.0.0.0:8000/api/v1/image/delete/<int:pk>/

5. method [delete] for admin

and 5 method for admin which deletes all images

end-point 0.0.0.0:8000/api/v1/image/delete_all/


### other methods of interacting with API

`For Authentication`

end-point 0.0.0.0:8000/api-auth/login/ at brower

`For registration`

end-point 0.0.0.0:8000/registr/

    {
        "username": "your_name",
        "email": "your_email@google.com",
        "password": "yourpassword",
        "password2": "yourpassword"
    }

return:
`"Registration completed successfully" or raise`

`For info about you `

end-point 0.0.0.0:8000/about_me/