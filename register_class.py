# This Is The Class File For Registering The Users.
# This Class Will Be Used To Register The Users.

class Register:
# This Class Will Be Used To Register The Users.
    def __init__(self,file,accounts,seller_folder,buyer_folder):
        self.file_name=file    # file name for accounts holding
        self.accounts_list=accounts    # list to hold the accounts
        self.seller_folder=seller_folder    # seller folder
        self.buyer_folder=buyer_folder     # buyer folder

   




    # Getting data from file in account list.
    def extract_data(self):
        with open(self.file_name) as file:
            for line in file: 
                # split the line and store in the list
                lines=line.strip().split("###")
                # dictionary to hold the account details
                account_dic={lines[0]:[lines[1],lines[2],lines[3],line[4]]}
                # append the dictionary to the list
                self.accounts_list.append(account_dic)


    # first name input
    def first_name(self):
        while True:
            first_name = input("Please Enter the Name (enter 0 to back):")
            if first_name=="0":   # if user wants to go back
                return
            # if the name is not empty
            new_name=[char for char in first_name if char.strip()]
            if len(new_name)>2: 
                return first_name   # return the name
            else:
                print()
                print("First Name should Contain Atleast Three Words")
                print("Enter Again")







    # password input by user
    def password_input(self):
         while True:
              password = input("Please Enter strong Password (enter 0 to back): ")                                       
              if password=="0": # if user wants to go back
                  return
            # password must contain atleast 8 characters, one special character and digit
              if any(char.isdigit() for char in password) and any(not (char.isalnum()) for char in password) and len(password) >= 8:
                print("Password set successfully.")
                print()
                return password    # return the password

              # if the password is not strong
              else:
                   print()
                   print("Password Must Conatins atleast 8 characters, one special character and digit.")
                   print()
  
    # recovery input
    def get_recovery(self):
        # taking recovery in case if user forgets the password
        recovery=input("Enter backup username (optional):")
        if len(recovery)>=1:
            return recovery
        else:
            return "*"   # if user does not want to give recovery
    

    # taking username input
    def get_user_name(self):
        self.extract_data()   #Calling the extract data function to get the data from file
        while True:
            username=input("Enter Your username To register (enter 0 to back):")
            if username=="0":   # if user wants to go back
                return
            if len(username)>1:
                # Convert username to lowercase for case-insensitive comparison
                username_lower = username.lower()
                for line in self.accounts_list:
                    if username_lower in line.keys():   # checking if the username is already taken
                        print("sorry,username is already taken.")
                        print()
                        break
                else:
                    # if username is not taken
                    print("username set successfully.")
                    return username    # return the username
            else:
                print("Please Enter User-name to register.")
    
    # taking mobile number input
    def get_number(self):
        while True:
            number=input("Enter Mobile Number To Register (enter 0 to return):").strip()
            if number=="0":
                return
            # number must contain 11 digits
            if all(char.isdigit() for char in number) and len(number)==11:
                print("valid Mobile Number.Mobile Number set.")
                print()
                return number   # return the number
            else:
                print()
                print("Please write Correct Number")
                print()

    # Taking choice from user that he want to register as seller or buyer
    def Take_choice(self):
        while True:
            print("\t\t\tWelcome To Registration Services.")
            print("\t\t1.To create Seller Account.")
            print("\t\t2.To Create Buyer Account.")
            print("\t\t3.To Exit From Registration.")
            print()
            option=input("Enter Your Option Based On These Choices:")
            if option in ["1","2"]:
                return option      # if valid input return the option
            elif option=="3":
                return
            else:
                print("Invalid Choice.")

    # This is the process of registration of seller
    def username_process_seller(self):
        seller="seller"
        # taking name input
        name=self.first_name()
        if name:   # if name is not empty
           username=self.get_user_name()
           if username:
            password=self.password_input()
            if password:
                recovery=self.get_recovery()
                # After taking all the inputs, write the data to the file
                with open (self.file_name,"a+") as file:
                    file.write(f"{username}###{name}###{password}###{recovery}###{seller}\n")
                return username
    
    # This is the process of registration of seller via number
    def number_process_seller(self):
        seller="seller"
        name=self.first_name()
        if name:
           number=self.get_number()
           if number:          
             password=self.password_input()
             if password:
                recovery=self.get_recovery()
                # After taking all the inputs, write the data to the file
                with open (self.file_name,"a+") as file:
                    file.write(f"{number}###{name}###{password}###{recovery}###{seller}\n")
                return number


    # Process of registration of buyer via username  
    def username_process_buyer(self):
        buyer="buyer"
        name=self.first_name()
        if name:
          username=self.get_user_name()
          if username:      
             password=self.password_input()
             if password:
                recovery=self.get_recovery()
                # after taking all the inputs, write the data to the file
                with open (self.file_name,"a+") as file:
                    file.write(f"{username}###{name}###{password}###{recovery}###{buyer}\n")
                return username
    
    # Process of registration of buyer via number
    def number_process_buyer(self):
        buyer="buyer"
        name=self.first_name()
        if name:
           number=self.get_number()
           if number:
             password=self.password_input()
             if password:
                recovery=self.get_recovery()
                # after taking all the inputs, write the data to the file
                with open (self.file_name,"a+") as file:
                    file.write(f"{number}###{name}###{password}###{recovery}###{buyer}\n")
                return number


    # Process of registration for sellers                        
    def process_final_seller(self):
        while True:
                #  taking choice from user he want to register via username or number
                print("\t1.Register Via Username.")
                print("\t2.Register Via Mobile Number.")
                print("\t3.To back From Registration.")
                print()
                # taking choice from user
                choice=input("Enter Your Preferred Option:")
                if choice=="1":     
                    # if user wants to register via username
                    username=self.username_process_seller()
                    # make file with the username in seller folder
                    file_path= self.seller_folder + f"{username}" + ".txt"
                    with open (file_path,"w") as file:
                        pass
                    return

                elif choice=="2":
                    # if he want to register via number
                   number=self.number_process_seller()
                   # make user file in seller folder
                   file= self.seller_folder + f"{number}" + ".txt"
                   with open (file,"w") as file:
                        pass

                   return

                elif choice=="3":
                    # If he want to go back from registration
                    print("Back From This page..")
                    break
                else:
                    print("Invalid Choice.")


    def process_final_buyer(self):
        while True:
                print("\t1.Register Via Username.")
                print("\t2.Register Via Mobile Number.")
                print("\t3.To back From Registration.")
                print()
                choice=input("Enter Your Preferred Option:")
                # if user wants to register via username
                if choice=="1":
                    username=self.username_process_buyer()
                    # make file with the username in buyer folder
                    file_path= self.buyer_folder + f"{username}" + ".txt"
                    with open (file_path,"w") as file:
                        pass
                    return

                elif choice=="2":
                   number=self.number_process_buyer()
                   # make user file in buyer folder with nuumber
                   file= self.buyer_folder + f"{number}" + ".txt"
                   with open (file,"w") as file:
                        pass

                   return

                elif choice=="3":
                    # if he want to go back
                    print("Back From This page..")
                    break
                else:
                    print("Invalid Choice.")
    # signup process
    
    def signup(self):
        # calling the take choice function
        option=self.Take_choice()
        if option=="1":
            # if user wants to register as seller
            print("Now You Can Create Your Seller Account.")
            self.process_final_seller()
        elif option=="2":
            # if user wants to register as buyer
            print("Now You Can Create Your Buyer Account.")
            self.process_final_buyer()

