### <ins>Task</ins> ###
**Design an eBay-like e-commerce auction site that will allow users to post auction listings, place bids on listings, comment on those listings, and add listings to a “watchlist.”**

### <ins>Specification</ins> ###
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

### <ins>Usage</ins> ###
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

Since Django uses token to prevent CSRF attack, if below error message pops out upon submitting request, please copy your website link shown in error message and paste it over to settings.py file inside main folder with this line of code: CSRF_TRUSTED_ORIGIN = ['url'] where url is the link you copied.
![image](https://user-images.githubusercontent.com/107826905/215715142-b6501234-4f95-4f70-afb3-ed7ba41e49bc.png)

![image](https://user-images.githubusercontent.com/107826905/215715064-d7d9e3cf-ed81-4811-bce9-828c487b8fe5.png)

### <ins>Program Example</ins> ###
- **<ins>Main Page / Active Listings Page</ins>**: Display all active listing items. User can only view items since have not logged in account yet.

![image](https://user-images.githubusercontent.com/107826905/215714428-4fd0b35b-fdf5-4627-b02f-7f4d02ea21f4.png)

- **<ins>Login Page</ins>**: Login to user's account

![image](https://user-images.githubusercontent.com/107826905/215714525-3212cf96-6f7b-4afd-95b9-3d6da6351491.png)

- **<ins>Register Page</ins>**: Register new account

![image](https://user-images.githubusercontent.com/107826905/215714639-3e3e7477-4d5a-4552-8ba3-e65719ded814.png)

- **<ins>Main Page / Active Listings Page</ins>**: Display all active listing items. Logged in user can perform certain actions.

![image](https://user-images.githubusercontent.com/107826905/215715392-5a6d22fd-89e2-4231-be62-c7efc71959a2.png)

- **<ins>Category Page</ins>**: Display only items under chosen category to user.

![image](https://user-images.githubusercontent.com/107826905/215715761-58ac1709-f36c-4143-9a4b-41f7a2eeb3cc.png)

- **<ins>Item Listing Page</ins>**: Display more info for particular item when user click on "More Details" for the item.

![image](https://user-images.githubusercontent.com/107826905/215716047-152a1cbe-a099-4e1a-a0f0-ccf889d4930d.png)
![image](https://user-images.githubusercontent.com/107826905/215716118-0299a847-68f1-4184-aed4-454d47fa8ef9.png)

- **<ins>Comment Function</ins>**: User can comment on the selected item under the item description. Comments will display for the respective items in a list.

![image](https://user-images.githubusercontent.com/107826905/215716355-d65f1765-2db1-46eb-a0d8-99d5f24ed3d0.png)

- **<ins>Bid Function</ins>**: User can place bid for the item.

![image](https://user-images.githubusercontent.com/107826905/215716450-b8c6e754-f57f-495a-8212-75a0376881b5.png)

- **<ins>Bid Function</ins>**: Messsage will be displayed on top for successful bid placing and price will be updated to the latest bid price upon successful bid.

![image](https://user-images.githubusercontent.com/107826905/215716499-aa49ecd6-0a6b-4d13-b4b7-75742e76414d.png)
![image](https://user-images.githubusercontent.com/107826905/215716565-bc432796-e9a4-467b-baa0-abffb46a9487.png)

- **<ins>Create New Listing Page</ins>**: Looged in user will be able to add in new item for listing.

![image](https://user-images.githubusercontent.com/107826905/215717020-5d908c24-c331-4cd8-a95b-bfb1c067b355.png)





