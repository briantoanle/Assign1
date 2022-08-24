def getUserInput():
    list = []
    looping = True
    while looping:
        list.append(input("Enter names, one on each line. Type DONE to quit entering names. "))
        if 'DONE' in list:
            looping = False
            del list[-1]

    for i in range(len(list)):
        list[i] = list[i].lower()
    return list


def soundexS3(name):

    temp_name = ""
    for char in name:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'y' or char == 'h' or char == 'w':
            temp_name += "0"
        elif char == 'b' or char == 'f' or char == 'p' or char == 'v':
            temp_name += '1'
        elif char == 'c' or char == 'g' or char == 'j' or char == 'k' or char == 'q' or char == 's' or char == 'x' or char == 'z':
            temp_name += '2'
        elif char == 'd' or char == 't':
            temp_name += '3'
        elif char == 'l':
            temp_name += '4'
        elif char == 'm' or char == 'n':
            temp_name += '5'
        else:
            temp_name +=6
    print(name)
    print(temp_name)
    return temp_name


def soundexS4(name):
    name1 = soundexS3(name)
    name2 = ""
    for i, char in enumerate(name1):
        if i == 0:
            name2 += char
        if i > 0:
            print("next character", name1[i], "previous character", name1[i-1])
            if name1[i] != name1[i-1]:
                name2 += char
        # print("temp name2 =", name2)

    print("result here =", name2)


def main():
    #print(getUserInput())
    soundexS4("schmidt")



main()