


class MyLuckyNumbers:

    def __init__(self, list=None):
        self.lucky_numbers = list

def show_lucky_numbers(lucky_numbers_obj: MyLuckyNumbers):
    
    for number in lucky_numbers_obj.lucky_numbers:
        print(number)