# 21039645 Piyush Lekhak
from Functions import * #Importing all the functions from file "Functions"
runLoop = True #Variable value set to true for main loop

print("************************************************************") #welcome message
print("             Welcome to Bike Management System             ")
print("************************************************************")
print()
print()

while runLoop == True: #condition set to run while loop

    displayOptions() #calling function to show the options
    soldData = [] #initializing empty list which will be later used to store sale related data
    orderedData = [] #initializing empty list which will be later used to store order related data
    userInput = getUserInput() #calling function to get user's input while simultaneously storing the input in a variable

    if userInput == "1":
        userName = getUserName()
        userAddress = getUserAddress()
        userContact = getUserContact()
        displaySellBikes() 
        displayBikes() #calling function that lists all the data from the txt file in a tabular structure
        bike_id = validateBikeIdSell() #calling function that validates id of the bike and storing the value in a variable
        sellQuantity = validSellQuantity(bike_id) #calling function that validates quantity with bike_id as parameter of the bike and storing the value in a variable
        sellBikes(bike_id, sellQuantity) #calling the sell function with bike_id and sellQuantity as parameters
        bikes = store2dList() #calling function that reads the txt file and stores it in list
        soldBikes = (bikes[bike_id-1][0]) #accessing bike name via index and storing it in a variable
        soldBikesCompany = (bikes[bike_id-1][1]) #accessing bike comapany via index and storing it in a variable
        soldBikesColor = (bikes[bike_id-1][2]) #accessing bike color via index and storing it in a variable
        soldBikesPrice = (bikes[bike_id-1][4]) #accessing bike price via index and storing it in a variable
        totalAmountSale = 0 #declaring variable totalAmount sale for calculating total sale amount
        price = int(bikes[bike_id -1][4]) * sellQuantity #getting price by multiplying unit price with sell quantity
        totalAmountSale += price #adding prices of all bikes to total sale amount
        soldData.append([soldBikesCompany,soldBikes,soldBikesColor,sellQuantity,soldBikesPrice,totalAmountSale]) #adding all the required sale data to above declared list

        sellLoop = True #another variable for sell again loop
        while sellLoop == True:
            print("\nDo you want to sell more Bikes?") #asking user if they want to make another sale
            anotherSale = str(input("\nIf yes, please enter 'Y' or else provide any input: ")).upper() #.upper function converts any input that is not capitalized to capitalized form
            if anotherSale == "Y": #if user inputs "Y" the same process from above is repeated
                displaySellBikes()
                displayBikes()
                bike_id = validateBikeIdSell()
                sellQuantity = validSellQuantity(bike_id)
                sellBikes(bike_id, sellQuantity)
                bikes = store2dList()
                soldBikes = (bikes[bike_id-1][0])
                soldBikesCompany = (bikes[bike_id-1][1])
                soldBikesColor = (bikes[bike_id-1][2])
                soldBikesPrice = (bikes[bike_id-1][4])
                totalAmountSale = 0
                price = int(bikes[bike_id -1][4]) * sellQuantity
                totalAmountSale += price
                soldData.append([soldBikesCompany,soldBikes,soldBikesColor,sellQuantity,soldBikesPrice,totalAmountSale])
               

            else: #if user inputs anything else loop is ended and sale details is displayed and bill is generated
                sellLoop = False
                print("\nThank You. Bike/s sold succcessfully!!!")
                displaySale(userName,userAddress, userContact,soldData)
                generateSaleBill(userName,userAddress, userContact,soldData)
        
    elif userInput == "2": #similar to sale process
        companyName = getCompanyName()
        companyAddress = getCompanyAddress()
        companyContact = getCompanyContact()
        displayOrderBikes()
        displayBikes()
        bike_id = validateBikeIdOrder()
        orderQuantity = validOrderQuantity()
        orderBikes(bike_id,orderQuantity)
        bikes = store2dList()
        orderedBikes = (bikes[bike_id-1][0])
        orderedBikesCompany = (bikes[bike_id-1][1])
        orderedBikesColor = (bikes[bike_id-1][2])
        orderedBikesPrice = (bikes[bike_id-1][4])
        totalAmountOrder = 0
        price = int(bikes[bike_id -1][4]) * orderQuantity
        totalAmountOrder += price
        orderedData.append([orderedBikesCompany,orderedBikes,orderedBikesColor,orderQuantity,orderedBikesPrice,totalAmountOrder])

        orderLoop = True
        while orderLoop == True:
            print("\nDo you want to order more Bikes?")
            anotherOrder = str(input("\nIf yes, please enter 'Y' or else provide any input: ")).upper()
            if anotherOrder == "Y":
                displayOrderBikes()
                displayBikes()
                bike_id = validateBikeIdOrder()
                orderQuantity = validOrderQuantity()
                orderBikes(bike_id,orderQuantity)
                bikes = store2dList()
                orderedBikes = (bikes[bike_id-1][0])
                orderedBikesCompany = (bikes[bike_id-1][1])
                orderedBikesColor = (bikes[bike_id-1][2])
                orderedBikesPrice = (bikes[bike_id-1][4])
                totalAmountOrder = 0
                price = int(bikes[bike_id -1][4]) * orderQuantity
                totalAmountOrder += price
                orderedData.append([orderedBikesCompany,orderedBikes,orderedBikesColor,orderQuantity,orderedBikesPrice,totalAmountOrder])

            else:
                orderLoop = False
                print("\nThank You. Bike/s order succcessfully!!!")
                displayOrder(companyName,companyAddress, companyContact,orderedData)
                generateOrderBill(companyName,companyAddress, companyContact,orderedData)

    elif userInput == "3": #if user inputs 3 the main loop ends and the program ends
        runLoop = False
        end() #calling method that displays thank you message
       
    else: #if user inputs any other value other than 1, 2 or 3 a function that displays invalid input is called
        invalidInput()
