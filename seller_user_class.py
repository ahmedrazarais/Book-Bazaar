import random # importing random
import os        # import os
from register_class import Register      # importing register class from register file





# creating class for seller inherited with register class
class Seller(Register):
    def __init__(self, file, accounts, seller_folder, buyer_folder, file_seller):
        super().__init__(file, accounts, seller_folder, buyer_folder)
        self.file_seller = file_seller
        self.id_file="purchseDetails/id_file.txt"    # all users purchase details
        self.main_file="booksDatabase/books_file.txt"      # books database where all sellers contribution stored

    # GENERATING RANDOM ID.
    def random_id(self):
        # checking that random id must not in file
        with open(self.id_file, "r") as file:
            used_ids = file.read()
            used_ids = used_ids.split("\n")
            while True:
                unique_id = random.randint(1000, 9999)
                if str(unique_id) not in used_ids:
                    used_ids.append(str(unique_id))
                    with open(self.id_file, "a") as file:
                        # write in file 
                        file.write(f"{unique_id}\n")
                    return unique_id
    
    def sell_books(self):
         # Prompt user for vehicle details
        while True:
            print()
            #taking book name input
            book_name = input("Enter Your Book Name (enter 0 to go back): ")
            print()
            if book_name == "0":
                return   # if he want to go back
            if book_name != "":
                break
            else:
                print("Please Provide The Name Of The Book")
                print()

        while True:   # taking author name input
            author_name = input(f"Enter author name of book {book_name}  (enter 0 to go back): ")
            print()
            if author_name == "0":
                return 
            # all alphabets are allowed
            if author_name != "" and author_name.isalpha():
                break
            # if not then print error message
            else:
                print()
                print("Oops! Author Name is Mandatory To Be Set.Only Alphabets are allowed.")
                print()

        while True: # taking edition input
            edition = input(f"Enter edition of the book {book_name} (enter 0 to go back): ")
            print()
            if edition == "0":
                return 
            # all digits are allowed
            if edition != "" and edition.isdigit():
                break
            else:  # if not then print error message
                print()
                print("Edition Of Book  is Mandatory. Only Digits are allowed.")
                print()

        while True:
            try:   # using try except block to handle exception
                book_price = int(input("Enter Price Of The Book (enter 0 to go back): "))
                print()
                if book_price == 0:
                    return # if he want to go back
                # if price is greater than 0 then break the loop
                if book_price != "" and book_price > 0:
                    break
                else:   # invalid price
                    print()
                    print("Price is Mandatory To Set Your Book For Sell.Must Be Greater Than 0.")
                    print()
            except ValueError:
                print("Price Should be in Digits.")
                print()

        while True: # status of book
            status = input("Share your  book status active or nonactive: ").strip().lower()
            print()
            # if valid status then break the loop
            if status in ["active", "nonactive"]:
                break
            else:
                print("Invalid Choice.")
                print("Please Select From (Active/Nonactive)")
                print()

        sold_status="Not-Sold"
        id=self.random_id()
        sep="+++"
        # after it writting in seller personal file
        with open(self.file_seller,"a+") as file:
            file.write(f"{id}{sep}{book_name}{sep}{author_name}{sep}{edition}{sep}{book_price}{sep}{status}{sep}{sold_status}\n")
        print()
        print(f"Congratulations Seller! your Book {book_name} written by {author_name} is set to be sold.")
        print(f"You Set Price Of the book is Rs {book_price}")
        print("We Will Notify You When the book is sold,Thank You!")
        print()
        # Writting in overall file that is general
        with open(self.main_file,"a+") as main:
            main.write(f"{id}{sep}{book_name}{sep}{author_name}{sep}{edition}{sep}{book_price}{sep}{status}\n")
        return


    # mehtod to view books that seller uploaded
    def view_books(self):
        with open(self.file_seller) as file:
            lines=file.readlines()
            if not lines: # if seller does not upload any book
                print("You Come so early There Are no books to show ,Add Some Books Then Came Back Later")
                print()
            else:
                print("\tHere Are Your Books That You Set For Sell.")
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
 
    # update choices for seller
    def update_choices(self):
        print()
        print("\t\t\tWelcome In Update Section")
        print("\t\t1.Change The Book Name.")
        print("\t\t2.Change The Author Name.")
        print("\t\t3.Change The Book Price.")
        print("\t\t4.Change The Book Status.")
        print("\t\t5.To Exit:Come Out Of Update Section.")
    
    # mehtod to update books
    def update_books(self):
     found = False
     with open(self.file_seller) as file:
        lines = file.readlines()
        if not lines:    # if there is no book to update
            print("No Books Information Received Yet, So What You Want To Update.")
        else:
            while True:
                self.view_books()
                print()
                print()
                # taking book id input
                book_id = input("Enter The Book Id That You want To Update (enter 0 to back):").strip()
                if book_id == "0":
                    return
                for line in lines:
                    parts = line.strip().split("+++")
                    if len(parts) >= 6 and parts[0] == book_id:
                        found = True # if book is found then break the loop
                        print()
                        print("Book found! You can now update its information.")
                        print()
                        break  # Exiting the loop once the book is found

                if found:   # if book is found then update the book
                    while True:
                        self.update_choices()
                        print()
                        # asking for choice
                        choice_update = input("Enter Your Choice In Update Section:").strip()

                        # BOOK NAME CHANGE PROCESS
                        if choice_update == "1":
                            while True:
                                new_book_name = input("Enter New Book Name (enter 0 to back):")

                                if new_book_name == "0":
                                    break
                                if new_book_name != "":
                                    updated_index = None
                                    # updating the book name
                                    for i, l in enumerate(lines):
                                        parts = l.strip().split("+++")
                                        if len(parts) >= 6 and parts[0] == book_id:
                                            parts[1] = new_book_name
                                            updated_line = "+++".join(parts) + "\n"
                                            lines[i] = updated_line
                                            updated_index = i
                                            break
                                    if updated_index is not None:
                                        # UPDATE IN SELLER FILE
                                        with open(self.file_seller, "w") as file:
                                            file.writelines(lines)
                                        
                                        # UPDATE IN MAIN DATABASE FILE
                                        with open(self.main_file, "r") as file:
                                            main_lines = file.readlines()
                                        for i, main_line in enumerate(main_lines):
                                            main_parts = main_line.strip().split("+++")
                                            if len(main_parts) >= 6 and main_parts[0] == book_id:
                                                main_parts[1] = new_book_name
                                                main_lines[i] = "+++".join(main_parts) + "\n"
                                        with open(self.main_file, "w") as file:
                                            file.writelines(main_lines)
                                        print("Book Name Successfully Updated.")
                                        print()
                                        self.view_books()
                                        break
                                else:
                                    print("Please Provide The Name Of The Book")
                                    print()

                        # AUTHOR NAME UPDATE PROCESS
                        elif choice_update == "2":
                            while True:
                                new_author_name = input("Enter new author name of book (enter 0 to go back): ")
                                print()
                                if new_author_name == "0":
                                    break 
                                if new_author_name != "" and new_author_name.isalpha():
                                    updated_index = None
                                    for i, l in enumerate(lines):
                                        parts = l.strip().split("+++")
                                        if len(parts) >= 6 and parts[0] == book_id:
                                            parts[2] = new_author_name
                                            updated_line = "+++".join(parts) + "\n"
                                            lines[i] = updated_line
                                            updated_index = i
                                            break
                                    if updated_index is not None:
                                        # UPDATE IN SELLER FILE
                                        with open(self.file_seller, "w") as file:
                                            file.writelines(lines)
                                        
                                        # UPDATE IN MAIN DATABASE FILE
                                        with open(self.main_file, "r") as file:
                                            main_lines = file.readlines()
                                        for i, main_line in enumerate(main_lines):
                                            main_parts = main_line.strip().split("+++")
                                            if len(main_parts) >= 6 and main_parts[0] == book_id:
                                                main_parts[2] = new_author_name
                                                main_lines[i] = "+++".join(main_parts) + "\n"
                                        with open(self.main_file, "w") as file:
                                            file.writelines(main_lines)
                                        print("Author Name Successfully Updated.")
                                        self.view_books()
                                        break
                                else:
                                    print("Oops! Author Name is Mandatory To Be Set. Only Alphabets are allowed.")
                                    print()

                        # PRICE UPDATE PROCESS
                        elif choice_update == "3":
                            while True:
                                try:
                                    new_book_price = int(input("Enter Price Of The Book (enter 0 to go back): "))
                                    print()
                                    if new_book_price == 0:
                                        break
                                    if new_book_price > 0:
                                        updated_index = None
                                        # updating the book price
                                        for i, l in enumerate(lines):
                                            parts = l.strip().split("+++")
                                            if len(parts) >= 6 and parts[0] == book_id:
                                                parts[4] = str(new_book_price)
                                                updated_line = "+++".join(parts) + "\n"
                                                lines[i] = updated_line
                                                updated_index = i
                                                break
                                        if updated_index is not None:
                                            # UPDATE IN SELLER FILE
                                            with open(self.file_seller, "w") as file:
                                                file.writelines(lines)
                                            
                                            # UPDATE IN MAIN DATABASE FILE
                                            with open(self.main_file, "r") as file:
                                                main_lines = file.readlines()
                                            for i, main_line in enumerate(main_lines):
                                                main_parts = main_line.strip().split("+++")
                                                if len(main_parts) >= 6 and main_parts[0] == book_id:
                                                    main_parts[4] = str(new_book_price)
                                                    main_lines[i] = "+++".join(main_parts) + "\n"
                                            with open(self.main_file, "w") as file:
                                                file.writelines(main_lines)
                                            print("Price Of The Book Updated Successfully.")
                                            self.view_books()
                                            break
                                    else:
                                        print("Price is Mandatory To Set Your Book For Sell. Must Be Greater Than 0.")
                                        print()
                                except ValueError:
                                    print("Price Should be in Digits.")
                                    print()

                        # STATUS UPDATE PROCESS
                        elif choice_update == "4":
                            while True:
                                status = input("Share your book status active or nonactive: ").strip().lower()
                                print()
                                if status in ["active", "nonactive"]:
                                    updated_index = None
                                    for i, l in enumerate(lines):
                                        parts = l.strip().split("+++")
                                        if len(parts) >= 6 and parts[0] == book_id:
                                            parts[5] = status
                                            updated_line = "+++".join(parts) + "\n"
                                            lines[i] = updated_line
                                            updated_index = i
                                            break
                                    if updated_index is not None:
                                        # UPDATE IN SELLER FILE
                                        with open(self.file_seller, "w") as file:
                                            file.writelines(lines)
                                        
                                        # UPDATE IN MAIN DATABASE FILE
                                        with open(self.main_file, "r") as file:
                                            main_lines = file.readlines()
                                        for i, main_line in enumerate(main_lines):
                                            main_parts = main_line.strip().split("+++")
                                            if len(main_parts) >= 6 and main_parts[0] == book_id:
                                                main_parts[5] = status
                                                main_lines[i] = "+++".join(main_parts) + "\n"
                                        with open(self.main_file, "w") as file:
                                            file.writelines(main_lines)
                                        print("Book Status Successfully Updated.")
                                        self.view_books()
                                        break
                                else:    # if invalid status
                                    print("Invalid Choice.")
                                    print("Please Select From (Active/Nonactive)")
                                    print()
                        # if he want to exit from update section
                        elif choice_update == "5":
                            print()
                            print("Thanks For Visiting Update Area. Hope You Are satisfied with our services")
                            print()
                            return
                #  if book is not found
                if not found:
                    print()
                    print()
                    print("No book found with the given ID. Please enter a valid Book ID.")
                    print()
                    print()
                    print()




    
   # This method is used to perform seller operations
    def seller_operations(self):
        # if file does not exist in seller folder
        if not os.path.exists(self.file_seller):
            print()
            print("Unable To Enter In Seller Section,Kindly Provide Correct Credentials.")
            print()
            return  # return if file not found
        print("Credentials Are Correct! Now You Can Access Sellers Operations.")
        print()
        # Perform seller operations if file exists
        while True:
            print("\t\t\tWelcome To Book-Bazaar (Seller Choices)")
            print("\t\t1.Add Your Books To Your Catalog.")
            print("\t\t2.View All Books That you Upload.")
            print("\t\t3.Update Books Information.")
            print("\t\t4.To Exit:exit From Seller Operations")
            print()
            
            seller_choice=input("Enter Your Choice In seller Section:").strip()
            # calling the respective methods based on the user's choice
            if seller_choice=="1":
                print()
                print("Welcome to the Book Addition Area!")
                self.sell_books()
            
            elif seller_choice=="2":
                print()
                print("Welcome! Here You Can see All Books That You Added In Our Library.")         
                self.view_books()
                print()
            
            elif seller_choice=="3":
                print()
                print("Welcome In Update Area. Here You can update Your Book Information")
                self.update_books()
            
            elif seller_choice=="4":
                print()
                print("Thank you for visiting the Seller's Area!")
                break      # if he want to exit from seller section
            
            else:
                print("Invalid Option.Please Select On The Basis of given Choices.")
                print()
                    

        
              

    
    # Method to set the file path using the username
    def set_seller_file_path(self, username):
        # Construct file path using username
        self.seller_file_path = os.path.join(self.seller_folder, f"{username}.txt")
