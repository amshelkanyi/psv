'''create a psv sacco for the matatu industry and private cars
    from route of ngong to nairobi
'''
class psv(object):
    def __init__(self, no_of_seats, regno):
        self.no_of_seats = no_of_seats
        self.regno = regno

    def ntsa_fee(self, amount):
        self.amount = 200

    def returns(self, fare):
        self.fare = 100
class matatu(psv):
    def __init__(self):
        self.no_of_seats = 14
        self.income = 0
    def ntsa_fee(self, amount):
        amount = self.amount*self.no_of_seats
        return amount
    def returns(self, fare):
        income = self.fare*self.no_of_seats
        return income

class taxi(psv):
    def __init__(self):
        self.no_of_seats = 4
        self.income = 0
        self.raining = False
    def ntsa_fee(self, amount):
        amount = self.amount*self.no_of_seats
        return amount
    def returns(self, fare):
        if self.raining:
            income = self.fare*self.no_of_seats
            return income
        else:
            return (self.fare*self.no_of_seats)+400

