Item_No = []
Item_Description = []
Reserve_Price = []
No_of_Bids = []
Place = 0
Continue = 1
Item_Bid = 0


def datainput(Place, Item_No, Item_Description, Reserve_Price, No_of_Bids):
  while Continue == 1:
    item_no = int(input("Please input the Item ID: "))
    item_description = str(input("Please input a brief description of the item: "))
    reserve_price = str(input("Pleae input a reserve price: "))
    no_of_bids = 0
    Item_No.append(item_no)
    Item_Description.append(item_description)
    Reserve_Price.append(reserve_price)
    No_of_Bids.append(no_of_bids)
    Place = Place + 1
    End_Input(Continue,Place)

def End_Input (Continue, Place):
  Continue = int(input("Input 1 to continue adding items or 0 to stop inputing items and start the auction: "))
  if Continue == 0:
    if Place>0:
      Auction_Bid()
    else:
     print("You need at least 10 items to start the auction")
     print("You can now input more items")
     Continue = 1
  elif Continue ==1:
    print("")
  else:
    print("Sorry what you inputted is not valid.")
    End_Input(Continue,Place)

def Auction_Bid():
  for x in range (len(Item_No)):
     print("Item ID:\n", Item_No[x])
    
     print("Item Description:\n" + Item_Description[x])
    
     print("Reserve Price:\n" + Reserve_Price[x])
  
  if input("Please input 'Yes' if you would like to bid on an item ")=="Yes" or "Yes":
    Item_Bid = int(input("Please Input the Item ID of the item you would like to look at "))
    Buyer_ID = int(input("Please Input your Buyer ID "))
    for x in range (len(Item_No)):
      if Item_Bid in Item_No:
        print(Item_No[x])
        print(Item_Description[x])
   
    
    

  
 
              
datainput(Place, Item_No, Item_Description, Reserve_Price, No_of_Bids)



