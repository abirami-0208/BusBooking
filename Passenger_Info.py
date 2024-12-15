import csv
from travel_info import Travelinfo
import random


class PassengerInfo(Travelinfo):
    def __init__(self):

        super(PassengerInfo,self).__init__()
        
        self.name = None
        self.noOfPassenger = None
        self.gender = None
        self.departure = None
        self.destination = None
        self.date = None
        self.seatNo = None
        self.bustype = None
        self.busFare = None
        self.autoInc = 1
        self.countcol= 0
        self.Amount = 0
        self.otp_pass = 0
        self.otp_value = 0
        self.bookingList = []
        self.payment_completed = False
        self.payment_status = None
        self.mob = 0
        
        

    def PassengerRegistration(self):
        self.name = input("Enter your Name:")
        self.noOfPassenger = int(input("Enter the number of Passenger:"))
        self.gender = input("Enter the gender:(male/female)")
        self.mob = int(input("Enter your contact number:"))
        self.date = input("Enter the date of journey(yyyy-mm-dd):")

    def location(self):
        #Pobj = PassengerInfo()
        print("""Departure Location:
              1.Chennai
              2.Coimbatore
              3.Trichy
              4.Madurai""")

        dpl = int(input("Enter the departure location:")) #departure location
        print("Choose the destination location:")
        if dpl == 1:
            self.departure = "Chennai"
            print("""
              1.Coimbatore
              2.Trichy
              3.Madurai""")
        elif dpl == 2:
            self.departure = "Coimbatore"
            print("""
              1.Chennai
              2.Trichy
              3.Madurai""")
        elif dpl == 3:
            self.departure = "Trichy"
            print("""
              1.Coimbatore
              2.Chennai
              3.Madurai""")
        elif dpl == 4:
            self.departure = "Madurai"
            print("""
              1.Coimbatore
              2.Trichy
              3.Chennai""")
        else:
            print("Enter the correct location!")
            location()

        #Travels available
        dl = int(input())
        if dpl == 1:
            if dl == 1:
                self.destination = "Coimbatore"
                self.chennai_coimbatore()
            elif dl == 2:
                self.destination = "Trichy"
                self.chennai_trichy()
            elif dl == 3:
                self.destination = "Madurai"
                self.chennai_madurai()
            else :
                print("Invalid option! choose correct destination")
                self.location()

        elif dpl == 2:
            if dl == 1:
                self.destination = "Chennai"
                self.chennai_coimbatore()
            elif dl == 2:
                self.destination = "Trichy"
                self.coimbatore_trichy()
            elif dl == 3:
                self.destination = "Madurai"
                self.coimbatore_madurai()
            else :
                print("Invalid option! choose correct destination")
                self.location()

        elif dpl == 3:
            if dl == 1:
                self.destination = "Coimbatore"
                self.coimbatore_trichy()
            elif dl == 2:
                self.destination = "Chennai"
                self.chennai_trichy()
            elif dl == 3:
                self.destination = "Madurai"
                self.trichy_madurai()
            else :
                print("Invalid option! choose correct destination")
                self.location()

        elif dpl == 4:
            if dl == 1:
                self.destination = "Coimbatore"
                self.coimbatore_madurai()
            elif dl == 2:
                self.destination = "Trichy"
                self.trichy_madurai()
            elif dl == 3:
                self.destination = "Chennai"
                self.chennai_madurai()
            else :
                print("Invalid option! choose correct destination")
                self.location()


    def busselection(self):
        
        bus = int(input("""Enter the bus type
                                 1.NON-AC
                                 2.AC
                                 Note: The fare will be differ for AC/Non-AC buses"""))
        if bus == 1:
            self.bustype = "NON-AC"
            self.Amount = self.noOfPassenger * self.amt
            print("Bus Fare:",self.Amount)
        elif bus == 2:
            self.bustype = "AC"
            self.Amount = self.noOfPassenger * (self.amt + 300)
            print("For AC bus the fare is",self.Amount)
        else:
            print("Invalid option! please enter correct data")
            self.busselection()
            

    def seatselection(self):
        seatNoList = list(range(1, 31))
        booked_seats = []  # Track booked seats from CSV

        # Load booked seats from CSV file
        try:
            with open("passengerData.csv", 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) > 12 and row[12] == self.bus_id:
                        seat_str = row[9].strip("[]").replace(" ", "")
                        if seat_str:
                            seat_numbers = seat_str.split(",")
                            for seat in seat_numbers:
                                if seat.isdigit():
                                    booked_seats.append(int(seat))

        except FileNotFoundError:
            # Default seat arrangement if file is not found
            print("[1]__[2]__[3]__[4]__[5]__[6]__[7]__[8]__[9]__[10]")
            print("[11]_[12]_[13]_[14]_[15]_[16]_[17]_[18]_[19]_[20]")
            print("[21]_[22]_[23]_[24]_[25]_[26]_[27]_[28]_[29]_[30]")
            seatNoList = list(range(1, 31))

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return

        # Update available seats by removing booked seats
        for seat in booked_seats:
            if seat in seatNoList:
                seatNoList.remove(seat)

        print(f"Available seats: {seatNoList}")

        for i in range(self.noOfPassenger):
            while True:
                try:
                    self.seatNo = int(input(f"Choose a Seat Number for Passenger {i + 1} (1-30): "))
                
                    if self.seatNo < 1 or self.seatNo > 30:
                        print("Invalid seat number. Please choose a number between 1 and 30.")
                    elif self.seatNo in booked_seats:
                        print("Seat already booked! Please choose a valid seat.")
                    elif self.seatNo in seatNoList:
                        self.bookingList.append(self.seatNo)
                        seatNoList.remove(self.seatNo)
                        print(f"Seat {self.seatNo} booked successfully for Passenger {i + 1}.")
                        #print(f"Your booking list: {self.bookingList}")
                        print(f"Available seats: {seatNoList}")
                        break
                    else:
                        print("Seat already booked. Please choose another seat.")
                except ValueError:
                    print("Invalid input. Please enter a valid seat number.")
        
    def generate_otp(self):
        self.otp_value = random.randint(1000,9999)
        print("Your One Time Password(OTP) is:",self.otp_value)


    def validate_otp(self):
        while True:
            try:
                self.otp_pass = int(input("Enter your OTP value:"))
                if(self.otp_pass == self.otp_value):
                    print("Your payment is Successfully completed!!")
                    print("Your Booking Completed successfully")
                    self.payment_status = "yes"
                    return True
                else:
                    print("Wrong OTP")
                    op = int(input("""Do you continue
                      1.yes
                      2.no"""))
                    if op == 1:
                        print("Regenerating OTP...")
                        self.generate_otp()
                        #self.otp_check()
                    else:
                        print("Payment process terminated.")
            except ValueError:
                print("Invalid input! PLease enter a valid numeric OTP")
    def payment(self):
        while True:
            try:
                if self.payment_completed:
                    print("This payment has already been completed.")
                    return False
                
                fare = int(input("Enter the payment amount:"))
                if(fare == self.Amount):
                    self.generate_otp()
                    if self.validate_otp():
                        self.payment_completed = True
                        return True
                    
                else:
                    print("Invalid amount!")
                    op = int(input("""Do you continue
                      1.yes
                      2.no"""))
                    if op == 1:
                        print("Please enter valid amount!!")
                        self.payment()
                    else:
                        return False
            except ValueError:
                print("Invalid input! Please enter a valid numeric amount.")

class PassengerDataCsv(PassengerInfo):
    #Pobj = PassengerDataCsv()
    def saveInfo(self):
        try:
            with open("passengerData.csv",'r+',newline="") as f:
                r =  csv.reader(f)
                data = list(r)
                #print(self.data)
                for  i in data:
                    self.autoInc += 1
                    for j in i:
                        self.countcol +=1
                    print()
                print("Passenger id(Note this id for getting ticket):",self.autoInc)    
            
        except:
            print("File has not available")
        finally:     
            with open("passengerData.csv",'a+',newline="") as f:
                w =  csv.writer(f)
                #w.writerow(["Auto Increment","passenger Name","Number of Passenger","Departure Location","Destination Location","ddmmyyyy","Seat No","Select Bus Type","Bus Fare"])
                w.writerow([self.autoInc,self.name,self.noOfPassenger,self.departure,self.destination,self.travel,self.date,self.timing,self.duration,self.bookingList,self.bustype,
                            self.Amount, self.bus_id,self.payment_status, self.gender,self.mob])
                print("Data Save successfully")
                print()
    















    
"""    
            
def saveInfo(self):
        try:
        # Attempt to read the file and count records
            with open("passengerData.csv", 'r+', newline="") as f:
                r = csv.reader(f)
                data = list(r)
            
            # Set auto-increment based on number of records
                self.autoInc = len(data)
            
            # Print the number of records found
                print("Number of Records Found In Database:", self.autoInc)
    
        except FileNotFoundError:
            print("File not found. A new file will be created.")
            self.autoInc = 0  # Initialize for new file
    
        except Exception as e:
            print(f"An error occurred: {e}")
    
        finally:
        # Write new data to the file
            with open("passengerData.csv", 'a+', newline="") as f:
                w = csv.writer(f)
            
            # Header row can be written if `self.autoInc == 0`
                if self.autoInc == 0:
                    w.writerow(["Auto Increment", "Passenger Name", "Number of Passengers", 
                            "Departure Location", "Destination Location", "Travel Name", "Travel Date",
                            "Travel Timing", "Duration", "Seat No", "Select Bus Type", "Bus Fare"])
            
            # Write the new passenger data
                w.writerow([
                    self.autoInc + 1, self.name, self.noOfPassenger, self.departure, 
                    self.destination, self.travel, self.date, self.timing, 
                    self.duration, self.bookingList, self.bustype, self.Amount
                ])
            
                print("Data saved successfully!")"""
            



    
            
        

        

    


       

    


    
     

    

    

    

        

        
                
            
        
            

















            
            
            
        
        
    


















   
