"""
This program is meant to use input information 
from the user about the opposing soccer teams rating,
and use that information to tell the user the best 
or most efficient layout of their strikers, 
attacking midfield, midfield, and defense for the game.
"""
def teamgamelayout(my_teams_layout): #defines the function
    for layout in range (0,5): #makes the loop
        striker_rating = int(input(f"What is the opposing team's strikers rating?: ")) #asks the user to input needed information about  the other teams strikers
        attacking_midfield_rating = int(input(f"What is the opposing team's attacking midfeild's rating?: ")) #asks the user to input needed information about  the other teams attacking midfield
        midfield_rating = int(input(f"What is the opposing team's midfeild's rating?: "))#asks the user to input needed information about  the other teams midfiled
        defense_rating = int(input(f"What is the opposing team's defense's rating?: "))#asks the user to input needed information about  the other teams defense
        opposing_teams_rating = [striker_rating, attacking_midfield_rating, midfield_rating, defense_rating] #puts all of the inputs into a list
        opposing_teams_rating.sort() #sorts the list from lowest to highest
        print(f"{opposing_teams_rating} = 1, 2, 3, 4")
        if striker_rating == opposing_teams_rating[0]: #makes some if statements to get the lists lined up with the messages so the lowest rated position recieves the least number of players
            message1 = (f"There should be 1 stiker on the field for yout team")
        elif attacking_midfield_rating == opposing_teams_rating[0]:
            message1 = (f"There should be 1 attacking midfield on the field for yout team")
        elif midfield_rating == opposing_teams_rating[0]:
            message1 = (f"There should be 1 midfield on the field for yout team")
        else:
            message1 = (f"There should be 1 defender on the field for yout team")
        
        if striker_rating == opposing_teams_rating[1]:
            message2 = (f"There should be 2 stikers on the field for yout team")
        elif attacking_midfield_rating == opposing_teams_rating[1]:
            message2 = (f"There should be 2 attacking midfield on the field for yout team")
        elif midfield_rating == opposing_teams_rating[1]:
            message2 = (f"There should be 2 midfield on the field for yout team")
        else:
            message2 = (f"There should be 2 defenders on the field for yout team")

        if striker_rating == opposing_teams_rating[2]:
            message3 = (f"There should be 3 stikers on the field for yout team")
        elif attacking_midfield_rating == opposing_teams_rating[2]:
            message3= (f"There should be 3 attacking midfield on the field for yout team")
        elif midfield_rating == opposing_teams_rating[2]:
            message3 = (f"There should be 3 midfield on the field for yout team")
        else:
            message3= (f"There should be 3 defenders on the field for yout team")
        
        if striker_rating == opposing_teams_rating[3]:
            message4 = (f"There should be 4 stikers on the field for yout team")
        elif attacking_midfield_rating == opposing_teams_rating[3]:
            message4= (f"There should be 4 attacking midfield on the field for yout team")
        elif midfield_rating == opposing_teams_rating[3]:
            message4 = (f"There should be 4 midfield on the field for yout team")
        else:
            message4= (f"There should be 4 defenders on the field for yout team")
        
        print(message1) #prints all of the messages in order
        print(message2)
        print(message3)
        print(message4)

teamgamelayout("opposing_teams_rating") #calls the function