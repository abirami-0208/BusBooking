from Passenger_Info import PassengerDataCsv
from ticket_show import TicketShow
from admin import Admin


global ch  # declared global variable

print("---------------------------------------------------")
print("           Welcome To ABC Bus Travel               ")
print("---------------------------------------------------")
print()

def start(): #called function
    print("1. Admin Registration :")
    print("2. Admin Login        :")
    print()
    adminObj = Admin()
    Pobj = PassengerDataCsv()
   
    ch = int(input("Choose Correct option :"))

    if ch == 1:
        #admin class object creation
        adminObj.adminregistration()

    if ch == 2:
        adminObj.adminlogin()
        print()
        print("1. Passenger Registration :")
        print("2. Show Ticket            :")
        print()
        ch = int(input("Choose Any One Option :"))
        if ch == 1:
            Pobj.PassengerRegistration()
            Pobj.location()
            Pobj.busselection()
            Pobj.seatselection()
            Pobj.payment()
            Pobj.saveInfo()
        elif ch ==2:
            obj = TicketShow()
            obj.ticketShow()

start()#calling function
