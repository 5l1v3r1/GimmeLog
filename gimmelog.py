import sys
import re 
import os 

global OutContent 
OutContent = ""

def menu(arg, OutContent):
    line1 = "\nApache Log Analyser - Main Menu"
    print(line1)
    print("\n1) Successful Requests\n2) Failed Requests\nq) Quit")
    choice = input("Select an option [1-2] q to quit: ")
    
    if choice == "1":
        succes_menu(arg, OutContent)
    if choice == "2":
        fail_menu(arg, OutContent)
    if choice == "q":
        print("GoodBye!")
        sys.exit(0)
      
def succes_menu(arg, OutContent):
    line1 = "\nApache Log Analyser - Successful Requests Menu\n"
    print(line1)
    for letter in line1: #for each word in the variable print =  end = '' will print it horizontally
        print('=', end='')      
    print("\n1) How many total requests (Code 200)\n2) How many requests from Seneca (IPs starting with 142.204)\n3) How many requests for isomaster-1.3.13.tar.bz2\nq) Return to Main Menu\n")
    
    choice = input("Select an option [1-3] q to quit:")
    
    if choice == "1":
        total_200(arg, OutContent)
    if choice == "2":
        senIP(arg, OutContent)
    if choice == "3":
        isoMaster(arg, OutContent)
    if choice == "q":
        menu(arg, OutContent)
    else:
        succes_menu(arg, OutContent)
        
def total_200(arg, OutContent):
    counter = 0 # set a counter to 0 
    for line in OutContent or allFileContents: #for each line in load if the " 200 " is found add 1 to the counter and repeat until done. 
       if re.findall(r"\s\b200\b\s", line):
           counter += 1
    print("\nTotal of (Status Code) 200 request:", counter)

def senIP(arg, OutContent):
    counter = 0 
    for line in OutContent or allFileContents:
        if re.findall(r"\b142.204\b", line):
            counter += 1
    print("\nTotal of Requests from 142.204:",counter)
    
def isoMaster(arg, OutContent):
    counter = 0 #creates a counter to increment from starting from 0
    for line in OutContent or allFileContents:
        if re.findall(r"\bisomaster-1.3.13.tar.bz2\b", line): #finds all the requests that contain what is inside \b \b it will not look further to the rest of strings.
            counter += 1 #increment counter by one each time the condition is met. 
    print("\nTotal requests to isomaster-1.3.13.tar.bz2:",counter)
    
######################## Successful ####################### 

def fail_menu(arg, OutContent):
    line1 = "Apache Log Analyser - Failed Requests Menu"
    print(line1)
    for letter in line1:
        print('=',end='')
    print("\n1) How many total failed requests (Codes 404, 400, 500, 403, 405, 408, 416)\n2) How many invalid requests for wp-login.php\n3) List the filenames for failed requests for files in /apng/assembler/data\nq) Return to Main Menu\n")
    
    choice = input("Select an option [1-3] q to go back:")

    if choice == "1":
        failed_Request(arg, OutContent)
    if choice == "2":
        invalid_WP(arg, OutContent)
    if choice == "3":
        invalid_Apng(arg, OutContent)
    if choice == "q":
        menu(arg, OutContent)
    else: 
        fail_menu(arg, OutContent)

######################## Failed #######################  

def failed_Request(arg, OutContent):
    counter_404 = 0 
    counter_400 = 0 
    counter_500 = 0 
    counter_403 = 0 
    counter_405 = 0 
    counter_408 = 0 
    counter_416 = 0 
    
    for line in OutContent or allFileContents:
        if re.findall(r"\s\b404\b\s", line):
        #if " 404 " in line:
            counter_404 += 1
        if re.findall(r"\s\b400\b\s", line):
        #if " 400 " in line:
            counter_400 += 1
        if re.findall(r"\s\b500\b\s", line):
        #if " 500 " in line:
            counter_500 += 1
        if re.findall(r"\s\b403\b\s", line):
        #if " 403 " in line:
            counter_403 += 1
        if re.findall(r"\s\b405\b\s", line):
        #if " 405 " in line:
            counter_405 += 1
        if re.findall(r"\s\b408\b\s", line):
        #if " 408 " in line:
            counter_408 += 1
        if re.findall(r"\s\b416\b\s", line):
        #if " 416 " in line: 
            counter_416 += 1
    
    print("\n=====================================")
    print("Total 404 request: ", counter_404)
    print("Total 400 request: ", counter_400)    
    print("Total 500 request: ", counter_500)
    print("Total 403 request: ", counter_403)
    print("Total 405 request: ", counter_405)
    print("Total 408 request: ", counter_408)
    print("Total 416 request: ", counter_416)
    print("=====================================\n")

def invalid_WP(arg, OutContent):
    counter = 0 #Start a counter at 0 
    for line in OutContent or allFileContents:  # loop through each line in the files
        #check if regex is matched () = groups # . = Any number of matches
        #.* = any number of anything \s = space \bword\b = search word only avoids wording or words  
        if re.findall(r'(./wp-login.php).*(\s\b404\b\s)', line): 
            counter += 1 # add one to the counter if the match exist.             
    print("\nTotal failed requests to wp-login.php: ", counter, "\n")

def invalid_Apng(arg, OutContent):
    counter = 0 #Start a counter at 0 
    for line in OutContent or allFileContents:  # loop through each line in the files
        #check if regex is matched () = groups # . = Any number of matches
        #.* = any number of anything \s = space \bword\b = search word only avoids wording or words  
        if re.findall(r'(./apng/assembler/data).*(\s\b404\b\s)', line): 
            counter += 1 # add one to the counter if the match exist.             
    print("\nTotal failed requests to /apng/assembler/data: ", counter, "\n")
    
def main():
    if len(sys.argv)== 1: 
        sys.exit("[+] No arguments passed [+]\nUsage: program.py [filenames]\noptional arguments:\n-d, --default            Skips to Total 200 Requests and exit")
    script = sys.argv[0]
    action = sys.argv[1]
    
    if sys.argv[1] == '--default' or sys.argv[1] == '-d':
        filenames = sys.argv[2:]
    else:
        filenames = sys.argv[1:]
        
    OutContent = filenames 
    
    #Load files with arguments -d & --default
    print("Loading Files....", filenames)

    for arg in filenames:
        try:
            myfile = open(arg, "r")
            fileContent = myfile.readlines()
            myfile.close()
            OutContent = OutContent + fileContent
        except OSError:
            print("File could not be opened " + str(filenames) + "\n")
            print("Usage: program.py [filenames]\noptional arguments:\n-d, --default            Skips to Total 200 Requests and exit")
            sys.exit()
           
    if action == '--default' or action == '-d':
        counter = 0 # set a counter to 0 
        for line in OutContent: #for each line in load if the " 200 " is found add 1 to the counter and repeat until done. 
            if re.findall(r"\s\b200\b\s", line):
                counter += 1
        print("\nTotal of (Status Code) 200 request:", counter)
    else:
        if sys.argv[1]:
            menu(arg,OutContent)
    
if __name__ == "__main__":
    main()
