class star_cinema:
    hall_list=[]
class Hall(star_cinema):
    def __init__(self,seats,show_list,rows,cols,hall_no) -> None:
        self.seats=seats
        self.show_list=show_list
        self.rows=rows
        self.cols=cols
        self._hall_no=hall_no
        super().__init__()
    def entry_hall(self):
        self.hall_list.append([self.seats,self.show_list,self.rows,self.cols,self._hall_no])
    # show list
    def enter_show(self,id,movie_name,time):
        self.id=id
        self.movie_name=movie_name
        self.time=time
        self.hall_list[0][1].append((self.id,self.movie_name,self.time))

        seatList = self.hall_list[0][0]
        li = []
        for i in range(5):
            col = []
            for j in range(10):
                 col.append(0)
            li.append(col)
        seatList[str(self.id)]=li
    
    # book seat by user

    def book_seats(self,id):
        self.id = id
        seat = self.hall_list[0][0]
        print("-----------------------------------------------")
        i = int(input("Please, Enter Colum Number:- "))
        j = int(input("Please, Enter Row Number:- "))
        if(i>=self.rows or j>=self.cols):
            print(f"Sorry, Invalid seat NO please enter less than {self.rows} and {self.cols}")
        elif(seat[id][i][j]==1):
            print("Sorry, This seat is already booked try another")
        else:
            seat[id][i][j]=1
        print("-----------------------------------------------")



m = Hall(dict(),list(),4,10,2)
m.entry_hall()
m.enter_show(10,'Hello','11:00 AM 10/02/2024')
m.enter_show(12,'Hello','11:00 AM 10/02/2024')

s = Hall(dict(),list(),30,35,3)
while(True):
    print("1. View all show today")
    print("2. View available seats")
    print("3. Book seats")
    print("4. Exit")

    x = int(input("Enter Option:- "))
    if(x==4):
        break
    elif(x==1):
        print("-----------------------------------------------")
        showList = m.hall_list[0][1]
        for id,movie_name,time in showList:
            print("Movie Name: ",movie_name," Show ID: ",id," Time: ",time)
        print("-----------------------------------------------")
    elif(x==2):
        id = str(input("Enter show ID:- "))
        flg = False
        seatList = m.hall_list[0][0]
        for k,v in seatList.items():
            if(id==k):
                flg=True
        if(not flg):
            print("-----------------------------------------------")
            print("Sorry, Wrong ID")
            print("-----------------------------------------------")
        else:
            print("-----------------------------------------------")
            for li in seatList[id]:
                print(li)
            print("-----------------------------------------------")
    elif(x==3):
        id = str(input("Enter show ID:- "))
        flg = False
        seatList = m.hall_list[0][0]
        for k,v in seatList.items():
            if(id==k):
                flg=True
        if(flg):
            m.book_seats(id)
        else:
            print("Sorry, Wrong ID")

    

