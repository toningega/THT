import sys
sys.path.append('./')

import unittest
from main import venue_picker
import json


with open(r"tests\users.json") as users_data:
    test_users = json.loads(users_data.read())
    # print(users)

with open(r"tests\venues.json") as venue_data:
    test_venues = json.loads(venue_data.read())
    # print(venues)


# Clean the venue data 
for venue in test_venues:
    venue['food'] = [x.lower() for x in venue['food']]
    venue['drinks'] = [x.lower() for x in venue['drinks']]

# Clean the user data
for user in test_users:
    user['wont_eat'] = [x.lower() for x in user['wont_eat']]
    user['drinks'] = [x.lower() for x in user['drinks']]



class MyTestCase(unittest.TestCase):

    def test_eats_everything(self):
        response = venue_picker(["eats_everything person"],test_venues,test_users)
        # print(len(test_venues))
        assert response['places_to_avoid'] == list()
        assert len(response['places_to_visit']) == len(test_venues)

    def test_picky_eater(self):
        response = venue_picker(["picky eater"],test_venues,test_users)
        assert response['places_to_visit'] == list() 
        assert response['places_to_avoid'][0]['reason'][0] == 'There is nothing for picky to eat'

    def test_picky_drinker(self):
        response = venue_picker(["picky drinker"],test_venues,test_users)
        print( response)
        assert response['places_to_visit'] == list()     
        assert response['places_to_avoid'][0]['reason'][0] == 'There is nothing for picky to drink'      




if __name__ == '__main__':
    unittest.main()