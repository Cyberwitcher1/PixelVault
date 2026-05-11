import json

def to_json():

        post = {
            'title': 'An interesting title',
            'user_id': 22,
            'content': 'This is a string of content'
        }

        with open('file.json', 'w') as file:
            json.dump(post, file, indent=4)

to_json()
