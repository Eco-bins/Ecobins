# Ecobins
## Modules and Pages Outline:

Get DB design by downloading: [DB Design.xlsx](https://github.com/Eco-bins/Ecobins/blob/main/!%20DB%20Design.xlsx)

0. **Auth**: **`ALREADY COMPLETED`** *(Optional remake of DB design mentioned in the end)*
   - Login
   - Register
   - Forgot Password

1. **Basic**:
   - Basic Public Details
   - Posts
   - Settings
   - Book Waste Pick Up
   - **Database Tables**: 
     - `Settings`: Stores user settings (user_id, setting_name, setting_value)
     - `WastePickup`: Stores waste pickup details (pickup_id, user_id, timestamp, status)

2. **Content Creators**:
   - Home Feed
   - Upload
   - View File
   - Edit File
   - Profile
   - Notifications
   - Create Post (*Added*)
   - Edit Profile (*Added*)
   - **Database Tables**: 
     - `User`: Stores user details (username, password, email)
     - `Post`: Stores post details (post_id, user_id, content, timestamp)
     - `Notification`: Stores notification details (notification_id, user_id, message, timestamp)

3. **Marketplace**:
   - Product Page
   - Cart Pages
   - Messaging
   - Product Details (*Added*)
   - Checkout (*Added*)
   - **Database Tables**: 
     - `Product`: Stores product details (product_id, name, description, price)
     - `Cart`: Stores cart details (cart_id, user_id)
     - `CartProduct`: Stores relationship between carts and products (cart_id, product_id)

4. **Waste Disposal Service Provider**:
   - List of Bookings
   - Individual Booking Details Page
   - New Booking (*Added*)
   - Update Booking (*Added*)
   - **Database Tables**: 
     - `Booking`: Stores booking details (booking_id, user_id, timestamp, status)
     - `Service`: Stores service details (service_id, name, description)

---
## Notes
 - **No templates edited within repo**
 - Templates only to be uploaded after completion of full design without model integration.
 - No need to create branches, but always keep backup of files on your system if possible.

## Work divs
- **CORE:** Niranjan, Nitish, Ajay
- **DB Design:** Albert, Arjun
- **Templates:** Sabin, Ashin, Arun

## Assigned work
1. Niranjan - *Create modules and prepare for templates & models*
2. Albert, Arjun - *Database design (Tables needed)*
3. Sabin, Ashin, Arun - *Find templates & make the HTML/CSS pages accomodate the tables from DB Design*
4. Niranjan, Nitish, Ajay, Sabin - *Make models for tables from DB Design* (Also, teach about models in Django and creation of models)
5. _ALL_ - Model integration to templates.
6.  ... etc.

---
For the **AUTH** module, you would typically need the following tables:

1. `User`:
   - **username**: Unique identifier for each user.
   - **email**: Email address of the user.
   - **password_hash**: Hashed version of the user's password. It's important to store hashed passwords for security reasons.
   - **salt**: Random data that is used as an additional input to a one-way function that hashes the password.

2. `PasswordReset` (for handling 'Forgot Password' requests):
   - **user_id**: Identifier of the user who requested the password reset.
   - **token**: Unique token generated for the password reset request.
   - **expiry_date**: Expiry date of the token. It's a good practice to have tokens that expire to ensure they can't be misused if they are intercepted by malicious parties.

