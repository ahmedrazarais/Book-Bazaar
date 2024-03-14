from register_class import Register



class Login(Register):
    def __init__(self, file, accounts, seller_folder, buyer_folder):
        super().__init__(file, accounts, seller_folder, buyer_folder)
        self.extraction_of_accounts=[]

    def extrcation_accounts_from_file(self):
        self.extraction_of_accounts=[]
        with open(self.file_name) as file:
            for line in file:
                lines=line.strip().split("###")
                account_dictionary={lines[0]:[lines[1],lines[2],lines[3],lines[4]]}
                self.extraction_of_accounts.append(account_dictionary)
            return self.extraction_of_accounts            
      
            

    def take_input(self):
        while True:
            print("\t\t\tWelcome To Login Section Of Book-Bazaar-System.")
            print("\t\t1.Login As Seller.")
            print("\t\t2.Login As Buyer.")
            print("\t\t3.To Exit From Login Section.")
            choice = input("Enter Your Choice:")
            if choice in ["1", "2"]:
                return choice
            elif choice == "3":
                return
            else:
                print("Invalid choice. Please Enter Correct Choice.")

    

    def process_login(self):
        self.extrcation_accounts_from_file()
       
        while True:
            username = input("Enter username or Mobile number For Login (enter 0 to back):")
            if username == "0":
                return
            found = False

            for line in self.extraction_of_accounts:
                if username in line.keys():
                    found = True
                    stored_password = line[username][1]

                    while True:
                        password = input("Enter Password For Login (enter 0 to back):")
                        if password == "0":
                            return
                        if password == stored_password:
                            print()
                            print("Wait While We Check For Credentials...")
                            print()
                            return username  # Returning the username if login is successful
                        else:
                            print("Oops, Invalid Password.")
                            print()
                            ask_for_change = input("Did You Forget password (Y/N):").lower()
                            while ask_for_change not in ["y", "n"]:
                                print("Please Enter Correct Word.")
                                print()
                                ask_for_change = input("Did You Forget password (Y/N):").lower()
                                print()

                            if ask_for_change == "n":
                                pass
                            else:
                                if line[username][2] != "*":
                                    print()
                                    recovery_input = input("Enter Your Recovery User-Id (enter 0 to back):")
                                    if recovery_input == "0":
                                        return
                                    if recovery_input == line[username][2]:
                                        print("Alright Now Reset Password.")
                                        print()
                                        new_password = self.password_input()
                                        line[username][1] = new_password  # Update the password in the accounts list
                                        print()
                                       
                                        # Write back to file updated/ data
                                        with open(self.file_name, 'w') as file:
                                            for dictionary in self.extraction_of_accounts:
                                                for key, value in dictionary.items():
                                                    file.write(key + '###')
                                                    for item in value:
                                                        file.write(str(item) + '###')
                                                    file.write('\n')

                                        return
                                    else:
                                        print()
                                        print("Invalid recovery user-id.")
                                        print("Access Denied..")
                                        break
                                else:
                                    print("Sorry, We don't have any recovery of that account")
                                    print()
                                    break
                    break

            if not found:
                print("Invalid Username or Mobile number.")
                print()

    def login(self):
        option = self.take_input()
        if option == "1":
            print()
            print("Now Login As Seller with either username or mobile number.")
            print()
            username = self.process_login()
            if username:
                return "seller", username  # Returning both role and username
            else:
                return None, None  # Return None if login is not successful
        elif option == "2":
            print()
            print("Now Login As buyer with either username or mobile number.")
            print()
            username = self.process_login()
            if username:
                return "buyer", username  # Returning both role and username
            else:
                return None, None  # Return None if login is not successful
        else:
            return None, None  # Return None if option is invalid