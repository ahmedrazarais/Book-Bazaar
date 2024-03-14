import time
import os
from seller_user_class import Seller





class Buyer(Seller):
    def __init__(self, file, accounts, seller_folder, buyer_folder, file_buyer, file_seller):
        super().__init__(file, accounts, seller_folder, buyer_folder, file_seller)
        self.file_buyer = file_buyer  # Include any other necessary initialization here
        self.booking_file="purchseDetails/purchase.txt"


    def view_available_books(self):
        try:
            with open(self.main_file, "r") as file:
                lines = file.readlines()
                active_books_exist = False
                for line in lines:
                    parts = line.strip().split("+++")
                    if len(parts) >= 6:
                        id, book_name, author, edition, book_price, status = parts[:6]
                        if status == "active":
                            active_books_exist = True
                            break  # If at least one active book is found, break the loop

                if not lines or not active_books_exist:
                    print()
                    print("Apologies, but it seems we're currently out of stock on all books. Please check back later for updated availability. Thank you for your understanding!")
                    print()
                else:
                    print("\tHere Are The Available Books For Sell At That Moment.")
                    print()
                    print("{:<5} {:<15} {:<15} {:<15} {:<15} {:<10}".format("ID", "Book-Name", "Authors", "Editions", "Book-Price", "Status"))
                    print("=" * 100)
                    for line in lines:
                        parts = line.strip().split("+++")
                        if len(parts) >= 6:
                            id, book_name, author, edition, book_price, status = parts[:6]
                            if status == "active":
                                print("{:<5} {:<15} {:<15} {:<15} {:<15} {:<10}".format(id, book_name, author, edition, book_price, status))
                        else:
                            print(f"Invalid data format: {line.strip()}")
        except FileNotFoundError:
            print("Books file not found.")

   




    def add_books_to_cart(self):
        # Check if there is data in the autofile and if any auto has an active status
        with open(self.main_file, "r") as file:
            lines = file.readlines()
            active_book_found = any(line.strip().split("+++")[5] == "active" for line in lines)

        if not lines or not active_book_found:
            print("Apologies, but it seems we're currently out of stock on all books. Please check back later for updated availability. Thank you for your understanding!")
            return

        # If there are active autos, proceed with booking
        time_now = time.ctime()
        while True:
            self.view_available_books()
            print()
            book_id = input("Enter the ID of the Book to Purchase That Book (enter 0 to go back): ")
            if book_id == '0':  # Corrected to compare with string instead of integer
                return

            found = False
            with open(self.main_file, "r") as file:
                lines = file.readlines()

            for line in lines:
                parts = line.strip().split("+++")
                if len(parts) >= 6:
                    id, book_name, author, edition, book_price, status = parts[:6]
                    if id == book_id and status == "active":
                        found = True
                        break  # Once found, no need to continue the loop

            if found:
                print()
                print("\t\tBook Details,You Selected That Book To Purchase")
                print(f"1.Book Name:{book_name}\n2.Author:{author}\n3.Edition:{edition}\n4.Book Price:{book_price}")
                print()
                while True:
                    ask_confirm=input("Are You Confirm To buy The Book (Y/N):").lower()
                    if ask_confirm not in ["y","n"]:
                        print("Please Select Correct Keyword.")
                        print()
                    elif ask_confirm=="y":
                    
                        time_now = time.ctime()
                        with open(self.buyer_file_path, "a+") as file:
                            file.write(f"Recorded Time: {time_now}\n")
                            file.write(f"Book Id: {book_id}\nBook Name: {book_name}\nBook Author: {author}\nEdition: {edition}\nPrice: {book_price}\n")
                            file.write("\n\n")
                        with open(self.booking_file,"a+") as booking_file:
                            booking_file.write(f"Recorded Time: {time_now}\n")
                            booking_file.write(f"Book Id: {book_id}\nBook Name: {book_name}\nBook Author: {author}\nEdition: {edition}\nPrice: {book_price}\n")
                            booking_file.write("\n\n")

                        for i, line in enumerate(lines):  # Iterate with index to modify lines
                            parts = line.strip().split("+++")
                            if len(parts) >= 6:
                                id, book_name, author, edition, book_price, status = parts[:6]
                                if id == book_id:
                                    parts[5] = "nonactive"
                                    lines[i] = "+++".join(parts) + "\n"

                        with open(self.main_file, "w") as file:  # Write back to the file
                            file.writelines(lines)

                        print("Book Has Been Purchased Successfully.")

                        # Update status in SEller files
                        files = os.listdir(self.seller_folder)
                        for file_name in files:
                            if file_name.endswith('.txt'):
                                file_path = os.path.join(self.seller_folder, file_name)
                                # Open the file for reading and writing
                                with open(file_path, 'r+') as file:
                                    lines = file.readlines()
                                    modified = False
                                    # Iterate through each line in the file
                                    for index, line in enumerate(lines):
                                        # Check if the book ID is present in the line
                                        if str(book_id) in line:
                                            # If found, replace the status with the new status
                                            parts = line.strip().split("+++")
                                            if len(parts) >= 7 and parts[6].strip() == "Not-Sold":
                                                parts[6] = "Sold-Out"
                                                lines[index] = "+++".join(parts) + "\n"
                                                modified = True
                                    # If the file was modified, write the changes back to the file
                                    if modified:
                                        file.seek(0)
                                        file.writelines(lines)
                                        file.truncate()

                        return
                    elif ask_confirm=="n":
                        print("Alright Return To Main page..")
                        return

            else:
                print()
                print("Invalid Book Id. Please Enter Correct Book Id.")
                print()
                print()

     

    
    
            
# function to display customer history
    def display_buyer_history(self):
        with open(self.buyer_file_path) as file:
            lines= file.read()
            if not lines:   # if no history found
                print()
                print("You come so early!! No history found.")
                print("Purchase Some Books First.Then Comeback To Check History.")
            else:
                print("\t\tHere Is Your Booking History.")
                print()
                print(lines)
                print()


    def buyer_operations(self):
         if not os.path.exists(self.buyer_file_path):
            print()
            print("Unable To Enter In Buyer Section,Kindly Provide Correct Credentials.")
            print()
            return
         print("Credentials Are Correct! Now You Can Access Buyers Operations.")
         print()
         while True:
            print()
            print("\t\t\tWelcome To Book-Bazaar System (Buyer Choices)")
            print("\t\t1.View All The Books That Are Avaliable for Sell.")
            print("\t\t2.Purchase The Books From Book-Bazaar.")
            print("\t\t3.See Your Previous Purchase History.")
            print("\t\t4.To Exit:exit From Buyer Operations")
            print()
            
            buyer_choice=input("Enter Your Choice In Buyer Section:").strip()
            
            if buyer_choice=="1":
                print()
                print("Explore our collection below:")
                self.view_available_books()
            
            
            elif buyer_choice=="2":
                print()
                print("Welcome! Here You Can Purchase All Books That Are In Our Library.")         
                self.add_books_to_cart()
                
                print()
            
            elif buyer_choice=="3":
                print()
                print("Welcome to your purchase history area! Here you can view all your past purchases.")
                self.display_buyer_history()

              
            
            elif buyer_choice=="4":
                print()
                print("Thank you for visiting the Buyer's Area!")
                break
            
            else:
                print()
                print("Invalid Option.Please Select On The Basis of given Choices.")
                print()
                    
        









    def set_buyer_file_path(self, username):
        # Construct file path using username
        self.buyer_file_path = os.path.join(self.buyer_folder, f"{username}.txt")