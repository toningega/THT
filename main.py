import json
from collections import OrderedDict
import pprint as pp


def venue_picker(user_list: list, venue_json, user_json):
    """Returns viable venue options for team outings based on user preferences on food and drink

    Args:
        user_list (list): List of user names (Case Sensitive) to consider for the outing
        venue_json ([dict]): from venue.json
        user_json ([dict]): from users.json

    Returns:
        [dict]: 
            places_to_visit: a list of places which are available to visit based on the users entered
            places_to_avoid: a list of dicts with the venue name to avoid and reason for avoiding it
    """ 
    venues = venue_json
    users = user_json
    users = [x for x in users if x['name'] in user_list]

    # loop through venues and update attributes on each venue for each person, if they can or can't eat/drink
    for venue in venues:
        suitable = []
        not_suitable_for_food = []
        not_suitable_for_drink = []
        for user in users:
            if len(set(venue['food']).difference(set(user['wont_eat']))) != 0: # take the set difference of the venues food and users won't_eat
                # print(set(venue['drinks']).intersection(set(user['drinks'])))
                if len(set(venue['drinks']).intersection(set(user['drinks']))) != 0: # take the set intersection of the venue drink offerings and user drink preferences
                    # if there's food available after the set difference and drinks available then this venue is okay for this user
                    suitable.append(user['name'])
                else:
                    # if there's food available but no drink this venue is not suitable as there is no drink
                    not_suitable_for_drink.append(user['name'])
            else: # no food or drinks
                not_suitable_for_food.append(user['name'])
        # These attributes will help with later logic, assign them for each venue
        venue['suitable'] = suitable
        venue['not_suitable_for_food'] = not_suitable_for_food
        venue['not_suitable_for_drink'] = not_suitable_for_drink

    # Begin constructing our response object
    response = {}

    # for each venue if both food and drink are empty then option is available to team memebers
    # construct list of available options
    places_to_visit = [venue['name'] for venue in venues if len(venue['not_suitable_for_food']) == 0 and len(venue['not_suitable_for_drink']) == 0]

    # for each venue if no food is available or no drinks are available then option is not available to team members
    # construct a list of dicts with reason for options not being available 
    places_to_avoid = []
    for venue in venues:
        if len(venue['not_suitable_for_food']) == 0 and len(venue['not_suitable_for_drink']) == 0:
            continue
        else:
            avoid_dict = {}
            reason = []
            if len(venue['not_suitable_for_food']) != 0 or len(venue['not_suitable_for_drink']) != 0:
                avoid_dict['name'] = venue['name']
                avoid_dict['reason'] = [f'There is nothing for {person.split()[0]} to eat' for person in venue['not_suitable_for_food']] + [f'There is nothing for {person.split()[0]} to drink' for person in venue['not_suitable_for_drink']]
            places_to_avoid.append(avoid_dict)

    response['places_to_visit'] = places_to_visit
    response['places_to_avoid'] = places_to_avoid

    return response


if __name__ == "__main__":
    with open("users.json") as users_data:
        users = json.loads(users_data.read())
        # print(users)

    with open("venues.json") as venue_data:
        venues = json.loads(venue_data.read())
        # print(venue)


    # Clean the venue data 
    for venue in venues:
        venue['food'] = [x.lower() for x in venue['food']]
        venue['drinks'] = [x.lower() for x in venue['drinks']]

    # Clean the user data
    for user in users:
        user['wont_eat'] = [x.lower() for x in user['wont_eat']]
        user['drinks'] = [x.lower() for x in user['drinks']]

    # ['Danielle Ren', 'Cristiana Lusitano', 'Karol Drewno', 'Gaston Chambray', 'Tom Mullen', 'Rosie Curran', 'Wen Li']
    resp = venue_picker(['Danielle Ren', 'Cristiana Lusitano', 'Karol Drewno', 'Gaston Chambray', 'Tom Mullen', 'Rosie Curran', 'Wen Li']
                        ,venues
                        ,users
                        )

    print(resp)