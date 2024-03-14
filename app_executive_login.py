from buyer_user_class import Buyer








class Admin_Login(Buyer):
    def __init__(self, file, accounts, seller_folder, buyer_folder, file_buyer, file_seller):
        super().__init__(file, accounts, seller_folder, buyer_folder, file_buyer, file_seller)
        self.seller_manager_file="admin_credentials/seller_manager_acc.txt"
        self.buyer_manager_file="admin_credentials/buyer_manager_acc.txt"
        
    
    def assign_seller_manager(self):
                        print("Now You Can Assign The Postion Of Seller Operations Manager To Someone")
                        print("Please Fill Out Following Details")
                        name=self.first_name()
                        if name:
                            while True:
                                username=input("Set The Username For manager So He can access His Portal with that useraname:")
                                if len(username)>=1:
                                    break
                                else:
                                    print("Please Set Username for manager.")
                            password=self.password_input()
                            print("Congratulations Dear App Executive The Post Of Seller Operaions manager is assigned succesfully")
                            print(f"1.Name of person:{name}\n2.User-Name:{username}\n3.Password:{password}")
                            print()
                            with open (self.seller_manager_file,"w") as file:
                                file.write(f"{name}$$${username}$$${password}")


    def assign_buyer_manager(self):
                        print("Now You Can Assign The Postion Of Buyer Operations Manager To Someone")
                        print("Please Fill Out Following Details")
                        print()
                        name=self.first_name()
                        if name:
                            while True:
                                username=input("Set The Username For manager So He can access His Portal with that useraname:")
                                if len(username)>=1:
                                    break
                                else:
                                    print("Please Set Username for manager.")
                            password=self.password_input()
                            print("Congratulations Dear App Executive The Post Of Buyer Operaions manager is assigned succesfully")
                            print(f"1.Name of person:{name}\n2.User-Name:{username}\n3.Password:{password}")
                            print()
                            with open (self.buyer_manager_file,"w") as file:
                                file.write(f"{name}$$${username}$$${password}")


    def reassign_seller_manager(self):
        with open(self.seller_manager_file) as file:
            lines=file.read()
            if not lines:
                print("Sorry Dear App Executive This Post Is Not assigned Yet! So You can't Reassign It.")
                print()
                return
            else:
                data=lines.strip().split("$$$")
                print(f"Dear Sir! This Post (Seller Operations Manager) is currently assign to:\nName Of Manager:{data[0]}\nUser-name:{data[1]}\nPassword:{data[2]}")
                print()
                while True:
                    confirmation=input("Are You Sure You Want To Reassign This Post (y/n):").lower()
                    if confirmation not in ["y","n"]:
                        print("Please Sir Enter Correct Word.")
                        print()
                    elif confirmation=="n":
                        print(f"Alright Mr{data[0]} will still able to serve his services. ")
                        print()
                        return
                    else:
                        print("Alright Now Reassign This Post To some one else")
                        print()
                        self.assign_seller_manager()
                        break

    def reassign_buyer_manager(self):
        with open(self.buyer_manager_file) as file:
            lines=file.read()
            if not lines:
                print("Sorry Dear App Executive This Post Is Not assigned Yet! So You can't Reassign It.")
                print()
                return
            else:
                data=lines.strip().split("$$$")
                print(f"Dear Sir! This Post (Buyer Operations Manager) is currently assign to:\nName Of Manager:{data[0]}\nUser-name:{data[1]}\nPassword:{data[2]}")
                print()
                while True:
                    confirmation=input("Are You Sure You Want To Reassign This Post (y/n):").lower()
                    if confirmation not in ["y","n"]:
                        print("Please Sir Enter Correct Word.")
                        print()
                    elif confirmation=="n":
                        print()
                        print(f"Alright Mr-{data[0]} will still able to serve his services. ")
                        print()
                        return
                    else:
                        print("Alright Now Reassign This Post To some one else")
                        print()
                        self.assign_buyer_manager()
                        break



    def admin_login(self):
        admin_username = "admin"    # Admin username
        admin_password = "admin123"   # admin password

        # Ask the user for the username and password
        while True:
            username = input("Enter App Executive Username (enter 0 to back): ")
            if username == "0":
                return
            # Check if the username is correct
            if username == admin_username:
                break
            else:
                print("Incorrect Username of App Executive.")
                print()
        # when username is correct then ask for password
        while True:
                password = input("Enter App Executive Password (enter 0 to back): ")
                if password == "0":
                    return
                
                # Check if the password is correct
                if password == admin_password:
                    print("App Executive Login Successful!!")
                    print()
                    break
                else:
                    print("Incorrect Password of App Executive.")
                    print()
        while True:
            print()
            print("\t\t\tWelcome Dear App Executive.")
            print("\t\t1.Declare The post of Seller Operations Manager To person")
            print("\t\t2.Declare The post of Buyer Operations Manager To person")
            print("\t\t3.Reassign The post of Seller Operations Manager To person")
            print("\t\t4.Reassign The post of Buyer Operations Manager To person")
            print("\t\t5.To Exit:exit From App Executive Area.")
            print()
            executive_choice=input("Dear Sir Please Enter preferred Option:").strip()

            if executive_choice=="1":
                with open(self.seller_manager_file) as file:
                    lines=file.readlines()
                    if lines:
                        print("Dear Sir! You Already Assigned This Designation To someone Else.")
                        print()             
                    else:
                        self.assign_seller_manager()
                       
            
            elif executive_choice=="2":
                with open(self.buyer_manager_file) as file:
                    lines=file.readlines()
                    if lines:
                        print("Dear Sir! You Already Assigned This Designation To someone Else.")
                        print()
                        
                    else:
                        self.assign_buyer_manager()
                        
            elif executive_choice=="3":
                self.reassign_seller_manager()

            elif executive_choice=="4":
                self.reassign_buyer_manager()


            elif executive_choice=="5":
                print("GoodBye! Dear App Executive Hope You Got satisfied by our services.")
                print()
                return
            
            else:
                print()
                print("Invalid choice sir.please Enter Correct Choice.")
                print()

