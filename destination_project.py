import random
from tkinter import N
destinations = ['Paris','New York','Oahu','Los Angeles','Jamaica']
paris_restaurants = ['linguinis','ratatouilles','Le Frenchie']
restaurants = ['McDonalds','Chic-Fil-A','Steak house','Italian']
mode_of_transportation = ['Rental Car','Train','Bus','Trolley']
entertainments = ['Go on a City tour','Go to the bar','Go see local sports','Go to a Festival']
y = 'Ok great, lets move on to the next step.'
def destination_selector():
    # destination = random.choice(destinations)
    # destination_response = input(f'Your destination for this trip is {destination}. Is that OK? y/n ')
    
    # if destination_response == 'y':
    #     print('Ok Great, Lets move on')
    #     return destination
    # else:
    #     while destination_response == 'n': 
    #         destinations.remove(destination)
    #         destination = random.choice(destinations)
    #         destination_response = input(f'Your destination for this trip is now {destination}. Is that OK? y/n ') 
    #     print(y)    
    #     return destination
    destination_response = 'n'
    while destination_response == 'n':
        destination = random.choice(destinations)
        destination_response = input(f'Your destination for this trip is now {destination}. Is that OK? y/n ')
        if destination_response == 'n':
            destinations.remove(destination)

    print(y)
    return destination        




             


def restaurant_selector():
    # restaurant = random.choice(restaurants)
    # restaurant_response = input(f'Do you want to eat at {restaurant}? y/n ')
    
    # if restaurant_response == 'y':
    #     print(y)
    #     return restaurant
    # else:
    #     while restaurant_response == 'n':
    #         restaurants.remove(restaurant)
    #         restaurant = random.choice(restaurants)
    #         restaurant_response = input(f'Do you want to eat at {restaurant}? y/n ')
    #     return restaurant
    #     print(y)
    destination = saved_dest_choice
    restaurant_response = 'n'
    while restaurant_response == 'n': 
        if destination == 'Paris' and restaurant_response == 'n':
            restaurant = random.choice(paris_restaurants)
            restaurant_response = input(f'Do you want to eat at {restaurant}? y/n ')
            if restaurant_response == 'n':
                paris_restaurants.remove(restaurant) 
        else:             
            restaurant = random.choice(restaurants)
            restaurant_response = input(f'Do you want to eat at {restaurant}? y/n ') 
            if restaurant_response == 'n':
                restaurants.remove(restaurant)   
    print(y)
    return restaurant

        








def mode_of_transportation_selector():
    # transportation = random.choice(mode_of_transportation)
    # transportation_response = input(f'Is using a {transportation} for transportation OK? y/n ')
#    if transportation_response == 'y':
#        return transportation
#    else:
#        while transportation_response == 'n':
#            mode_of_transportation.remove(transportation)
#            transportation = random.choice(mode_of_transportation)
#            transportation_response = input(f'Is using a {transportation} for transportation OK? y/n ')
#        return transportation

    transportation_response = 'n'
    while transportation_response == 'n':
        transportation = random.choice(mode_of_transportation)
        transportation_response = input(f'Is using a {transportation} for transportation OK? y/n ')
        if transportation_response == 'n':
            mode_of_transportation.remove(transportation)
    print(y)        
    return transportation

def entertainment_selector():
    # entertainment = random.choice(entertainments)
    # entertainment_response = input(f'would you like to {entertainment} while on vacation? y/n ')
    # if entertainment_response == 'y':
    #     return entertainment
    # else:
    #     while entertainment_response == 'n':
    #         entertainments.remove(entertainment)
    #         entertainment = random.choice(entertainments)
    #         entertainment_response = input(f'would you like to {entertainment} while on vacation? y/n ')    
    #     return entertainment

#changed function to a more simplified version with less steps
    entertainment_response = 'n'
    while entertainment_response == 'n':
        entertainment = random.choice(entertainments)
        entertainment_response = input(f'would you like to {entertainment} while on vacation? y/n ')
        if entertainment_response == 'n':
            entertainments.remove(entertainment)
    print(y)
    return entertainment



def final_results(ent, mod, rest, dest):
    print(f'Your random trip is now set up, you will be in {dest} using a {mod} for transportation. You will be eating at {rest} and will be able to {ent} for fun while your here! Have a great vacation!')
    

saved_dest_choice = destination_selector()
saved_mod_choide = mode_of_transportation_selector() 
saved_ent_choice = entertainment_selector()
saved_rest_choice = restaurant_selector()
final_results(saved_ent_choice, saved_mod_choide, saved_rest_choice, saved_dest_choice)






