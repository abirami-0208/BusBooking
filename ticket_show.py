from Passenger_Info import *
class TicketShow:

    def ticketShow(self):
        bln = [] # list for storing data and retrieving from passengerData.csv file
        with open("passengerData.csv",'r+',newline="") as f:
            r =  csv.reader(f)
            data = list(r)
            id = int(input("Enter Your Booking Id  :"))
            for i in data:
                if id == int(i[0]):
                    for j in i:
                        bln.append(j)
                    break
        #print(bln)  
        print("-----------------------------------------------------------------------------------")
        print("                          ADS Bus Travel                                      ")
        print("-----------------------------------------------------------------------------------")
        print()
        print(" e_Ticket :", "Nagpur Address              : Hingna Road Priyadarshini T-Point")
        print("           ", "Phone No\Mob No             : 8000800088,8888880000            ")
        print()
        print("",bln[3],"------------->",bln[4],"       "," Passenger Id        :",bln[0])
        print(" Passenger Name :", bln[1],"          ","       Number of Passenger :",bln[2])
        print(" Mob no :", bln[15],"                ","        Gender :",bln[14])
        print("___________________________________________________________________________________")
        print()
        print(" Date of Booking :",bln[6],"                "," Seat No  :           ",bln[9])
        print(" Travel Timing   :",bln[7],"     "," Duration :           ",bln[8])
        print()
        print("___________________________________________________________________________________ ")
        print(" Bus Type :       ",bln[10],"                 "," Travel Name :        ",bln[5])
        print(" Bus Fare :       ",bln[11],"                 ","Payment Status :      ",bln[13])
        print()
        print("------------------------------------------------------------------------------------")
                
