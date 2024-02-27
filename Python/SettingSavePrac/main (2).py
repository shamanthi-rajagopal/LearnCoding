# Created by Shamanthi Rajagopal
# Test file for saved settings to help with MazServStatus.py file
# For PinkByte 

# Global variables for settings
timeout = 10
retrySettings = 10
notifiSetting = "Email"
serverList = 10

def defaultSettings():
    global timeout, retrySettings, notifiSetting, serverList

    timeout = 10
    retrySettings = 10
    notifiSetting = "Email"
    serverList = 10

    writeSettingsToFile() #default settings are written in the text file

# The function for the settings, and it only displays the options
def Settings():
    global timeout, retrySettings, notifiSetting, serverList
    
    print(" ")
    print("################################ Settings ################################")
    print("1) Time Outsettings")
    print("2) Retry Connection Settings")
    print("3) Notification Settings")
    print("4) Server List")
    print("5) Default Settings ")
    print(" ")

#The function for changing the settings with user input
def changeSettings():
    global timeout, retrySettings, notifiSetting, serverList
    
    print("What settings would you like to change (1-5): ") #if it is any other options it just uses default options
    settingInput = input() 
    
    #Timeout Setting Option
    if settingInput == "1":
        while True:
            new_timeout = input("How many seconds would you like to put the Time Out session for: ")
            if new_timeout.isdigit() and int(new_timeout) > 0:
                timeout = int(new_timeout)
                print("The new time out time is: ", timeout)
                print(" ")
                break
            else:
                print("Please enter a valid positive integer for the timeout.")

        repeatChangeSettings()

    #Retry Settings Option
    elif settingInput == "2":
        while True:
            new_retrySettings = input("How many retries would you like the program to do in case of failed connections: ")
            if new_retrySettings.isdigit() and int(new_retrySettings) > 0:
                    retrySettings = int(new_retrySettings)
                    print("The new time out time is: ", retrySettings)
                    print(" ")
                    break
            else:
                    print("Please enter a valid positive integer for the connection retry settings.")
       
        repeatChangeSettings()


    #Notification Setting Option
    elif settingInput == "3":
        while True:
            new_notifiSetting = input("Which Notification Setting would you like (Email/SMS): ")
            if new_notifiSetting == "Email" or new_notifiSetting == "email" or new_notifiSetting == "EMAIL" or new_notifiSetting == "SMS" or new_notifiSetting == "sms":
                notifiSetting = str(new_notifiSetting)
                print("The Notification Settings have changed to: ", notifiSetting)
                print(" ")
                break
            
            else:
                print("Please enter Email or SMS: ")

        repeatChangeSettings()

    #Server List Setting Option
    elif settingInput == "4":
        while True:
            new_serverList = input("How many servers would you like to list: ")
            if new_serverList.isdigit() and int(new_serverList) > 0:
                    serverList = int(new_serverList)
                    print("The server list has ", serverList, " servers")
                    print(" ")
                    break
            else:
                    print("Please enter a valid positive integer for the # of servers.")
       
        repeatChangeSettings()

    #Default Settings
    else:
        print("Settings are put to default")
        
        defaultSettings()
        repeatChangeSettings()
        # Will be used in the actual MazServStatus.py file

# Function to repeat the change of settings until user is satisfied
def repeatChangeSettings():
    global timeout, retrySettings, notifiSetting, serverList
    
    while True:
        change_Settings = input("Would you like to change any other settings (y/n): ").lower()
        if change_Settings == "y":
            Settings()
            changeSettings()
            break
        elif change_Settings == "n":
            print("Done")
            break
        else:
            print("Invalid input. Please enter 'y' to change settings or 'n' to finish.")


def writeSettingsToFile():
    with open('settings.txt', 'w') as file:
        file.write(f"Timeout: {timeout}\n")
        file.write(f"Retry Settings: {retrySettings}\n")
        file.write(f"Notification Method: {notifiSetting}\n")
        file.write(f"# of Servers: {serverList}\n")
   
         
# The main function    
def main():
    global timeout, retrySettings, notifiSetting, serverList
    
    writeSettingsToFile()

    while True:
        updateSettings = input("Do you want to update and save to the Settings (y/n): ").lower()
        if updateSettings == "y":
            Settings()
            changeSettings()
            break
        elif updateSettings == "n":
            print("Program will continue to check the servers")
            print(" ")
            break
        else:
            print("Invalid input. Please enter 'y' to update settings or 'n' to continue to the server checking process.")

    # Prints the latest version of the settings after running through the settings options with the user
    print(" ")
    print("Program will continue here, the saved settings can be accessed in the later code with the variables during the original input")
    print(" ")
    print("Timeout: ", timeout)
    print("Retry Settings: ", retrySettings)
    print("Notification Method: ", notifiSetting)
    print("# of Servers: ", serverList)

    writeSettingsToFile()

# Code declaration starts here
main()