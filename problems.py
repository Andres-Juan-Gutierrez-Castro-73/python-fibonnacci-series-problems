"""
PROBLEM 1:
CREATE A FIBONNACCI SERIE IN A N RANGE, SOMTHING LIKE THIS 0, 1, 1, 2, 3, 5 ...
"""

#CREATE THE FUNTION FIBONNACCI
def fibonnacci(number_range):
    #CREATE AN ARRAY WITH THE 2 INITAL VALUES
    serie = [0, 1]

    #CONFIRM THAT THE ARRAY HAVE ONLY 2 VALUES AND THE VALUES MIGTH TO BE CONSECUTE NUMBERS
    if (len(serie) == 2) and (serie[0] + 1 == serie[1]):
        #FOR LOOP
        for i in range(2, number_range):
            next_number = serie[i - 1] + serie[i - 2]
            #ADD THE NUMBER TO THE ARRAY
            serie.append(next_number)
    else:
        print("something went wrong, check out your array")

    #PRINT THE FIBONNACCI SERIE
    print(serie)

"""
PROBLEM 2
CREATE A FIBONNACCI SERIE THAT STARTS WITH THE ELEVEN NUMBER (11) AND CONTINUE THE SECUENCIE N TIMES
"""

#CREATE THE FUNTION FIBONNACCI2
def fibonnacci2(number_range, number_inital):
    #CREATE AN ARRAy
    serie = [number_inital, number_inital + 1]

    #CONFIRM THAT THE ARRAY HAVE ONLY 2 VALUES AND THE VALUES MIGTH TO BE CONSECUTE NUMBERS
    if (len(serie) == 2) and (serie[0] + 1 == serie[1]):
        #FOR LOOP
        for i in range(2, number_range):
            next_number = serie[i - 1] + serie[i - 2]
            #ADD THE NUMBER TO THE ARRAY
            serie.append(next_number)
    else:
        print("something went wrong, check out your array")

    #PRINT THE FIBONNACCI SERIE
    print(serie)


#IPLEMENTS THE TWO FUNCIONS
number_range = int(input('Write the amount of fibonnacci number you want: '))
fibonnacci(number_range)

number_range = int(input('Write the amount of fibonnacci number you want: '))
inital_number = int(input('Write the number inital of your new fibonnaci series: '))
fibonnacci2(number_range, inital_number)