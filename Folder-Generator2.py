import os                                                           #Import the os library that alows to create the directories.
i=0                                                                 #This int will contain the number of the folder that has to be created.
size=int(input("Enter the size of the Vault(1-2-3-4-5):"))          #Enables the option to chose the number of folders. There are 5 options: 1,2,3,4,5
j="0"*39                                                            #This string  simply stores zeros.
k=""                                                                #The path of each folder will come from here.
count=1                                                             #This takes a count of the folders that have been created.
flag=True                                                           #This flag will end the next while loop when neccesary.
dirs=(2**15)*(2**(size*5))                                          #Stores the number of folders that will be created depending on the size input
path=os.path.dirname(os.path.realpath(__file__))                    #Gives the path of the the actual file
while flag:                                                         #The loop main loop.
    k=f"{j[0:(41-len(bin(i)))]}{bin(i).replace('0b','')}"           #This will create the path of the folders.
    if size==1:                                                      
        os.makedirs(f"{os.path.dirname(os.path.realpath(__file__))}/Vault(2^20)/{k[20]}/{k[21]}/{k[22]}/{k[23]}/{k[24]}/{k[25]}/{k[26]}/{k[27]}/{k[28]}/{k[29]}/{k[30]}/{k[31]}/{k[32]}/{k[33]}/{k[34]}/{k[35]}/{k[36]}/{k[37]}/{k[38]}")#This comand creates the folders.
    if size==2:
        os.makedirs(f"{os.path.dirname(os.path.realpath(__file__))}/Vault(2^25)/{k[15]}/{k[16]}/{k[17]}/{k[18]}/{k[19]}/{k[20]}/{k[21]}/{k[22]}/{k[23]}/{k[24]}/{k[25]}/{k[26]}/{k[27]}/{k[28]}/{k[29]}/{k[30]}/{k[31]}/{k[32]}/{k[33]}/{k[34]}/{k[35]}/{k[36]}/{k[37]}/{k[38]}")#This comand creates the folders.
    if size==3:
        os.makedirs(f"{os.path.dirname(os.path.realpath(__file__))}/Vault(2^30)/{k[10]}/{k[11]}/{k[12]}/{k[13]}/{k[14]}/{k[15]}/{k[16]}/{k[17]}/{k[18]}/{k[19]}/{k[20]}/{k[21]}/{k[22]}/{k[23]}/{k[24]}/{k[25]}/{k[26]}/{k[27]}/{k[28]}/{k[29]}/{k[30]}/{k[31]}/{k[32]}/{k[33]}/{k[34]}/{k[35]}/{k[36]}/{k[37]}/{k[38]}")#This comand creates the folders.
    if size==4:
        os.makedirs(f"{os.path.dirname(os.path.realpath(__file__))}/Vault(2^35)/{k[5]}/{k[6]}/{k[7]}/{k[8]}/{k[9]}/{k[10]}/{k[11]}/{k[12]}/{k[13]}/{k[14]}/{k[15]}/{k[16]}/{k[17]}/{k[18]}/{k[19]}/{k[20]}/{k[21]}/{k[22]}/{k[23]}/{k[24]}/{k[25]}/{k[26]}/{k[27]}/{k[28]}/{k[29]}/{k[30]}/{k[31]}/{k[32]}/{k[33]}/{k[34]}/{k[35]}/{k[36]}/{k[37]}/{k[38]}")#This comand creates the folders.
    if size==5:
        os.makedirs(f"{os.path.dirname(os.path.realpath(__file__))}/Vault(2^40)/{k[0]}/{k[1]}/{k[2]}/{k[3]}/{k[4]}/{k[5]}/{k[6]}/{k[7]}/{k[8]}/{k[9]}/{k[10]}/{k[11]}/{k[12]}/{k[13]}/{k[14]}/{k[15]}/{k[16]}/{k[17]}/{k[18]}/{k[19]}/{k[20]}/{k[21]}/{k[22]}/{k[23]}/{k[24]}/{k[25]}/{k[26]}/{k[27]}/{k[28]}/{k[29]}/{k[30]}/{k[31]}/{k[32]}/{k[33]}/{k[34]}/{k[35]}/{k[36]}/{k[37]}/{k[38]}")#This comand creates the folders.
    print(f"Folders created:{count*2}/{dirs}")                      #Prints how many folders were created.
    count+=1                                                        #Add one to count.
    i+=1                                                            #Add one to i.
    if count*2==dirs:                                                     #When all the folders are created.
        flag=False                                                  #It ends the loop.
        print(f"{dirs} Folders created successfully!")              #And prints a message.
#Have in mind that this process can take up to days and delete it may be impossible.
#Size options:
#Option 1: 2^20 Folders
#Option 2: 2^25 Folders
#Option 3: 2^30 Folders
#Option 4: 2^35 Folders
#Option 5: 2^40 Folders
#I dont recomend to use the full size 5 (2^40 Folders).
#This proyect was created by Valentino Amato: https://github.com/AMATO174/Folder-Generator2 . 