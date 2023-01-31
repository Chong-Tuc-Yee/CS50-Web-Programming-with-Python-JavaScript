### Task: ###
**Design an eBay-like e-commerce auction site that will allow users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist.”**

### Specification: ###
Framework: **Django**

**Website Function:**

- Website will display all of the currently active item listings to users.
- User can log in their own account and create their own item listings.
- Click and view details about a particular listing item.
- A category page which display only items under certain category to user.
- User can add items to their watchlist.
- Enable user to bid on items and the bid price have to be larger than starting bid price or subsequent placed bids.
- For user who created the listing, they can close the auction from the page, which makes highest bidder winner of the auction and makes listing no longer active. The page should notify winner of the auction.
- Enable user to comment on listing items and display user comments.

Practice Question Source: [More Info](https://cs50.harvard.edu/web/2020/projects/2/commerce/)

### Usage: ###
User need to download Django in order to run this program via this command: `pip3 install Django`

After downloading the package, in the terminal execute following commands to run program:
1. `cd Pset2`
2. `cd commerce`
3. `python manage.py runserver`

Other commands:
- To make migrations for the auctions app, run `python manage.py makemigrations auctions`
- To apply migrations to your database, run `python manage.py migrate` <br>
   (*Note: Both steps above are essential whenever changes are done to `auctions/models.py`.*)
- To create a superuser account that can access Django’s admin interface, run `python manage.py createsuperuser`.

### Program Example: ###
![image](https://user-images.githubusercontent.com/107826905/215714327-7ba3225b-cf74-47a0-9f74-660d9d7a746c.png)
![image](https://user-images.githubusercontent.com/107826905/215714428-4fd0b35b-fdf5-4627-b02f-7f4d02ea21f4.png)
![image](https://user-images.githubusercontent.com/107826905/215714525-3212cf96-6f7b-4afd-95b9-3d6da6351491.png)
![image](https://user-images.githubusercontent.com/107826905/215714639-3e3e7477-4d5a-4552-8ba3-e65719ded814.png)
![image](https://user-images.githubusercontent.com/107826905/215715142-b6501234-4f95-4f70-afb3-ed7ba41e49bc.png)
![image](https://user-images.githubusercontent.com/107826905/215715064-d7d9e3cf-ed81-4811-bce9-828c487b8fe5.png)
![image](https://user-images.githubusercontent.com/107826905/215715392-5a6d22fd-89e2-4231-be62-c7efc71959a2.png)
![image](https://user-images.githubusercontent.com/107826905/215715511-d4ef32fe-2ef5-4973-84a6-b81896ca2622.png)
![image](https://user-images.githubusercontent.com/107826905/215715761-58ac1709-f36c-4143-9a4b-41f7a2eeb3cc.png)
![image](https://user-images.githubusercontent.com/107826905/215716047-152a1cbe-a099-4e1a-a0f0-ccf889d4930d.png)
![image](https://user-images.githubusercontent.com/107826905/215716118-0299a847-68f1-4184-aed4-454d47fa8ef9.png)
![image](https://user-images.githubusercontent.com/107826905/215716216-aed68c89-75a6-4600-8ced-6626389c1bbf.png)
![image](https://user-images.githubusercontent.com/107826905/215716355-d65f1765-2db1-46eb-a0d8-99d5f24ed3d0.png)
![image](https://user-images.githubusercontent.com/107826905/215716450-b8c6e754-f57f-495a-8212-75a0376881b5.png)
![image](https://user-images.githubusercontent.com/107826905/215716499-aa49ecd6-0a6b-4d13-b4b7-75742e76414d.png)
![image](https://user-images.githubusercontent.com/107826905/215716565-bc432796-e9a4-467b-baa0-abffb46a9487.png)
![image](https://user-images.githubusercontent.com/107826905/215717020-5d908c24-c331-4cd8-a95b-bfb1c067b355.png)





