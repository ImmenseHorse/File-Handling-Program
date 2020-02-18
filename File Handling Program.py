#This program was written by Duc Nguyen on Dec 9, 2019.
#This program be shown a menu with 4 choices:
#1. Display the file
#2. Add a number to the file
#3. Delete a number from the file
#4. Exit the program
#For the first option, the user will be shown all the numbers in the file.
#For the second option, if the number does not already exist in the file, the
#number will be inserted into the correct location in the file. The user will
#either be given confirmation that the addition was successful or that the
#number was not added because it already existed. For the third option, the
#user will be asked for a number to be removed. The user will either be given
#confirmation that the removal was successful or that the number did not exist.


KEYS = "keys.txt" #The name of the input file


def Menu():
    """This function displays the main menu with 4 choices."""
    
    print("1. Display the file")
    print("2. Add a number to the file")
    print("3. Delete a number from the file")
    print("4. Exit the program")
    
 
def CreateList():
    """This function will accept a filename and return a list of integers."""
    
    #in_file - the file object associated with the keys text file
    #entire_list - the list of integers existed in the keys text file
    
    in_file = open(KEYS, "r")
    entire_list = in_file.readlines()
    in_file.close()
    for x in range(len(entire_list)):
        entire_list[x] = entire_list[x].strip()
    return entire_list

def DisplayFile():
    """This function will display the keys text file"""
    
    #in_file - the file object associated with the keys text file
    #entire_file - all the numbers in the keys text file
    
    in_file = open(KEYS, "r")
    entire_file = in_file.read()
    print(entire_file)
    in_file.close()
      
def Exists(usernumber, entire_list):
    """This function will accept a number and a list of integers. The function
       will return the value of True if the number exists in the list and False
       if it does not"""
    
    #usernumber - the user's entered number
    #entire_list - the list of integers existed in the keys text file
    
    if str(usernumber) in entire_list:
        return True
    else:
        return False

def DeleteNumber(usernumber, entire_list):
    """This function will delete a number entered by the user if it existed in
       the keys text file and give confirmation that the removal was successful
       or that the number did not exist"""
    
    #usernumber - the user's entered number
    #out_file - the file object associated with the keys text file
    #entire_list - the list of integers existed in the keys text file
    
    if Exists(usernumber, entire_list) == False:
        print("The removal was unsuccessful as the number did not exist.")
    else:
        out_file = open(KEYS,"w")
        for x in range(len(entire_list)):
            if entire_list[x] == str(usernumber):
                x = x+1 
            else:
                out_file.writelines(entire_list[x]+"\n")
        out_file.close()
        print("The removal was successful.")
    print()

def AddNumber(usernumber, entire_list):
    """This function will insert a number into the correct location in the file
       if it does not already exist in the file and give confirmation that the
       addition was successful or that the number was not added because it
       already existed"""
    
    #out_file - the file object associated with the keys text file
    #entire_list - the list of integers existed in the keys text file
    #usernumber - the user's entered number
    
    if Exists(usernumber, entire_list) == True:
        print("The number was not added because it already existed.")
    else:
        out_file = open(KEYS,"w")
        for x in range(len(entire_list)):
            if int(entire_list[x]) < usernumber:
                out_file.write(entire_list[x]+"\n")
        out_file.write(str(usernumber)+"\n")
        for x in range(len(entire_list)):
            if int(entire_list[x]) > usernumber:
                out_file.write(entire_list[x]+"\n")
        out_file.close()
        print("The addition was successful.")
    print()
                
def main():
    """This is the mainline for the program"""
    
    #keepgoing - the flag for the while loop
    #entire_list - the list of integers existed in the keys text file
    #userinput - the user's entered number
    #addnum - the number to be added to the keys text file
    #deletenum - the number to be removed from the keys text file
    
    keepgoing = True
    while keepgoing:
        entire_list = CreateList()
        Menu()
        userinput = int(input("Please enter a number from 1 to 4. "))
        while userinput < 1 or userinput > 4:
            print("The number entered is invalid.")
            userinput = int(input("Please enter a number from 1 to 4. "))
        if userinput == 1:
            DisplayFile()
        elif userinput == 2:
            addnum = int(float(input("Please enter a number to be added ")))
            AddNumber(addnum, entire_list)
        elif userinput == 3:
            deletenum = int(float(input("Please enter a number to be removed ")))            DeleteNumber(deletenum, entire_list)
        else:
            keepgoing = False
            print("Thank you for using the program!")
main()
           
            
        
            
                
                
            
            
                    
    
    


        
    
    
