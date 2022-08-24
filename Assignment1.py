def main():
    while True:
        offpeak = float(input("Enter kwh during Off Peak period: "))
        if offpeak <= 0:
            quit()
        onpeak = float(input("Enter kwh during On Peak period: "))
        midpeak = float(input("Enter kwh during Mid Peak period "))
        seniority = input("Is owner senior? (y,n): ")
        offkwh = 0.085
        onkwh = 0.176
        midkwh = 0.119

        totalkwh = onpeak+midpeak+offpeak

        #if total kwh < 400 4% discount
        totalDiscount = 0.96

        #not applicable if totaldiscount is applied
        peakDiscount = 0.95

        if seniority == 'y' or seniority == 'Y':
            seniorDiscount = .89
        elif seniority == 'n' or seniority == 'N':
            seniorDiscount = 1.00


        tax = 1.13

        offpeakcost = offpeak * offkwh
        onpeakcost = onpeak * onkwh
        midpeakcost = midpeak *midkwh
        costpretax = (offpeakcost + onpeakcost + midpeakcost)

        #print(round(costpretax,2))

        if totalkwh < 400:
            costpretax = costpretax * totalDiscount
        elif onpeak < 150:
            costpretax = offpeakcost + onpeakcost * peakDiscount + midpeakcost
            #onpeakcost = onpeakcost *.95




        cost = costpretax * 1.13 * seniorDiscount


        cost = round(cost,2)

        print("Electricity cost: $", cost)
        print()


main()
