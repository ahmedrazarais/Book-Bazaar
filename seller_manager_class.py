import os           # import admin login from appexeceutive file
from app_executive_login import Admin_Login





# selleer manager class that inherits from admin login
class Seller_Manager(Admin_Login):
    def __init__(self, file, accounts, seller_folder, buyer_folder, file_buyer, file_seller):
        super().__init__(file, accounts, seller_folder, buyer_folder, file_buyer, file_seller)
        self.fix=[]    # Initial Empty List as attribute

    # Mehtod To take input from the user
    def account_list(self):
        with open(self.seller_manager_file) as file:
            lines=file.read()
            # split on seperator
            data=lines.strip().split("$$$")
            return data



    # mehotd to seller manager login
    def seller_manager_login(self):
         with open(self.seller_manager_file) as file:
           lines=file.read()
           if not lines: # checking that credentials must be in  file if not then return
               print("You are Not Able To Access Seller manager Portal.")
               print("Might Be The App Executive Not Assign someone For This Post.")
               return        
           if lines:
            # if getting lines in file then taking input of credentials
               found=False
               data=self.account_list()
            
               print("Now Dear Manager of Seller Operations,Please Login With provided credentials.")
               print()
               while True:
                # taking username and password input by seller manager
                   seller_manager_username=input("Enter Username Provided By App Executive (entr 0 to back):")
                   if seller_manager_username=="0":
                       return
                   # if username matches then take password input
                   if seller_manager_username==data[1]:
                       print()
                       print("Username Is Correct,Kindly Enter Password For Further Process.")
                       print()
                       break
                   else:
                       print()
                       print("Invalid Seller Operations Manager username.")
                       print()
               while True:
                # taking password input
                   password=input("Enter Password Provided By App Executive (entr 0 to back):")
                   if password=="0":
                       return
                    # if password matches then login successfull
                   if password==data[2]:
                       print()
                       print("Login Successfull!")
                       print("Now You can Eligible To Access The Portal")
                       print()
                       found=True
                       break

                   else:
                       print("Invalid Password.")
               if found:
                   # if login successfull then call the seller manager operations
                   self.seller_operations_manager()

    def account_exctraction(self):
        self.fix = []  # Clear the list before populating it
        with open(self.file_name) as file:
            for line in file:
                parts = line.strip().split("###")
                if len(parts) >= 5:  # Ensure line has at least 5 parts
                    if parts[4] == "seller":
                        accounts = {"name": parts[0], "username": parts[1], "password": parts[2], "recovery": parts[3], "accounttype": parts[4]}
                        self.fix.append(accounts)            
    
    # mehtod to see all seller account
    def see_all_sellers_accounts(self):
        self.account_exctraction()
        # checking that list must cointain any account
        if len(self.fix) >= 1:
            # if any account found then print all the details of seller
            print("\tHere Are All The Sellers Credentials Details")
            print()
            print("{:<20} {:<20} {:<20} {:<20} {:<20}".format("User-Names", "Names", "Passwords", "Recovery", "Account-Type"))
            print("=" * 100)  # Separator line
            for account in self.fix:
                name = account["name"]
                user_name = account["username"]
                password = account["password"]
                recovery = account["recovery"]
                account_type = account["accounttype"]
                print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(name, user_name, password, recovery, account_type))
        else:    # if no selleres accounts in file
            print("No Sellers Have Opened Their Account Yet!")
            print()

     # mehtod to search any user bu entering its username
    def search_any_seller(self):
        self.account_exctraction()
        # checking that in list must be something
        if len(self.fix)>=1:
            user_name_fix="name"
            while True:
                # taking username to disoplay its details
                get_username=input("Enter User-Name To Search (enter 0 to back):")
                if get_username=="0":
                    return
                for dictionaries in self.fix:
                    # If username matches then print its details
                    if dictionaries[user_name_fix]==get_username:
                        print()
                        print("\t\tHere Is The Credetntials Details Of That Person")
                        print()
                        print(f"1.username:{dictionaries["name"]}\n2.Name: {dictionaries["username"]}\n3.Password: {dictionaries["password"]}\n4.Recovery: {dictionaries["recovery"]}")
                        print()
                        return
                else: # If Invalid username 
                    print("Invalid User-Name,No Seller Found With That Username.")
                    print()
                
        else: # if no dictionary in list
            print("No Sellers Has Open Thier account Yet!!")        
            return



    # Mehtod of any specific seller contribution
    def see_specific_seller_participation(self):
        # calling the mehtod to show all selllers accounts details
        self.see_all_sellers_accounts()
        print()
        while True:
            print()
            # Taking useranme input
            user_name=input("Enter User-name Of Seller To See His Particpation (enter 0 to back):")
            if user_name=="0":
                return
            # Checking that file exist in seller folder or not
            file_path_check = os.path.join(self.seller_folder, f"{user_name}.txt")
            if os.path.exists(file_path_check):
                # if file exists then checking in file something or not
                with open(file_path_check) as file:
                    lines=file.readlines()
                    if not lines:   # If not lines
                        print(f"You Come so early There Are no books to show ,The Seller {user_name} doesn't add any books yet!")
                        print()
                    else:
                        # If seller contributed something
                        print(f"\tHere Are the Books That {user_name} Upload For Sell.")
                        print()
                        print("{:<5} {:<15} {:<15} {:<15} {:<15} {:<15} {:<10}".format("ID", "Books-Name", "Authors", "Edition", "Book-Price","Status","Book Sold-Status"))
                        print("="*100)  # Separator line
                        for line in lines:
                            # Split the line into parts
                            parts = line.strip().split("+++")
                            if len(parts) >= 6:  # Check if there are at least 6 parts
                                id, book_name,author, edition, rent_price,status,book_status = parts[:7]  # Take only the first six parts
                                print("{:<5} {:<15} {:<15} {:<15} {:<15} {:<15} {:<10}".format( id, book_name,author, edition, rent_price,status,book_status ))
                            else:
                                print(f"Invalid data format: {line.strip()}")  # Print error message for invalid data

                
                
            else:
                print() # If File not found
                print(f"Seller File Not Found.Please Enter Valid Username")
                print()
                # Handle the case where the file does not exist













    # mehtod That manages all seller manager operations
    def seller_operations_manager(self):
        while True:
            # Display the main menu
            print("\t\t\tWelcome To The Portal Of Seller Manager Operations.")
            print("\t1.See All Seller Accounts Credentials.\t\t4.View Books Uploaded by Sellers..")
            print("\t2.Add Any Seller Account.\t\t\t5.View Any Specific Seller Participation.")
            print("\t3.Search any specific Seller account.\t\t6.To Exit: Exit From Seller manager operations.")

            print()
            print()
            # taking seller manager choice
            manager_seller_choice=input("Dear Seller manager Please Enter Desirable choice:").strip()
            # calling the mehtod according to the choice
            if manager_seller_choice=="1":
                print()
                self.see_all_sellers_accounts()

            elif manager_seller_choice=="2":
                print("Now You Can Add Any Seller Account With its credentials.")
                self.process_final_seller()
        

            elif manager_seller_choice=="3":
               print("Search any specific seller simply by entering thier username.")
               print()
               self.search_any_seller()
        
            elif manager_seller_choice=="4":
                print("Here are all the books details that are available at that moment uploaded by different sellers")
                print()
                self.view_available_books()

            elif manager_seller_choice=="5":
                print("This is area where you can see any specific seller participation")
                print()
                self.see_specific_seller_participation()
                print()
                print()

            elif manager_seller_choice=="6":
                print("Thank you for your dedicated service as our Manager of Seller Operations.")
                print("Hope You Got Satisfied With our services.")
                print()
                return         # If seller manager wants to return






