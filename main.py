print('   Welcome to the Ice Cream Shop!   ')
print('----------------MENU----------------')
print(' Size   | Chocolate |   Strawberry  ')
print(' Small  |  $ 8,00   |    $ 10,00    ')
print(' Medium |  $ 10,00  |    $ 12,00    ')
print(' Large  |  $ 12,00  |    $ 14,00    ')

total = 0
orders = []
while True:
    flavor = input('What flavor ice cream? (C/S): ').upper()
    if (flavor != 'C') and (flavor != 'S'):
        print('Invalid flavor')
        continue
    size = input('What size ice cream? (S/M/L): ').upper()
    if (size != 'S') and (size != 'M') and (size != 'L'):
        print('Invalid size')
        continue

    flavors = {'C': 'Chocolate', 'S': 'Strawberry'}
    sizes = {'S': 'Small', 'M': 'Medium', 'L': 'Large'}
    prices = {'C': {'S': 8, 'M': 10, 'L': 12},
              'S': {'S': 10, 'M': 12, 'L': 14}}

    flavor_name = flavors[flavor]
    size_name = sizes[size]
    price = prices[flavor][size]
    print(f'You chose the {size_name} {flavor_name} Ice Cream')
    total += price
    orders.append(f'- {size_name} {flavor_name} = $ {price:.2f}')

    # if the user wants to request anything else
    add = input('Would you like another ice cream? (Y/N): ').upper()
    if add == 'Y':
        continue
    else:
        print('---------------Order Summary---------------')
        for item in orders:
            print(item)

        print('Total to pay: $ {:.2f}'.format(total))
        print('Thank you for visiting the Ice Cream Shop!')
        break