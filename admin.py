import csv
class Admin:
    def __init__(self):
        self.username = None
        self.password = None

    def adminregistration(self):
        print("---------------------------------------------------")
        with open("AdminCredentials.csv","a",newline = "") as file:
            writer = csv.writer(file)
            self.username = input("Enter username(mail id):")
            self.password = input("Enter and set Password:")
            writer.writerow([self.username,self.password])
            print("Registration Successfully")
        print("---------------------------------------------------")

    def adminlogin(self):
        clist = []         #store username and password in this list
        with open("AdminCredentials.csv","r",newline = "") as file:
            reader = csv.reader(file)
            data = list(reader)
            for i in data:
                clist.append(i)
           
            print("---------------------------------------------------")
            print()
            self.username = input("Enter  username  :")
            self.password = input("Enter  password  :")
            flag = 0
            for j in clist:
                if self.username == j[0] and self.password == j[1]:
                    flag = 1
                    break
            if flag == True:
                print("Login Successfully")
            else:
                print("Invalid data!")


                 
             
             
            
                
            
            



        
    
