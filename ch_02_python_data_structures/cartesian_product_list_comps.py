
colors = ['green', 'red']
sizes = ['XS', 'S', 'M', 'L', 'XL']

tshirts = [(color, size) for color in colors for size in sizes]
print('Colors avaiable: {}'.format(colors))
print('Sizes available: {}'.format(sizes))
print('Possible t-shirts: {}'.format(tshirts))

