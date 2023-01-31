### <ins>Task</ins> ###
**Design a Twitter-like social network website for making posts and following users.**

### <ins>Specification</ins> ###
Framework: **Django** <br>
Language: **Python, HTML, CSS, JavaScript**

**Website Function:** <br>
Implement a social network that allows users to make posts, follow other users, and “like” posts. <br>
User can also edit posts, check user profile page which displays the user's posts and followers and following counts and use pagination tabs to look through posts on other pages.

Practice Question Source: [More Info](https://cs50.harvard.edu/web/2020/projects/4/network/)

### <ins>Usage</ins> ###
User need to download Django in order to run this program via this command: `pip3 install Django`.

After downloading the package, in the terminal execute following commands to run program:
1. `cd Pset4`
2. `cd project4`
3. `python manage.py runserver`

Other commands:

- To make migrations for the `network` app, run `python manage.py makemigrations network`.
- To apply migrations to your database, run `python manage.py migrate`. <br>
  (Note: Both steps above are essential whenever changes are done to auctions/models.py.)
- To create a superuser account that can access Django’s admin interface, run `python manage.py createsuperuser`.

Since Django uses token to prevent CSRF attack, if below error message pops out upon submitting request, please copy your website link shown in error message and paste it over to settings.py file inside main folder with this line of code: CSRF_TRUSTED_ORIGIN = ['url'] where url is the link you copied.
![image](https://user-images.githubusercontent.com/107826905/215782464-feb17254-ec9d-4196-ab27-24f36a66ad51.png)

![image](https://user-images.githubusercontent.com/107826905/215782748-9e373023-b702-4ce6-b260-bfa036fa4dd2.png)

### <ins>Program Example</ins> ###
- **<ins>Main Page / All Posts</ins>**: Displays all posts posted by users but user cannot comment or like posts since not logged in to account.

  ![image](https://user-images.githubusercontent.com/107826905/215783330-1f8c2447-2c09-4cba-8e1d-953eb220babc.png)

- **<ins>Login Page</ins>**

  ![image](https://user-images.githubusercontent.com/107826905/215783659-10bb8a77-7906-4da9-835e-7533730f6e09.png)
  
- **<ins>Register New Account Page</ins>**

  ![image](https://user-images.githubusercontent.com/107826905/215783903-af0ffd60-2dac-4b2f-8ea3-bcd02bbf91fd.png)

- **<ins>Main Page (Logged In)</ins>**: Logged in user can have access to making new posts, edit own posts. They can like or unlike posts made by other users and follow other users.

  ![image](https://user-images.githubusercontent.com/107826905/215784634-f314baa7-774a-4a31-b48c-2bf04faad71d.png)
  
  ![image](https://user-images.githubusercontent.com/107826905/215787333-53528ac3-e8cf-4fe7-97bc-89b3a314b632.png)

- **<ins>Profile Page</ins>**: By clicking the username on posts, user can directed to the person's profile page and check out their posts and followers counts.

  ![image](https://user-images.githubusercontent.com/107826905/215785421-51691f45-3490-411d-8ab9-a5cbfa02b8f5.png)
  
  ![image](https://user-images.githubusercontent.com/107826905/215788155-6f2741fb-aff9-407d-9ccf-89866f348277.png)

- **<ins>Edit Function</ins>**: Logged in user can edit their own contents in the modal when clicking the edit link.

  ![image](https://user-images.githubusercontent.com/107826905/215785991-304d0371-fe9b-4dc6-96d2-ffc2bf82f218.png)
  
- **<ins>Follow Function</ins>**: Logged in user can follow other users.

  ![image](https://user-images.githubusercontent.com/107826905/215787771-8dbe9888-9986-4de2-a473-6cf9d8ac0b02.png)
  
- **<ins>Following Page</ins>**: Display all posts followed by current user.
  
  ![image](https://user-images.githubusercontent.com/107826905/215788464-38ee132b-f0fc-4e12-9c7f-a10b0f91b9d1.png)
