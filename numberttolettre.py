from partnumber import partnumber

def numbertolettre(fullnumber):






    lettre = ""

    if int(fullnumber) < 1000:
        lettre=partnumber(fullnumber)

    elif int(fullnumber) >=1000 and int(fullnumber) < 10000:
        if fullnumber[0] == "1":
            lettre = "Mille " + partnumber(fullnumber[1] + fullnumber[2] + fullnumber[3])
        else:
            lettre = partnumber( fullnumber[0]) + " mille " + partnumber( fullnumber[1]+fullnumber[2]+fullnumber[3])

    elif int(fullnumber) >= 10000 and int(fullnumber) < 100000:
        lettre = partnumber(fullnumber[0]+fullnumber[1]) + " mille " + partnumber(fullnumber[2]+fullnumber[3]+fullnumber[4])

    elif int(fullnumber) >= 100000 and int(fullnumber) < 1000000:
        lettre = partnumber(fullnumber[0]+fullnumber[1]+fullnumber[2]) + " mille " + partnumber(fullnumber[3] + fullnumber[4] + fullnumber[5])

    elif int(fullnumber) >= 1000000 and int(fullnumber) < 10000000:
        if fullnumber[1] == "0" and fullnumber[2] == "0" and fullnumber[3] == "1":
            lettre = partnumber(fullnumber[0])+" million-mille " + partnumber(fullnumber[4] + fullnumber[5] + fullnumber[6])
        else:
            lettre = partnumber(fullnumber[0]) +" million " + partnumber(fullnumber[1]+fullnumber[2]+fullnumber[3]) + " mille " + partnumber(fullnumber[4] + fullnumber[5] + fullnumber[6])

    elif int(fullnumber) >=10000000 and int(fullnumber) < 100000000:
        if fullnumber[2] == "0" and fullnumber[3] == "0" and fullnumber[4] == "1":
            lettre = partnumber(fullnumber[0] + fullnumber[1])+" million mille " + partnumber(fullnumber[5] + fullnumber[6] + fullnumber[7])
        else:
            lettre = partnumber(fullnumber[0] + fullnumber[1])+" million " + partnumber(fullnumber[2]+fullnumber[3]+fullnumber[4]) + " mille " + partnumber(fullnumber[5] + fullnumber[6] + fullnumber[7])

    elif int(fullnumber) >=100000000 and int(fullnumber) < 1000000000:
        if fullnumber[3] == "0" and fullnumber[4] == "0" and fullnumber[5] == "1":
            lettre = partnumber(fullnumber[0] + fullnumber[1] + fullnumber[2])+" million Mille " + partnumber(fullnumber[6] + fullnumber[7] + fullnumber[8])
        else:
            lettre = partnumber(fullnumber[0] + fullnumber[1]+ fullnumber[2])+" million " + partnumber(fullnumber[3]+fullnumber[4]+fullnumber[5]) + " mille " + partnumber(fullnumber[6] + fullnumber[7] + fullnumber[8])

    elif int(fullnumber) >=1000000000 and int(fullnumber) < 10000000000:
        if fullnumber[4] == "0" and fullnumber[5] == "0" and fullnumber[6] == "1":
            lettre = partnumber(fullnumber[0]) +" milliard  " + partnumber(fullnumber[1] + fullnumber[2] + fullnumber[3])+" million Mille " + partnumber(fullnumber[7] + fullnumber[8] + fullnumber[9])
        else:
            lettre = partnumber(fullnumber[0]) +" milliard  " + partnumber(fullnumber[1] + fullnumber[2]+ fullnumber[3])+" million " + partnumber(fullnumber[4]+fullnumber[5]+fullnumber[6]) + " mille " + partnumber(fullnumber[7] + fullnumber[8] + fullnumber[9])

    elif int(fullnumber) >= 10000000000 and int(fullnumber) < 100000000000:
        if fullnumber[5] == "0" and fullnumber[6] == "0" and fullnumber[7] == "1":
            lettre = partnumber(fullnumber[0] + fullnumber[1]) +" milliards  " + partnumber(fullnumber[2] + fullnumber[3] + fullnumber[4]) +" million-Mille " + partnumber(fullnumber[8] + fullnumber[9] + fullnumber[10])
        else:
            lettre = partnumber(fullnumber[0] + fullnumber[1]) +" milliards  " + partnumber(fullnumber[2] + fullnumber[3] + fullnumber[4])+" million " + partnumber(fullnumber[5] + fullnumber[6] + fullnumber[7]) + " mille " + partnumber(fullnumber[8] + fullnumber[9] + fullnumber[10])

    elif int(fullnumber) >=100000000000 and int(fullnumber) < 1000000000000:
        if fullnumber[6] == "0" and fullnumber[7] == "0" and fullnumber[8] == "1":
            lettre = partnumber(fullnumber[0] + fullnumber[1]+ fullnumber[2]) +" milliards " + partnumber(fullnumber[3] + fullnumber[4] + fullnumber[5])+" million Mille " + partnumber(fullnumber[9] + fullnumber[10] + fullnumber[11])
        else:
            lettre = partnumber(fullnumber[0] + fullnumber[1]+ fullnumber[2]) +" milliards  " + partnumber(fullnumber[3] + fullnumber[4]+ fullnumber[5])+" million " + partnumber(fullnumber[6]+fullnumber[7]+fullnumber[8]) + " mille " + partnumber(fullnumber[9] + fullnumber[10] + fullnumber[11])



    return lettre