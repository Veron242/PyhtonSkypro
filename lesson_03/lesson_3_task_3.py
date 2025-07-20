from address import Address
from mailing import Mailing

to_address=Address("123456", "Москва", "Ленина", "42", "15")
from_address=Address("654321", "Санкт-Петербург", "Невский", "24", "7")

mailing = Mailing (to_address, from_address, 350, 'RB123456789CN')

print(mailing)
