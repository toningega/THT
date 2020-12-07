
# Python Question: 

# Venue Picker

This app is made by Tonin Gega for a Time out interview process


## Function venue_picker()

Input params:

    Args:
        user_list (list): List of user names (Case Sensitive) of people who want to come out to the event
        venue_json ([dict]): from file venue.json containing name (str), food (list), drinks (list)
        user_json ([dict]): from users.json containings name (str), wont_eat (list), drinks (list)

This function will assess each venue and see if it is compatible with the user list and their food and drink requirements. 

The function returns a dict response with the places_to_visit (list) and places_to_avoid (list)

e.g:
{
   "places_to_visit":[
      "Spice of life",
      "The Cambridge"
   ],
   "places_to_avoid":[
      {
         "name":"El Cantina",
         "reason":[
            "There is nothing for Rosie to eat",
            "There is nothing for Karol to drink"
         ]
      },
      {
         "name":"Twin Dynasty",
         "reason":[
            "There is nothing for Wen to eat"
         ]
      }
   ]
}



## Unittests

Unit tests have been written in the 'tests' folder under test_main.py.
It contains it's own data files user.json and venues.json

```
 Areas for improvement:
- Allow input for users to be case insensitive
- Validate input of function
- Handle edge cases like no places to visit
- Build as an API in flask or similar
- expand on tests
```

# SQL question

## Answer:

The answer to the SQL question is total revenue value: 4390

You can find the SQL for this in folder SQL_Question > revenue_value.sql