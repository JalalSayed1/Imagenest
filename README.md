# Imagenest team project

Web App Dev's team project in Level 2 - semester 2

## External sources used:
- [Bootstrap](https://getbootstrap.com/)

## How to use:
Using terminal line:
- Navigate to project location (folder where manage.py is located): `cd <Workspace>`
- Install project requirements in your machine or in a virtaul enviroment: `pip install -r requirements.txt`

Then you have 2 options:
- Make migrations and create new database: `python manage.py makemigrations imagenest && python manage.py migrate` ; or
- Run population script and populate the project with some predefined users and images data: `pyhton populate_imagenest.py`

Then, to run the project:
```
python manage.py runserver
```
To create a super user: `python manage.py createsuperuser`

## App overview:
- The app will allow registered users to upload, like, and view images like a social media application.
- Any user must create an account and be logged in to use the app.
- Users will be able to upload images to their profile page and view other people’s pages through the search page.
- They will be able to like a picture on someone’s page and the number of likes a picture has received will be visible beside the image.
- The top 10 most liked pictures on the whole website will be displayed on another page.

## Specification:
- User must be able to create an account.
- User must be able to log in/out of an account.
- User must be able to upload an image when logged in.
- Users must be able to view the top 10 most liked images and the posters username when logged in.
- Users must be able to like photos uploaded by others when logged in.
- Users must be able to search for other users by their username when logged in.
- Users should be able to view other users’ pictures when logged in.
- Users should be able to view the most recent users to like an image alongside the number of likes when logged in.
- Users should be able to navigate the website using the navigation bar (consistent throughout) when logged in.

## System architecture diagram:
![image](https://user-images.githubusercontent.com/92950538/159325820-df09e58e-7589-4df2-bbbc-143d0866c7d9.png)

## ER diagram:
![image](https://user-images.githubusercontent.com/92950538/159325900-8627724f-0033-4ebc-b24b-9448e33602bf.png)

## Sitemap:
![image](https://user-images.githubusercontent.com/92950538/159325966-cb55358c-f9a2-4c4a-9c1a-fe26da4a325e.png)

## Site URL’s:
- /Register
- /Login
  - /Home
  - /AddPicture
  - /Profile
  - /AddPicture
  - /EditProfile
  - /TopImages
  - /AddPicture
  - /SearchPage
  - /Logout

