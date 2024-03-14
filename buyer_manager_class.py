import os
from app_executive_login import Admin_Login  



# making a buyer manager class that inherits from adminlogin
class Buyer_Manager(Admin_Login):
    def __init__(self, file, accounts, seller_folder, buyer_folder, file_buyer, file_seller):
        super().__init__(file, accounts, seller_folder, buyer_folder, file_buyer, file_seller)
        self.accounts_making=[]
        

    # Making a mehtod to make a list of accou ts credentials
    def accounts_list_making(self):
        with open(self.buyer_manager_file) as file:
            lines=file.read()
            # split on seperator
            data=lines.strip().split("$$$")
            return data

    # mehtod  to login as buyer manager
    def buyer_manager_login(self):
         with open(self.buyer_manager_file) as file:
           lines=file.read()
           if not lines: # If buyer managaer file is empty then return
               print()
               print("You are Not Able To Access Buyer manager Portal.")
               print("Might Be The App Executive Not Assign someone For This Post.")
               print()
               return        
           if lines:
               # If file is not empty then taking input of credentials
               found=False
               data=self.accounts_list_making()
            
               print("Now Dear Manager of Buyer Operations,Please Login With provided credentials.")
               print()
               while True:
                # Taking input of username of buyer manager
                   buyer_manager_username=input("Enter Username Provided By App Executive (entr 0 to back):")
                   if buyer_manager_username=="0":
                       return
                   # if username matches then take password input
                   if buyer_manager_username==data[1]:
                       print()
                       print("Username Is Correct,Kindly Enter Password For Further Process.")
                       print()
                       break
                   else:
                       print()
                       print("Invalid Buyer Operations Manager username.")
                       print()
               while True:
                # taking input of password
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
                # if login successfull then call the buyer operations manager
               if found:
                   self.buyer_operations_manager()

    
    def account_exctraction(self):
        self.accounts_making = []  # Clear the list before populating it
        with open(self.file_name) as file:
            for line in file:
                parts = line.strip().split("###")
                if len(parts) >= 5:  # Ensure line has at least 5 parts
                    if parts[4] == "buyer":
                        accounts = {"name": parts[0], "username": parts[1], "password": parts[2], "recovery": parts[3], "accounttype": parts[4]}
                        self.accounts_making.append(accounts)            
    

    # Mehtod to see specific buyer history
    def see_specific_buyer_history(self):
        self.see_all_buyers_accounts()
        print()
        while True:
            print()
            # taking input of buyer username to show his history
            user_name=input("Enter User-name Of Buyer To See His Particpation (enter 0 to back):")
            if user_name=="0":
                return
            # Checking if file exists in folder or not
            file_path_check = os.path.join(self.buyer_folder, f"{user_name}.txt")
            # If file exists then check file is empty or not
            if os.path.exists(file_path_check):
                with open(file_path_check) as file:
                    lines=file.read()
                    if not lines: # If file is empty
                        print()
                        print(f"You Come so early There Are no books to show ,The Buyer {user_name} doesn't add any books yet!")
                        print()
                    else:
                        print() # If file is not empty then show the history
                        print(f"\t\t\tThat Is Complete Details Of Purchase History of {user_name} ")
                        print(lines)
           
            else: # If file not exists then show the message
                print()
                print(f"Buyer File Not Found.Please Enter Valid Username")
                print()
                # Handle the case where the
  

    # mehtod to show all the purchases done by buyers
    def view_all_purchases(self):
        with open(self.booking_file) as file:
            lines=file.read()
            if not lines: # If no book is purchased yet then show the message
                print("No Book Has Been Purchased Yet By any Buyers!!")
                print()
                return
            else:
                # If books are purchased then show the history
                print(lines)
                print()


    # Mehtod to search any buyer
    def search_any_buyer(self):
        self.account_exctraction()
        if len(self.accounts_making)>=1:
            user_name_fix="name"
            while True:
                # taking input of username to search
                get_username=input("Enter User-Name To Search (enter 0 to back):")
                if get_username=="0":
                    return
                for dictionaries in self.accounts_making:
                    # if username matches then show the details
                    if dictionaries[user_name_fix]==get_username:
                        print()
                        print("\t\tHere Is The Credetntials Details Of That Person")
                        print()
                        print(f"1.username: {dictionaries["name"]}\n2.Name: {dictionaries["username"]}\n3.Password: {dictionaries["password"]}\n4.Recovery: {dictionaries["recovery"]}")
                        print()
                        return
                else:    # if invalid username then show the message
                    print("Invalid User-Name,No Seller Found With That Username.")
                    print()
                
        else:       # if no buyer is registered yet then show the message
            print("No Sellers Has Open Thier account Yet!!")        
            return


    #mehtod to see all buyer account
    def see_all_buyers_accounts(self):
        self.account_exctraction()
        # If any buyer account is registered then show the details
        if len(self.accounts_making) >= 1:
            print("\tHere Are All The Buyers Credentials Details")
            print()
            print("{:<20} {:<20} {:<20} {:<20} {:<20}".format("User-Names", "Names", "Passwords", "Recovery", "Account-Type"))
            print("=" * 100)  # Separator line
            for account in self.accounts_making:
                name = account["name"]
                user_name = account["username"]
                password = account["password"]
                recovery = account["recovery"]
                account_type = account["accounttype"]
                print("{:<20} {:<20} {:<20} {:<20} {:<20}".format(name, user_name, password, recovery, account_type))
        # If no buyer account is registered then show the message
        else:
            print("No Buyers Have Opened Their Account Yet!")
            print()

    # mehtod to manage the buyer operations
    def buyer_operations_manager(self):
        while True:
            # display the menu
            print("\t\t\tWelcome To The Portal Of Buyer Manager Operations.")
            print("\t1.See All Buyer Accounts Credentials.\t\t4.View All Bookings By Buyers..")
            print("\t2.Add Any Buyer Account.\t\t\t5.View Any Specific Buyer History.")
            print("\t3.Search any specific Buyer account.\t\t6.To Exit: Exit From Seller manager operations.")

            print()
            print()
            # taking input of choice
            manager_buyer_choice=input("Dear Buyer manager Please Enter Desirable choice:").strip()
            # calling the respective mehtod based on the choice
            if  manager_buyer_choice=="1":
                print()
                self.see_all_buyers_accounts()
               

            elif  manager_buyer_choice=="2":
                print("Now You Can Add Any Buyer Account With its credentials.")
                self.process_final_buyer()
                

            elif  manager_buyer_choice=="3":
               print("Search any specific Buyer simply by entering thier username.")
               print()
               self.search_any_buyer()
            
            elif  manager_buyer_choice=="4":
                print("Here You can able to see all the Purchase details that are available at that moment Done By Differnt Buyers.")
                print()
                self.view_all_purchases()
               

            elif  manager_buyer_choice=="5":
                print("This is area where you can see any specific Buyer Purchase History.")
                print()
                print()
                print()
                self.see_specific_buyer_history()

            elif  manager_buyer_choice=="6":
                print()
                print("Thank you for your dedicated service as our Manager of Buyer Operations.")
                print("Hope You Got Satisfied With our services.")
                print()
                print()
                return  # If buyer manager wants to exit then return
