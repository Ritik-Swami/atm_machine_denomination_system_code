# This function gives number of notes required and remining in the database
def number_of_notes(amount, c_value):
    global atm_amount
    multipal = amount // int(c_value)
    x = denomination[c_value] - multipal
    y = x + multipal
    updated_multi = None

    for i in range(multipal):
        if y >= 0 and denomination[c_value] > 0: 
            denomination[c_value] = denomination[c_value] - 1
            if updated_multi == None:
                updated_multi = 1
            else:
                updated_multi += 1
            atm_amount = atm_amount - int(c_value)

    updated_amount = amount - updated_multi * int(c_value)
    print(f"""        |                                                |                 |
        |  Rs {c_value}                            {(4 - len(str(c_value))) * " "}           |       {updated_multi}  {(8 - len(str(updated_multi))) * " "}|
        |________________________________________________|_________________|""")

    return updated_amount

def required_amount(amount):
    global atm_amount
    if amount // 2000 != 0 and denomination['2000'] > 0:
        updated_amount = number_of_notes(amount, "2000")

    elif amount // 500 != 0 and denomination['500'] > 0:
        updated_amount = number_of_notes(amount, "500")
    
    elif amount // 200 != 0 and denomination['200'] > 0:
        updated_amount = number_of_notes(amount, "200")
        
    elif amount // 100 != 0 and denomination['100'] > 0:
        updated_amount = number_of_notes(amount, "100")
    
    else:
        print('Entered Amount Is Out Of Range')

    return updated_amount

def home(profile):
    global atm_amount
    global atm_amount_copy
    while True:
        print(F"""
========================================================================================
         __________________________________________________________________
        |                                                                  |
        |                       WelCome To Our ATM                         |
        |__________________________________________________________________|""")

        if profile == 'admin':
            step1 = int(input("""
         __________________________________________________________________
        |                                                                  |
        |   Do you want to continue                                        |
        |     1) Balance Inquiry                                           |
        |     2) Add Money                                                 |  
        |__________________________________________________________________|

        Enter The Option Number : """))  

            if step1 == 1:
                print(f"""        
         __________________________________________________________________
        |                                                                  |
        |                 Remaining Rupee Notes In ATM                     |
        |__________________________________________________________________|
        |                                             |                    |
        |   Rs 2000 Rupee Notes                       |        {denomination['2000']} {(10 - len(str(denomination['2000']))) * " "} |
        |   Rs 500 Rupee Notes                        |        {denomination['500']} {(10 - len(str(denomination['500']))) * " "} |
        |   Rs 200 Rupee Notes                        |        {denomination['200']} {(10 - len(str(denomination['200']))) * " "} |
        |   Rs 100 Rupee Notes                        |        {denomination['100']} {(10 - len(str(denomination['100']))) * " "} |
        |_____________________________________________|____________________|
        |                                             |                    |      
        |   Available Amount in the ATM               |    Rs {atm_amount}  {(10 - len(str(atm_amount))) * " "} |
        |_____________________________________________|____________________|""")

            elif step1 == 2:
                print("\n")
                added_amount = 0
                for currency_value in smallest_denomination:
                    amount_value = int(input(f"        Number of {currency_value}'s : "))
                    denomination[str(currency_value)] += amount_value
                    added_amount += (amount_value * currency_value)

                atm_amount = (denomination['2000']*2000 + denomination['500']*500 + denomination['200']*200 + denomination['100']*100)
                atm_amount_copy = len(str(atm_amount))
                print(f""" 
         __________________________________________________________________
        |                                          |                       |             
        |   Amount Added In ATM                    |      Rs {added_amount}  {(10 - len(str(added_amount))) * " "}  |     
        |__________________________________________|_______________________|""")
            
        if profile == 'user':
            try :
                user_amount = int(input(f"""
         __________________________________________________________________
        |                                                                  | 
        | Please Enter Amount in Multiples Of Rs 100, 200, 500, 2000 Only  |
        |__________________________________________________________________|
        
        Enter Withdrawal Amount : Rs """))

            except ValueError:
                user_amount = int(input("""
         __________________________________________________________________
        |                                                                  |
        |           Note : Please Enter Amount in Numbers Only             |
        |__________________________________________________________________|
        
        Enter Withdrawal Amount : Rs """))
            
            updated_amount = user_amount
            if user_amount % 100 == 0 and (atm_amount - user_amount + smallest_denomination[0]) >= smallest_denomination[0]:
                print(f""" 
         __________________________________________________________________
        |                                          |                       |             
        | Withdrawal Amount                        |       Rs {user_amount}  {(10 - len(str(user_amount))) * " "} |     
        |__________________________________________|_______________________|""")

                print("""
         __________________________________________________________________
        |                                                |                 |
        | Value Of Note                                  | Number Of Notes |
        |________________________________________________|_________________|""")     

                while updated_amount != 0:
                    updated_amount = required_amount(updated_amount)

            elif (atm_amount - user_amount) < smallest_denomination[0] and atm_amount != 0:
                print("""
         __________________________________________________________________
        |                                                                  |
        |            Entered Amount Is More Then ATM Balance               |
        |__________________________________________________________________|
        """)

            elif atm_amount == 0:
                print("""
         __________________________________________________________________
        |                                                                  |
        |          ATM Machine Is Empty. Please Try Again Later :)         |
        |__________________________________________________________________|""")

            else :
                print("""
         __________________________________________________________________
        |                                                                  |
        | Please Enter Amount in Multiples Of Rs 100, 200, 500, 2000 Only  |
        |__________________________________________________________________|""")
        

        continue_msg = int(input("""
         __________________________________________________________________
        |                                                                  |
        |   Do you want to continue                                        |
        |     1) Yes                                                       |
        |     2) No                                                        |  
        |__________________________________________________________________|

        Enter The Option Number : """))
        if continue_msg == 1 :
            continue
        else:
            print("""
         __________________________________________________________________
        |                                                                  |
        |                                                                  |
        |                                                                  |
        |                                                                  |
        |                           THANK YOU                              |
        |                                                                  |
        |                                                                  |
        |                                                                  |
        |__________________________________________________________________|""")
            break

######################################################################################################


# Using pyhton dictionary for future database updation like json (NoSQL Database)
denomination = {
    '2000': 10,    # 5 notes of 2000
    '500': 10,     # 5 notes of 500
    '200': 10,     # 5 notes of 200
    '100': 10      # 5 notes of 100
}

atm_amount = 28000  # ATM Balence
atm_amount_copy = len(str(atm_amount))

user_db = {
    'admins': [{
        'id' : 1,
        'name' : 'admin',
        'password' : "12345"
    }],
    'users' : [{
        'id' : 1,
        'name' : 'ritik',
        'password' : "67890",
        'amount' : 20000
    }]
}

smallest_denomination = [2000,500,200,100] #Taking the smallest no of denomination inside the ATM
smallest_denomination.sort()
updated_amount = None


while True:
    start = int(input("""
         __________________________________________________________________
        |                                                                  |
        |     1) Sign In                                                   |
        |     2) Exit                                                      |  
        |__________________________________________________________________|

        Enter The Option Number : """))
    
    if start == 1 :
        user_profile = input("\n        User Profile (ex : 'Admin' or 'User') : ")
        if user_profile.lower() == "admin":
            admin_name = input("\n        Admin Name : ")
            admin_password = input("        Password : ")
            if (admin_name == user_db['admins'][0]['name'] and admin_password == user_db['admins'][0]['password']):
                print("""
         __________________________________________________________________
        |                                                                  |
        |                        Admin Access Granted                      |
        |__________________________________________________________________|""")
                home('admin')
            else :
                print("""
         __________________________________________________________________
        |                                                                  |
        |                   Invalid Username or Password                   |
        |__________________________________________________________________|""")

        elif user_profile.lower() == "user":
            user_name = input("\n        User Name : ")
            user_password = input("        Password : ")
            if (user_name == user_db['users'][0]['name'] and user_password == user_db['users'][0]['password']):
                print("""
         __________________________________________________________________
        |                                                                  |
        |                        User Access Granted                       |
        |__________________________________________________________________|""")
                home('user')
            else :
                print("Invalid Username or Password")
        
        else :
            break
    elif start == 2:
        break
    else :
        break