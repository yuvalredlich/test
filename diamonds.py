"""
    Yuval Redlich
    Test
    25/12/2024
"""

def read_diamonds_data():
    diamonds_file = open(rf"C:\Users\User\OneDrive\Desktop\YuvalCourse\test\diamonds.csv", 'r')
    diamonds_data = diamonds_file.readlines()
    return diamonds_data


def expensive_diamond(data):
    """
    columns[6] is the price.
    """
    highest = 0
    for line in data[1:]:
        columns = line.split(",")
        if columns[6].isdigit():
            if int(columns[6]) > highest:
                highest = int(columns[6])
    return highest


def avg_price(data):
    total = 0
    count = 0
    avg = 0
    for line in data[1:]:
        columns = line.split(",")
        if columns[6].isdigit():
            count += 1
            total += int(columns[6])
    avg = total / count
    return avg


def ideal_diamonds(data):
    """
    columns[1] is cut.
    """
    count = 0
    for line in data[1:]:
        columns = line.split(",")
        if columns[1] == "Ideal":
            count += 1
    return count


def all_colors(data):
    count = 0
    colors = []
    for line in data[1:]:
        columns = line.split(",")
        if columns[2] not in colors:
            count += 1
            colors.append(columns[2])
    return count, colors


def half_carat_premium(data):
    carat = []
    for line in data[1:]:
        columns = line.split(",")
        if columns[1] == "Premium":
            carat.append(columns[0])
    list_len = len(carat)
    half_carat = carat[(list_len//2)]
    return half_carat


def cuts_carat_avg(data):
    cuts = {}
    average_for_cuts = {}

    # get all the kinds of cuts
    for line in data[1:]:
        columns = line.split(",")
        if columns[1] not in cuts:
            cuts[columns[1]] = 0
        else:
            cuts[columns[1]] += 1

    # create new keys in the average dictionary
    for cut in cuts:
        average_for_cuts[cut] = 0

    # sum all the carats for each cut
    for line in data[1:]:
        columns = line.split(",")
        cut = columns[1]
        carat = float(columns[0])
        average_for_cuts[cut] += carat

    # average of all the sums
    for avg in average_for_cuts:
        average_for_cuts[avg] /= cuts[avg]
    return average_for_cuts


def colors_price_avg(data):
    colors = {}
    average_for_colors = {}

    # get all the kinds of colors
    for line in data[1:]:
        columns = line.split(",")
        if columns[2] not in colors:
            colors[columns[2]] = 0
        else:
            colors[columns[2]] += 1

    # create new keys in the average dictionary
    for color in colors:
        average_for_colors[color] = 0

    # sum all the prices for each color
    for line in data[1:]:
        columns = line.split(",")
        color = columns[2]
        price = float(columns[0])
        average_for_colors[color] += price

    # average of all the sums
    for avg in average_for_colors:
        average_for_colors[avg] /= colors[avg]
    return average_for_colors


def main():
    """
    columns:
    carat,cut,color,clarity,depth,table,price,x,y,z
    """
    diamonds_data = read_diamonds_data()

    # the most expensive diamond
    highest = expensive_diamond(diamonds_data)
    print("The most expensive diamond costs {0}".format(highest))

    # the average price of the diamonds
    average_price = avg_price(diamonds_data)
    print("The average price is {0}".format(average_price))

    # the number of diamonds with ideal cut
    ideal_cut = ideal_diamonds(diamonds_data)
    print("The number of diamonds with ideal cut is {0}".format(ideal_cut))

    # how many different colors? what are they?
    count, colors = all_colors(diamonds_data)
    print("There are {0} different colors. The colors of the diamonds are {1}".format(count, colors))

    # the half carat of premium diamonds
    half_carat = half_carat_premium(diamonds_data)
    print("The half carat of premium diamonds is {0}".format(half_carat))

    # average carat for each cut
    avg_carats = cuts_carat_avg(diamonds_data)
    print("The average carat for each cut is {0}".format(avg_carats))

    # average price for each color
    avg_price_colors = colors_price_avg(diamonds_data)
    print("The average price for each color is {0}".format(avg_price_colors))



if __name__ == "__main__":
    main()
