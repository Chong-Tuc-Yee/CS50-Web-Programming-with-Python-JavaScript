### <ins>Task</ins> ###
**Design a front-end for an email client that makes API calls to send and receive emails.**

### <ins>Specification</ins> ###
Framework: **Django** <br>
Language: **HTML, CSS, JavaScript**

**Website Function:** <br>
Enable user to get mails, send mails, update mails, archive and unarchive emails and reply emails using the application's API.

Practice Question Source: [More Info](https://cs50.harvard.edu/web/2020/projects/3/mail/)

### <ins>Usage</ins> ###
User need to download Django in order to run this program via this command: `pip3 install Django`

After downloading the package, in the terminal execute following commands to run program:
1. `cd Pset3`
2. `cd mail`
3. `python manage.py runserver`

Other commands:
- To make migrations for the `mail` app, run `python manage.py makemigrations mail`.
- To apply migrations to your database, run `python manage.py migrate`. <br>
  (Note: Both steps above are essential whenever changes are done to mail/models.py.)
- To create a superuser account that can access Django’s admin interface, run `python manage.py createsuperuser`.

Since Django uses token to prevent CSRF attack, if below error message pops out upon submitting request, please copy your website link shown in error message and paste it over to settings.py file inside main folder with this line of code: CSRF_TRUSTED_ORIGIN = ['url'] where url is the link you copied.
![image](https://user-images.githubusercontent.com/107826905/215766258-078c54e6-d83f-4b57-9830-b44491bc141d.png)
![image](https://user-images.githubusercontent.com/107826905/215766756-d2dbbc68-b14a-49e8-96fb-e2840cb1248a.png)

### Program Example: ###
- **<ins>Login Page</ins>**

![image](https://user-images.githubusercontent.com/107826905/215767037-d1cc5e35-e57e-449d-8cf3-edefc8fcac87.png)

- **<ins>Register New Account</ins>**

![image](https://user-images.githubusercontent.com/107826905/215767148-9b1e9d98-007c-4b4c-b1f8-d7e2941a7ab4.png)

- **<ins>Compose Email</ins>**

![image](https://user-images.githubusercontent.com/107826905/215768355-00a211e4-b704-4e5c-b9e1-bb2fdac20d72.png)

- **<ins>Sent Email</ins>**: Unread messages have white background, read messages have grey background

![image](https://user-images.githubusercontent.com/107826905/215768683-63a88d78-4375-45f8-92ab-7fb0ed3610a7.png)

- **<ins> Email Details</ins>**: Click into emails inside inbox or sent email will show email content details and contain buttons for user to reply and archive/unarchive the message.

![image](https://user-images.githubusercontent.com/107826905/215769051-7c2b075c-9541-4333-b49f-9d700ae00923.png)


- **<ins>Inbox Email</ins>**: Unread messages have white background, read messages have grey background

![image](https://user-images.githubusercontent.com/107826905/215769718-2976c16d-96a6-43c4-801a-21af257913bf.png)


- **<ins>Reply Email</ins>**

![image](https://user-images.githubusercontent.com/107826905/215769917-57c096f4-e6b4-4ed8-932f-e8c808375876.png)


- **<ins>Archive Email</ins>**: Clicking archive button will send email to archive mailbox and vice versa.

![image](https://user-images.githubusercontent.com/107826905/215770101-636d61d6-5b72-4daf-93ea-8b4bce726478.png)


