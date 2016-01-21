
colors = ['green', 'red']
sizes = ['XS', 'S', 'M', 'L', 'XL']

for tshirt in ('%s %s' % (color, size) for color in colors for size in sizes):
    print(tshirt)
