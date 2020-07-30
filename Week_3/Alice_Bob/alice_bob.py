# GET INPUT FROM THE USER AND THE TURN IT INTO A LIST
alices_rating = list(input('Enter Alices rating'))
bobs_rating = list(input('Enter Bobs rating'))

# CREATE A FUNCTION THAT TAKES IN THE TWO RATINGS
def calulate_points(alice, bob) :
    # MAKE SURE THAT BOTH THEIR SCORES ARE 0 AT THE BEGINNING
    alices_score = 0
    bobs_score = 0

    for rating in range(3) :
        # NOW, WE LOOP THROUGH BOTH LISTS AND CHECK WHICH NUMBERS ARE BIGGER
        # IF ALICE'S RATING IS BIGGER, GIVE HER A POINT
        if (alice[rating] > bob[rating]) :
            alices_score = alices_score + 1
            print('Alice gets a point, her score is: ' + str(alices_score))

        # IF THEIR RATINGS ARE EQUAL, NO ONE GETS A POINT
        elif (alice[rating] == bob[rating]) :
            print('No one gets a point')

        # IF BOB'S RATING IS BIGGER, GIVE HIM A POINT
        elif (alice[rating] < bob[rating]) :
            bobs_score = bobs_score + 1
            print('Bob gets a point, his score is: ' + str(bobs_score))

    print('Alice: ' + str(alices_score) + ', Bob: ' + str(bobs_score))

calulate_points(alices_rating, bobs_rating)
