import api_connector
import os
import json


def test(path):
    print("Test running")

    # load the database info file
    with open(path, 'r') as file:
        data = json.load(file) 

    # recipe data base
    db_config = data['recipe_db']
    

    # pass in the api url 
    db_api = api_connector.db_api('http://127.0.0.1:8001')
    db_api.db_connect(db_config)

    print("Test finished")




if __name__ == '__main__':

    cwd = os.getcwd()
    path = os.path.join(cwd,'db_info.json')

    test(path) 







