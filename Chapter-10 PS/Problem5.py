from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    def book_a_ticket(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def get_status(self):
        print(f"Train no: {self.trainNo} is running on time.")

    def get_fare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(100,500)}")

a = Train(1213)
a.book_a_ticket( "Delhi", "Agra")
a.get_status()
a.get_fare( "Delhi", "Agra")