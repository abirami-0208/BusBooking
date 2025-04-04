
# BUS TICKET BOOKING SYSTEM USING PYTHON

    The  Bus Ticket Booking System is a Python-based application designed to streamline the process of bus ticket booking. The system allows administrators to manage registrations and logins, while passengers can register, choose bus routes, select seats, and complete payments. The application provides functionalities to handle conflicts in seat booking and displays tickets for passengers.


## Features

1. Passenger Registration: Register as a passenger to book a ticket.

2. Login: Log in as a passenger for bookings and access the ticket.

3. Location: Choose the departure and destination location.

4. Choose Travel: Select the available travels based on travel timing and fare.

5. Choose bus type: Select  the bus type as AC or NON-AC by which the fare would be differ for type of bus. 

6. Seat Selection: Interactive seat selection for passengers to choose their preferred seats.

7. Multiple Passenger Booking: Book multiple seats for multiple passengers in one go.

8. Conflict Detection: Detects and handles conflicts when the same seat is selected for different passengers.

9. Payment Process: Checking for enter allotted payments.

10. OTP Generation and Validation: Secures the booking process with a one-time password (OTP) generation and validation.

11. Ticket Display: Show tickets to passengers after booking.

12. Error Handling: Robust error handling for invalid inputs and exceptions.

13. File Storing: Manages local storage of passenger data and tickets in CSV format.


## OTP Generation and Validation
    The OTP validation ensures that the user is the rightful owner before confirming the booking. It generates a secure one-time password, sends it to the user, and validates the entered OTP against the generated one.

##Implementation:
    
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

## File Storage
    The Bus Ticket Booking System stores passenger and booking data in CSV format to manage information locally. This ensures that user data and booking details are securely saved on the local machine, making it easy to view and manage.

##Passenger Data Storage:
Each entry in the CSV file includes the following details:

o	Passenger ID
o	Name
o	Contact Number
o	Gender
o	Date of Journey
o	Location
o	Travel Name
o	Bus ID
o	Duration
o	Seat Number
o	Bus type
o	Bus fare
o	Payment Status

##Implementation:
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

![passengerdata](https://github.com/user-attachments/assets/c8210947-354a-4edc-9548-4167ec797114)

## Display ticket

    The bus ticket includes essential travel details for the passenger. It specifies the passenger's name, bus name, source, destination, travel date, departure time, seat number, and booking ID.

o	When a passenger registers, their information is stored in passengerData.csv.
o	This file is updated each time a booking is made.The Passenger was able to see their ticket by entering passenger Id.

![ticket_display](https://github.com/user-attachments/assets/8f138a1e-1a4e-43e7-8db8-a87819422875)

## Key Details

Passenger Booking:
o	Passengers can register, select buses, choose seats, and make payments.
o	Ensures seat availability and prevents overbooking.

Error Handling:
o	The system provides feedback for invalid inputs and resolves conflicts if the same seat is selected for multiple passengers.

Invalid input:
o	Ensure that inputs are valid numbers.
o	If an invalid option is selected, the system will prompt the user to try again.

Seat already booked:
o	If a selected seat is already booked, the user will be informed and asked to choose a different seat.

Conflict Resolution:
o	If the same seat is booked for multiple passengers, the system will detect it and prompt users to correct the booking.
