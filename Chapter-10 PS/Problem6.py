from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo
    def book_a_ticket(slf, fro, to):
        print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to}")

    def get_status(slf):
        print(f"Train no: {slf.trainNo} is running on time.")

    def get_fare(slf, fro, to):
        print(f"Ticket fare in train no: {slf.trainNo} from {fro} to {to} is {randint(100,500)}")

a = Train(1213)
a.book_a_ticket( "Delhi", "Agra")
a.get_status()
a.get_fare( "Delhi", "Agra")