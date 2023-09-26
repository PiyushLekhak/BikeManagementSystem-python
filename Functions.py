# 21039645 Piyush Lekhak
import datetime #importing datetime module for using date and time for transactions
def displayOptions(): #function that displays the initial  options
    options= print("\n1. Sell Bikes.\n2. Order Bikes.\n3. Exit.\n")
    return options #the function returns the value in the variable

def displaySellBikes():
    letsSell = print("\nLet's sell bikes.\n\n***************************************************\n\n")
    return letsSell

def getUserInput(): #function that take takes the user's option either to sell, order or exit
    userInput = str(input("\nEnter value of the option: "))
    return userInput

def getUserName():  #function that take takes the user's name
    userName = str(input("\nEnter Customer's Name: "))
    return userName

def getUserAddress(): #function that take takes the user's address
    userAddress = str(input("\nEnter Customer's Address: "))
    return userAddress

def getUserContact(): #function that take takes the user's contact info
    runLoop = True
    while runLoop:
        try: 
            userPhn = int(input("\nEnter Customer's Phone Number: ")) #forcing user to input numbers as phone number
            if (len(str(userPhn)) == 10): #making sure user's entered number is a valid phone number
                runLoop = False
                return userPhn
            else:
                 print("\nPlease provide a 10 digit Phone number")
        except:
            print("\nPlease enter a valid Phone number")

def getCompanyName():
    userName = str(input("\nEnter Shipping Company's Name: "))
    return userName

def getCompanyAddress():
    userAddress = str(input("\nEnter Shipping Company's Address: "))
    return userAddress

def getCompanyContact():
    runLoop = True
    while runLoop:
       try:
            userPhn = int(input("\nEnter Company's Phone Number: "))
            if (len(str(userPhn)) == 10):
                runLoop = False
                return userPhn
            else:
                 print("\nPlease provide a 10 digit Phone number")
       except:
            print("\nPlease enter a valid Phone number")

def displayOrderBikes():
    letsOrder =  print("\nLet's order bikes.\n\n***************************************************\n\n")
    return letsOrder

def invalidInput(): #function that displays an invalid message when user doesn't enter one of the options
    inputInvalid =  print("\nINVALID INPUT. Please enter a number from the options.\n")
    return inputInvalid

def end(): #function to display thank you message
    theEnd =   print("***********************************************************\n         Thank you for using Bike Management System          \n***********************************************************")
    return theEnd

def displayBikes(): #function to display all the available bikes with their data
    print("*******************************************************************************************************************************************************")
    print("Bike ID\t\tBike-Name\t\t\tCompany\t\t\tColor\t\t\t\tStock\t\t\tPrice")
    print("*******************************************************************************************************************************************************")
    file = open("bikes.txt","r") #opening the file that has all the relevant info
    bikeId = 1 #setting initial bike id to 1
    for line in file: #using loop to iterate through each item in the file
        print("",bikeId,"\t\t"+line.replace(",","\t\t\t")) #for each line in the file bikeid(1) is printed then "," is replaced with 3 spaces
        bikeId += 1 #bike id is increased by 1 
    print("***************************************************")
    file.close() #file closed as sometimes changes made may not be shown if file not closed
    

def store2dList(): #function to store all the data in a list
    file = open("bikes.txt")
    list_2d = [] #declaring an empty list to store the data
    for line in file:
        line = line.replace("\n","") #for every line line break is replaced with a ","
        line = line.split(",") #splitting after every ","
        list_2d.append(line) #adding the list as a single item in the list_2d making it a 2d list
    file.close()
    return list_2d

def validateBikeIdSell(): #function to validate the sell id
    runLoop = True
    while runLoop:
        try: #exception handling in case the user inputs value that is not a string
            validBikeId = int(input("\nEnter ID of bike to sell: "))
            runLoop = False
            while validBikeId <= 0 or validBikeId > len(store2dList()): #making sure the user inputted id is more than zero and less than the list's length
                print("\nPlease provide a valid bike Id!!!")
                displayBikes()
                validBikeId = int(input("\nEnter Id of bike to sell: "))
            return validBikeId
        except:
            print("\nPlease enter a valid number") 
            displayBikes()

def validateBikeIdOrder():
    runLoop = True
    while runLoop:
        try:
            validBikeId = int(input("\nEnter ID of bike to Order: "))
            runLoop = False
            while validBikeId <= 0 or validBikeId > len(store2dList()):
                print("\nPlease provide a valid bike Id!!!")
                displayBikes()
                validBikeId = int(input("\nEnter Id of bike to Order: "))
            return validBikeId
        except:
             print("\nPlease enter a valid number")
             displayBikes()

def validSellQuantity(bike_id): #function to validate the sell quantity
    runLoop = True
    while runLoop:
        try:
            quantity = int(input("\nEnter number of bikes you want to Sell: "))
            runLoop = False
            bikes = store2dList()
            while quantity > int(bikes[bike_id-1][3]) or quantity <= 0: #making sure the user inputted qunatity is more than zero and is not more than the stock
                print("\nPlease input within the Stock values!!!")
                quantity = int(input("\nEnter number of bikes you want to Sell: "))
            return quantity
        except:
             print("\nPlease enter a valid number")
             displayBikes()

def validOrderQuantity(): #function to validate the sell quantity
    runLoop = True
    while runLoop:
        try:
            quantity = int(input("\nEnter number of bikes you want to Order: "))
            runLoop = False
            while quantity <=0: #making sure the user inputted qunatity is more than zero
                print("\nPlease order 1 or more bikes")
                quantity = int(input("\nEnter number of bikes you want to Order: "))
            return quantity
        except:
             print("\nPlease enter a valid number")
             displayBikes()

def updateStock(bikes): #function to update stocks by overwriting the txt file
    file = open("bikes.txt","w")
    for bike in bikes:
        file.write(str(bike[0])+","+str(bike[1])+","+str(bike[2])+","+str(bike[3])+","+str(bike[4])+"\n") #replacing data
    file.close()

def sellBikes(bike_id, sellQuantity): #function to sell bikes
    bikes = store2dList()
    bikes[bike_id - 1] [3] = int(bikes[bike_id-1] [3]) - sellQuantity #deducting the inputted user quantity from the stock
    updateStock(bikes) #above function that overwrites is called to show the new stock
    print("\nSold!!!")

def orderBikes(bike_id,orderQuantity): #function to order bikes
    bikes = store2dList()
    bikes[bike_id - 1] [3] = int(bikes[bike_id-1] [3]) + orderQuantity #adding the inputted user quantity to the stock
    updateStock(bikes)
    print("\nOrdered!!!")

    
def getDateAndTime(): #date and time of sell/order is required multiple times, so its stored in a variable 
    dateAndTime = str(datetime.datetime.now().year) +"-"+ str(datetime.datetime.now().month) +"-"+ str(datetime.datetime.now().day) +"-"+ str(datetime.datetime.now().hour) +"_"+ str(datetime.datetime.now().minute)+"_"+str(datetime.datetime.now().second)
    return dateAndTime

def displaySale(userName,userAddress, userContact,soldData): #function to display sale details in the program
    grandTotal = 0
    print("\nCustomer Details: "+ "\n*********************************************************************************************************************************")
    print("\nName: "+"\t\t"+ userName + "\n\nAddress: "+"\t"+ userAddress+ "\n\nPhone NUmber: "+"\t"+ str(userContact))
    print("\n\nSale Details: "+ "\n*********************************************************************************************************************************")
    print("\nCompany"+"\t\t"+"Bike-Name"+"\t\t"+ "Color"+"\t\t\t"+"Quantity"+"\t"+ "Unit Price"+"\t"+"Total-Price"+"\t"+ "Sold-Time\n")
    print("*********************************************************************************************************************************\n")
    for bike in soldData: #using loop to extract all the sold data from list incase multiple sales are made
        grandTotal += bike[5] #grand total increases with every single sale
        print(bike[0]+"\t\t"+bike[1]+"\t\t"+bike[2]+"\t\t"+str(bike[3])+"\t\t"+bike[4] +"\t\t"+str(bike[5])+"\t\t"+getDateAndTime()) #displaying the sale details
    print( "\n\n\t\t\t\t\t\t\t\t\t\t\t\t\tGrand Total = " + "$"+str(grandTotal))
    print("\n*********************************************************************************************************************************\n")

def displayOrder(companyName,companyAddress, companyContact,orderedData):
    grandTotal = 0
    shippingCost = 890
    print("\nShipping Company Details: "+ "\n*********************************************************************************************************************************")
    print("\nName: "+"\t\t"+ companyName + "\n\nAddress: "+"\t"+ companyAddress+ "\n\nPhone NUmber: "+"\t"+ str(companyContact))
    print("\n\nOrder Details: "+ "\n*********************************************************************************************************************************")
    print("\nCompany"+"\t\t"+"Bike-Name"+"\t\t"+ "Color"+"\t\t\t"+"Quantity"+"\t"+ "Unit Price"+"\t"+"Total-Price"+"\t"+ "Ordered-Time\n")
    print("*********************************************************************************************************************************\n")
    for bike in orderedData:
        grandTotal += bike[5]
        print(bike[0]+"\t\t"+bike[1]+"\t\t"+bike[2]+"\t\t"+str(bike[3])+"\t\t"+bike[4] +"\t\t"+str(bike[5])+"\t\t"+getDateAndTime())
    grandTotal += shippingCost
    print( "\n\n\t\t\t\t\t\t\t\t\t\t\t\t\tShipping Cost = " + "$"+str(shippingCost))
    print( "\n\n\t\t\t\t\t\t\t\t\t\t\t\t\tGrand Total = " + "$"+str(grandTotal))
    print( "\n\n*Delivery usually takes 15 days from ordered time")
    print("\n*********************************************************************************************************************************\n")

def generateSaleBill(userName,userAddress, userContact,soldData): #function to generate the sale bill
    grandTotal = 0
    file = open("Sold To"+"_"+userName+"_" + "at" +"_" + getDateAndTime()+".txt","w")
    file.write("Customer Details: "+ "\n*********************************************************************************************************************************")
    file.write("\nName: "+"\t\t"+ userName + "\n\nAddress: "+"\t"+ userAddress+ "\n\nPhone NUmber: "+"\t"+ str(userContact))
    file.write("\n\nSale Details: "+ "\n*********************************************************************************************************************************")
    file.write("\nCompany"+"\t\t"+"Bike-Name"+"\t\t"+ "Color"+"\t\t\t"+"Quantity"+"\t"+ "Unit Price"+"\t"+"Total-Price"+"\t"+ "Sold-Time\n")
    file.write("*********************************************************************************************************************************\n")
    for bike in soldData: #using loop to extract all the sold data from list incase multiple sales are made
        grandTotal += bike[5]
        file.write(bike[0]+"\t\t"+bike[1]+"\t\t"+bike[2]+"\t\t"+str(bike[3])+"\t\t"+bike[4] +"\t\t"+str(bike[5])+"\t\t"+getDateAndTime()+"\n") #writing the details in a new file which acts as the sale bill
    file.write( "\n\n\t\t\t\t\t\t\t\t\t\t\t\t\tGrand Total = " + "$"+str(grandTotal))
    file.write("\n*********************************************************************************************************************************\n")
    file.close()

def generateOrderBill(companyName,companyAddress, companyContact,orderedData):
    grandTotal = 0
    shippingCost = 890
    file = open("Ordered by"+"_"+companyName+"_" + "at" +"_" + getDateAndTime()+".txt","w")
    file.write("Shipping Company Details: "+ "\n*********************************************************************************************************************************")
    file.write("\nName: "+"\t\t"+ companyName + "\n\nAddress: "+"\t"+ companyAddress+ "\n\nPhone NUmber: "+"\t"+ str(companyContact))
    file.write("\n\nOrder Details: "+ "\n*********************************************************************************************************************************")
    file.write("\nCompany"+"\t\t"+"Bike-Name"+"\t\t"+ "Color"+"\t\t\t"+"Quantity"+"\t"+ "Unit Price"+"\t"+"Total-Price"+"\t"+ "Ordered-Time\n")
    file.write("*********************************************************************************************************************************\n")
    for bike in orderedData:
        grandTotal += bike[5]
        file.write(bike[0]+"\t\t"+bike[1]+"\t\t"+bike[2]+"\t\t"+str(bike[3])+"\t\t"+bike[4] +"\t\t"+str(bike[5])+"\t\t"+getDateAndTime()+"\n")
    grandTotal += shippingCost
    file.write( "\n\n\t\t\t\t\t\t\t\t\t\t\t\t\tShipping Cost = " + "$"+str(shippingCost))
    file.write( "\n\n\t\t\t\t\t\t\t\t\t\t\t\t\tGrand Total = " + "$"+str(grandTotal))
    file.write( "\n\n*Delivery usually takes 15 days from ordered time")
    file.write("\n*********************************************************************************************************************************\n")
    file.close()