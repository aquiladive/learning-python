#bookshop display and billing

#initialising constants like genres and books
genre_list = ["Romance","Fantasy","Mystery","Manga","Children's Lit","Short Stories"]

book_list = [["Hold My Hand","Red, White and Royal Blue","Twilight","The Fault in Our Stars"],
["Dragon Weather","The Golden Compass","Lord of Mysteries","The Amulet of Samarkand"],
["The Murder of Roger Ackroyd","A Study in Scarlet","The Purrfect Murder","The Secret Adversary"],
["Tokyo Ghoul Vol 1","Spy x Family Vol 1","Assassination Classroom Vol 1","Bungou Stray Dogs Vol 1"],
["Charlotte's Web","The Mona Mousa Code","Matilda","The Wonderful Wizard of Oz"],
["Aesop's Fables","Grandma's Bag of Stories","The Greatest Short Stories of Leo Tolstoy","Miss Marple: The Complete Short Stories"]]

book_details = [[["Durjoy Datta","English",310],["Casey McQuiston","English",415],["Stephenie Meyer","English",375],["John Green","English",399]],
[["Lawrence Watt-Evans","English",225],["Philip Pullman","English",350],["Cuttlefish","Chinese",1750],["Johnathan Stroud","English",389]],
[["Agatha Christie","English",199],["Arthur Conan Doyle","English",199],["Rita Mae Brown","English",225],["Agatha Christie","English",225]],
[["Sui Ishida","English",400],["Tatsuya Endo","English",475],["Yusei Matsui","Japanese",400],["Kafka Asagiri","Japanese",475]],
[["EB White","English",150],["Geronimo Stilton","English",225],["Roald Dahl","English",175],["L Frank Baum","English",200]],
[["Aesop","English",200],["Sudha Murthy","English",175],["Leo Tolstoy","English",200],["Agatha Christie","English",225]]]

cart = []

#function for displaying genres
def display():
    for i in range(len(genre_list)):
        print("{}) {}".format(i+1,genre_list[i]))
    print("input corresponding number to see book list, or 0 for cart")

#function for choosing a book and placing it in cart
def book_pick(index):
    print("Sl no\t{:<25}\t{:<20}\t{:<9}\tPrice".format("Book Name","Author","Language"))
    for i in range(4):
        print("{:<5}\t{:<25}\t{:<20}\t{:<9}\tRs {}".format(i+1,book_list[index][i],book_details[index][i][0],book_details[index][i][1],book_details[index][i][2]))
    book_choice=int(input("input sl no: to put book in cart\n"))-1 #subtracting 1 because user input is from 1 to 7, array index is 0 to 6
    
    if book_choice>=0 and book_choice<4:
        cart_line=[book_list[index][book_choice],book_details[index][book_choice][0],book_details[index][book_choice][1],book_details[index][book_choice][2]]
        cart.append(cart_line)
        choice=int(input("input 0 to go to billing, or anything else to continue browsing\n"))
        if choice == 0:
            open_cart()
	       
#function for the cart and billing option
def open_cart():
    while(True):
        print("Your cart is as follows:\n")
        print("Sl no\t{:<25}\t{:<20}\t{:<9}\tPrice".format("Book Name","Author","Language"))
        total=0
        for i in range(len(cart)):
            print("{:<5}\t{:<25}\t{:<20}\t{:<9}\tRs {}".format(i+1,cart[i][0],cart[i][1],cart[i][2],cart[i][3]))
            total+=cart[i][3]
        print("Total = Rs {}".format(total))
        cart_choice=int(input("\npress 0 to pay, 1 to add an item, 2 to remove\n"))
        if cart_choice==0:
            print("Enter payment details.")
            print("Thank you for shopping with Tale.Traders!")
            quit()
        elif cart_choice==1:
            break
            display()
        elif cart_choice==2:
            removal=int(input("Which item do you wish to remove?\n(input its sl no)\n"))
            if removal <= len(cart):
                cart.remove(cart[removal-1])
                print("Item has been removed.\n")
            else:
                print("Invalid input.")
        else:
            print("Invalid input.\n")


#main
print("Welcome to Tale.Traders! An online bookstore here to satisfy your word cravings.")
while(True):
    print("Our currently available genres:")
    display()
    index=int(input())-1
    
    if index >= 0 and index < 6:
        book_pick(index)
        
    elif index == -1:
        open_cart()

    else:
        print("Invalid input.\n")
