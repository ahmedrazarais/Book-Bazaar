# Import the classes from the respective files
from seller_user_class import Seller
from buyer_user_class import Buyer
from register_class import Register
from login_class import Login
from app_executive_login import Admin_Login
from seller_manager_class import Seller_Manager
from buyer_manager_class import Buyer_Manager


# Create instances of the classes

seller_class = Seller(file="Accountsdatabase/accounts.txt", accounts=[], seller_folder="seller_folder/", buyer_folder="buyer_folder/", file_seller="")
buyer_class = Buyer(file="Accountsdatabase/accounts.txt", accounts=[], seller_folder="seller_folder/", buyer_folder="buyer_folder/",file_buyer="",file_seller="")
object=Register(file="Accountsdatabase/accounts.txt",accounts=[],seller_folder="seller_folder/",buyer_folder="buyer_folder/")
log=Login(file="Accountsdatabase/accounts.txt",accounts=[],seller_folder="seller_folder/",buyer_folder="buyer_folder/")
admin_class = Admin_Login(file="Accountsdatabase/accounts.txt", accounts=[], seller_folder="seller_folder/", buyer_folder="buyer_folder/",file_buyer="",file_seller="")
seller_manager_class=Seller_Manager(file="Accountsdatabase/accounts.txt", accounts=[], seller_folder="seller_folder/", buyer_folder="buyer_folder/",file_buyer="",file_seller="")                  
buyer_manager_class=Buyer_Manager(file="Accountsdatabase/accounts.txt", accounts=[], seller_folder="seller_folder/", buyer_folder="buyer_folder/",file_buyer="",file_seller="")


# In the main function

while True:
    # Display the main menu
    print("\t\t\tWelcome To Book-Bazaar.")
    print()
    print("\t1.Register Yourself As User.\t\t4.Login As Seller Operations Manager. ")
    print("\t2.Login As User.\t\t\t5.Login As Buyer Operations Manager.")
    print("\t3.Login As App Executive.\t\t6.To Exit From The System.")

    print()
    # Capture the user's choice
    option = input("Enter Your Desired Option: ")
    # Perform the respective operations based on the user's choice
    if option == "1":
        object.signup()
    elif option == "2":
        login_option, username = log.login()  # Capture the returned username
        # check if the user is a seller or a buyer
        if login_option == "seller":
            file_seller = "seller_folder/" + username + ".txt"
            seller_instance = Seller(file="Accountsdatabase/accounts.txt", accounts=[], seller_folder="seller_folder/", buyer_folder="buyer_folder/", file_seller=file_seller)
            # Perform seller-specific operations
            seller_instance.seller_operations()
        
        elif login_option == "buyer":
            buyer_instance = Buyer(file="Accountsdatabase/accounts.txt", accounts=[], seller_folder="seller_folder/", buyer_folder="buyer_folder/", file_buyer="", file_seller="")
            buyer_instance.set_buyer_file_path(username)  # Set the file path using the returned username
            buyer_instance.buyer_operations()
        else:
            print("Login failed. Please try again.")
    # Admin login
    elif option=="3":
        admin_class.admin_login()
  
# Seller Manager Login
    elif option=="4":
        seller_manager_class.seller_manager_login()
# Buyer Manager Login
    elif option=="5":
        buyer_manager_class.buyer_manager_login()
# Exit the system
    elif option == "6":
        print("Book-Bazaar System Exited Successfully.")
        print("Thank You For Using Book-Bazaar.")
        print()
        break   # break the loop
    else:
        print("Invalid Choice. Please Select Correct Choice.")



