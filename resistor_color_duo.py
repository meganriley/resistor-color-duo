color_codes = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}
def value(colors):
    color_one = str(color_codes[colors[0]])
    color_two = str(color_codes[colors[1]])
    return int(color_one + color_two)
    #return combined_colors