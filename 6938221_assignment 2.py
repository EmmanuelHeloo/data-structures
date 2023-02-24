'''
COMPUTER APPLICATIONS IN CIVIL ENGINEERING CE 257
    Github Link: https://github.com/EmmanuelHeloo
    @author: Emmanuel Y. Heloo
'''
car_brand = {
    'Aston martin':'550,000',
    'Rimac':'330,795',
    'Ford':'100,000',
    'Corvette':'440,800',
    'Alfa Remeo':'420,300',
    'Mercedes-Benz':'570,450',
    'Nissan':'31,690',
    'Renault':'35,000',
    'Ferrari':'5,001,200',
    'Bugatti':'2,000,000'
}           
# prices of available car brands
car_name=input('Please enter a car brand: ')
# get user input for car brand
if car_name in car_brand:
    print('Yes, this brand is available.')
    print('The {0} car brand costs ${1}.'.format(car_name, car_brand[car_name]))
else:
    print('No, this brand is not available.')