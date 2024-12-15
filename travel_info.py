class Travelinfo():

    
    def __init__(self):
        self.bustype = None
        self.travel = None
        self.timing = None
        self.duration = None
        self.bustype = 0
        self.amt = 0
        self.bus_id = None

    def choose_travel(self,options):
        ch = int(input("Choose the Travel:"))
        self.travel = list(options.keys())[ch - 1]
        self.timing = options[self.travel]["timing"]
        self.duration = options[self.travel]["duration"]
        self.amt = options[self.travel]["amt"]
        self.bus_id = options[self.travel]["id"]
        
        
    def chennai_coimbatore(self):
         
         print('''Bus details, Time and Duration, Payment:
                    1. LION Travels (21:50 to 04:35) 6h 45m - ₹600
                    2. KPN Travels (22:00 to 05:00) 7h 00m - ₹650
                    3. Parveen Travels (23:00 to 05:30) 6h 30m - ₹700
                    4. SRM Travels (20:30 to 03:00) 6h 30m - ₹720
                    5. YBM Travels (22:15 to 04:45) 6h 30m - ₹680 ''')
         options = {
    "LION Travels": {"id": "A1", "timing": "21:50 to 04:35", "duration": "6h 45m", "amt": 600},
    "KPN Travels": {"id": "A2","timing": "22:00 to 05:00", "duration": "7h 00m", "amt": 650},
    "Parveen Travels": {"id": "A3","timing": "23:00 to 05:30", "duration": "6h 30m", "amt": 700},
    "SRM Travels": {"id": "A4","timing": "20:30 to 03:00", "duration": "6h 30m", "amt": 720},
    "YBM Travels": {"id": "A5","timing": "22:15 to 04:45", "duration": "6h 30m", "amt": 680} }
         self.choose_travel(options)
         

    def chennai_trichy(self):

        print('''Bus details, Time and Duration, Payment:
                1. LION Travels (21:50 to 04:35) 6h 45m - ₹600
                2. KPN Travels (22:00 to 05:00) 7h 00m - ₹650
                3. Parveen Travels (23:00 to 05:30) 6h 30m - ₹700
                4. SRM Travels (20:30 to 03:00) 6h 30m - ₹720
                5. YBM Travels (22:15 to 04:45) 6h 30m - ₹680 ''')

        options = {
    "LION Travels": {"id": "B1", "timing": "21:50 to 04:35", "duration": "6h 45m", "amt": 600},
    "KPN Travels": {"id": "B2", "timing": "22:00 to 05:00", "duration": "7h 00m", "amt": 650},
    "Parveen Travels": {"id": "B3", "timing": "23:00 to 05:30", "duration": "6h 30m", "amt": 700},
    "SRM Travels": {"id": "B4", "timing": "20:30 to 03:00", "duration": "6h 30m", "amt": 720},
    "YBM Travels": {"id": "B5", "timing": "22:15 to 04:45", "duration": "6h 30m", "amt": 680}}
        self.choose_travel(options)

        

    def chennai_madurai(self):

        print('''Bus details, Time and Duration, Payment:
1. Rathimeena Travels (21:30 to 04:00) 6h 30m - ₹550
2. SRS Travels (22:15 to 05:15) 7h 00m - ₹600
3. SRM Travels (20:45 to 03:30) 6h 45m - ₹580
4. KPN Travels (22:30 to 05:00) 6h 30m - ₹620
5. National Travels (23:00 to 05:30) 6h 30m - ₹700 ''')

        options = {
    "Rathimeena Travels": {"id": "C1", "timing": "21:30 to 04:00", "duration": "6h 30m", "amt": 550},
    "SRS Travels": {"id": "C2", "timing": "22:15 to 05:15", "duration": "7h 00m", "amt": 600},
    "SRM Travels": {"id": "C3", "timing": "20:45 to 03:30", "duration": "6h 45m", "amt": 580},
    "KPN Travels": {"id": "C4", "timing": "22:30 to 05:00", "duration": "6h 30m", "amt": 620},
    "National Travels": {"id": "C5", "timing": "23:00 to 05:30", "duration": "6h 30m", "amt": 700}}
        self.choose_travel(options)

        

    def coimbatore_trichy(self):

        print('''Bus details, Time and Duration, Payment:
1. Rathimeena Travels (21:30 to 04:00) 6h 30m - ₹550
2. Mariya Tours (21:45 to 04:15) 4h 30m - ₹600
3. Universal Travels (22:00 to 05:30) 5h 30m - ₹650
4. Mayurra Travels (22:15 to 05:00) 6h 00m - ₹580
5. Air India Travels (22:30 to 05:00) 6h 00m - ₹700
''')

        options = {
    "Rathimeena Travels": {"id": "D1", "timing": "21:30 to 04:00", "duration": "6h 30m", "amt": 550},
    "Mariya Tours": {"id": "D2", "timing": "21:45 to 04:15", "duration": "4h 30m", "amt": 600},
    "Universal Travels": {"id": "D3", "timing": "22:00 to 05:30", "duration": "5h 30m", "amt": 650},
    "Mayurra Travels": {"id": "D4", "timing": "22:15 to 05:00", "duration": "6h 00m", "amt": 580},
    "Air India Travels": {"id": "D5", "timing": "22:30 to 05:00", "duration": "6h 00m", "amt": 700}}
        self.choose_travel(options)
        
    def coimbatore_madurai(self):
        print('''Bus details, Time and Duration, Payment:
1. Rathimeena Travels (21:30 to 04:00) 6h 30m - ₹550
2. SRS Travels (22:15 to 05:15) 7h 00m - ₹600
3. SRM Travels (20:45 to 03:30) 6h 45m - ₹580
4. KPN Travels (22:30 to 05:00) 6h 30m - ₹620
5. National Travels (23:00 to 05:30) 6h 30m - ₹700
''')

        options = {
    "Rathimeena Travels": {"id": "E1", "timing": "21:30 to 04:00", "duration": "6h 30m", "amt": 550},
    "SRS Travels": {"id": "E2", "timing": "22:15 to 05:15", "duration": "7h 00m", "amt": 600},
    "SRM Travels": {"id": "E3", "timing": "20:45 to 03:30", "duration": "6h 45m", "amt": 580},
    "KPN Travels": {"id": "E4", "timing": "22:30 to 05:00", "duration": "6h 30m", "amt": 620},
    "National Travels": {"id": "E5", "timing": "23:00 to 05:30", "duration": "6h 30m", "amt": 700}}
        self.choose_travel(options)

       
    def trichy_madurai(self):
        print('''Bus details, Time and Duration, Payment:
1. KPN Travels (22:15 to 05:00) 6h 45m - ₹600
2. Mariya Tours (22:00 to 04:30) 6h 30m - ₹650
3. Parveen Travels (21:45 to 04:15) 6h 30m - ₹670
4. Vijay Tours (23:00 to 05:30) 6h 30m - ₹680
5. TAT Travels (21:15 to 04:00) 6h 45m - ₹590
''')

        options = {
    "KPN Travels": {"id": "F1", "timing": "22:15 to 05:00", "duration": "6h 45m", "amt": 600},
    "Mariya Tours": {"id": "F2", "timing": "22:00 to 04:30", "duration": "6h 30m", "amt": 650},
    "Parveen Travels": {"id": "F3", "timing": "21:45 to 04:15", "duration": "6h 30m", "amt": 670},
    "Vijay Tours": {"id": "F4", "timing": "23:00 to 05:30", "duration": "6h 30m", "amt": 680},
    "TAT Travels": {"id": "F5", "timing": "21:15 to 04:00", "duration": "6h 45m", "amt": 590}}
        self.choose_travel(options)

        
        

        



        
        

        



    
          

             

        







        
 
         


         
     
             
         
