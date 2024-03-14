# Book-Bazaar System

#### Book-Bazaar is a Python-based book-selling system that facilitates various operations related to buying and selling books. It provides functionalities for user registration, login for sellers and buyers, as well as administrative tasks for managing seller and buyer operations.

## Features

- **User Registration**: 
#### Users can register themselves as sellers or buyers by providing necessary details such as username, password, and recovery information. Additionally, both sellers and buyers have the option to register via either username or mobile number. In case a user forgets their password, they can recover it by providing the recovery information entered during registration, enabling them to reset their password.

- **User Login**:
#### Registered users can log in to the system using their credentials. Based on their role (seller or buyer), they are directed to different functionalities.In case a user forgets their password, they can recover it by providing the recovery information entered during registration, enabling them to reset their password.

- **Seller Operations**: 
#### Sellers can perform operations such as adding books for sale, managing their book inventory, and viewing sales history.sellers are able to update thier uploaded books details at any moment they also got notified when any of thier book is sold out.

- **Buyer Operations**: 
#### Buyers can browse books available for purchase, make purchases, and view their purchase history with recorded time.

- **Admin Panel**:
#### An administrative interface is available for admin users to manage seller and buyer operations. This includes assigning roles to seller and buyer operations managers and overseeing their activities.

## Components

1. **User Classes**: 
    - `Seller`: Manages seller-related operations such as adding books for sale.
    - `Buyer`: Handles buyer-related functionalities like browsing books and making purchases.
    - `Register`: Allows users to register themselves by providing necessary details.
    - `Login`: Facilitates user login by verifying credentials.
    - `Admin_Login`: Provides administrative functionalities such as assigning roles and managing operations.
    - `Seller_Manager`: Handles operations specific to managing sellers, such as viewing seller accounts and their contributions.(username:raza12,password:raza123@) But you can change username and password anytime after login as app executive.
    - `Buyer_Manager`: Manages buyer-related operations, including viewing buyer accounts and purchase history.(username:ali,password:ali1234@) But you can change username and password anytime after login as app executive.

2. **Main Functionality**: 
    - The main function of the system facilitates user interaction by presenting a menu-driven interface. Users can register, login, and perform various operations based on their roles.

3. **File Handling**: 
    - The system utilizes file handling to store user account details and book-related information. This includes storing seller and buyer details, as well as book inventory and purchase history.

## Usage

1. **User Registration**: 
    - Users can register by selecting the "Register Yourself As User" option from the main menu. They need to provide relevant details to complete the registration process.

2. **User Login**: 
    - Registered users can log in using their credentials through the "Login As User" option. Based on their role, they will be directed to the respective functionalities.

3. **Seller Operations**: 
    - Sellers can add books for sale, manage their inventory, and view sales history by logging in and selecting appropriate options.

4. **Buyer Operations**: 
    - Buyers can browse available books, make purchases, and view their purchase history after logging in to the system.

5. **Admin Panel**: 
    - Admin users can access administrative functionalities through the "Login As App Executive" option. They can assign roles to seller and buyer operations managers and oversee system operations.(App Executive username: admin , password:admin123)
    

6. **Exiting the System**: 
    - Users can exit the system by selecting the "Exit From The System" option from the main menu.

## Cloning the Repository and Running the Application

- If You clone the repository  run the `mainexecution.py` file To Run The Program.
**Note**: Ensure that the following directories and files are present in the repository:

- `Accountsdatabase` folder: Contains the `accounts.txt` file where all user account details are stored.
- `admin_credentials` folder: Contains two files, `seller_manager_acc.txt` and `buyer_manager_acc.txt`, where the credentials of the seller manager and buyer manager are stored, respectively.
- `buyer_folder`: Holds all buyer account files.
- `seller_folder`: Holds all seller files.
- `purchasedetails` folder: Holds the `purchase.txt` file where all book purchase details are stored.
- `id_file`: Holds the `id.txt` file where ID information is stored.


## Project Creator

####  [Mohammed Ahmed Raza]
#### This project is written in Python and represents my first project focusing on Object-Oriented Programming (OOP) principles.
#### For any inquiries or collaboration opportunities, feel free to reach out to me at     [razarais28@gmail.com]
