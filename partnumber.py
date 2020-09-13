def partnumber(number):

    dicUnites = {
                        "0": "",
                        "1" : "un",
                        "2" : "deux",
                        "3" : "trois",
                        "4" : "quatre",
                        "5" : "cinq",
                        "6" : "six",
                        "7" : "sept",
                        "8" : "huit",
                        "9" : "neuf",
                        }

    dicDizaines = {
        "0": "",
        "1": "dix",
        "2": "vingt",
        "3": "trente",
        "4": "quarante",
        "5": "cinquante",
        "6": "soixante",
        "7": "soixante-dix",
        "8": "quatre-vingts",
        "9": "huquatre-vingt-dix",

    }


    dicCentaines = {
        "1": "cent",
        "2": "deux cents",
        "3": "trois cents",
        "4": "quatre cents",
        "5": "cinq cents",
        "6": "six cents",
        "7": "sept cents",
        "8": "huit cents",
        "9": "neuf cents",
        "0": "",
    }



    dicOnzeSeize = {

        "11": "onze",
        "12": "douze",
        "13": "treize",
        "14": "quatorze",
        "15": "quinze",
        "16": "seize",
        "71": "soixante et onze",
        "72": "soixante et douze",
        "73": "soixante et treize",
        "74": "soixante et quatorze",
        "75": "soixante et quinze",
        "76": "soixante et seize",
        "91": "quatre-vingt-onze",
        "92": "quatre-vingt-douze",
        "93": "quatre-vingt-treize",
        "94": "quatre-vingt-quatorze",
        "95": "quatre-vingt-quinze",
        "96": "quatre-vingt-seize",
        "0": "",

    }


    partlettre = ""
    if number in dicOnzeSeize:
        partlettre = dicOnzeSeize.get(number, "")

    elif int(number) >= 0 and int(number) < 10:
        partlettre = dicUnites.get(str(int(number)), "")

    elif int(number) >= 10 and int(number) < 100:
        number = str(int(number))
        partlettre = dicDizaines.get(number[0], "") + "-" + dicUnites.get(number[1], "")

    elif int(number) >= 100 and int(number) < 999:
        if number[1] + number[2] in dicOnzeSeize:
            partlettre = dicCentaines.get(number[0], "") + "-" + dicOnzeSeize.get(number[1] + number[2], "")
        else:
            partlettre = dicCentaines.get(number[0], "") + "-" + dicDizaines.get(number[1], "") + "-" + dicUnites.get(
                number[2], "")
    return partlettre