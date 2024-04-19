class star_cinema:
    def __init__(self) -> None:
        self.hall_list = []
    # hall_list=[]
class Hall(star_cinema):
    def __init__(self,seats,show_list,rows,cols,hall_no) -> None:
        self.seats=seats
        self.show_list=show_list
        self.rows=rows
        self.cols=cols
        self._hall_no=hall_no #use protected variable in hall no
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
        for i in range(self.rows+1):
            col = []
            for j in range(self.cols+1):
                 col.append(0)
            li.append(col)
        seatList[str(self.id)]=li
    
    # book seat by user

    def book_seats(self,id):
        self.id = id
        seat = self.hall_list[0][0]
        print("-----------------------------------------------")
        i = int(input("PLEASE, ENTER ROW NUMBER:- "))
        j = int(input("PLEASE, ENTER COLUM NUMBER:- "))
        if(i>self.rows or j>self.cols):
            print(f"SORRY ,INVALID SEAT NO PLEASE ENTER LESS THEN OR EQUAL {self.rows} and {self.cols}")
        elif(seat[id][i][j]==1):
            print("SORRY,THIS SEAT IS ALREADY BOOKED TYR ANOTHER")
        else:
            seat[id][i][j]=1
            print(f"SEAT ({i},{j}) BOOKED FOR SHOW ({self.id})")
        print("-----------------------------------------------")

    # view show list
    def movieList(self):
        mList = self.hall_list[0][1]
        for id,name,time in mList:
            print("MOVIE NAME:",name," ID:",id," TIME:",time)
    #  view available seats
    def view_available_seats(self,id):
        seatList = self.hall_list[0][0]
        for li in seatList[id]:
            print(li)


        



m = Hall(dict(),list(),4,10,2)
m.entry_hall()
m.enter_show(111,'HOROR MOVIE','11:00 AM 10/02/2024')
m.enter_show(115,'JOY BANGLA','2:30 PM 10/02/2024')
m.enter_show(117,'AMAR BONDU RASHED','6:30 PM 13/04/2024')

s = Hall(dict(),list(),30,35,3)
while(True):
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK SEATS")
    print("4. EXIT")

    x = int(input("ENTER OPTION:- "))
    if(x==4):
        break
    elif(x==1):
        print("-----------------------------------------------")
        m.movieList()
        print("-----------------------------------------------")
    elif(x==2):
        id = str(input("ENTER SHOW ID:- "))
        flg = False
        seatList = m.hall_list[0][0]
        for k,v in seatList.items():
            if(id==k):
                flg=True
        if(not flg):
            print("-----------------------------------------------")
            print("SORRY, WRONG ID")
            print("-----------------------------------------------")
        else:
            print("-----------------------------------------------")
            # call from class
            m.view_available_seats(id)
            print("-----------------------------------------------")

    elif(x==3):
        id = str(input("ENTER SHOW ID:- "))
        flg = False
        seatList = m.hall_list[0][0]
        for k,v in seatList.items():
            if(id==k):
                flg=True
        if(flg):
            m.book_seats(id)
        else:
            print("SORRY, WRONG ID")
    else:
        print("-----------------------------------------------")
        print("SORRY, WRONG OPTION")
        print("-----------------------------------------------")

    

