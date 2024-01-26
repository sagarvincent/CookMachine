# import libraries
import requests
import subprocess
import time



# define a api class
class db_api():

    # define constructors
    def __init__(self,api_url):
        self.api_url = api_url

        # define cmd script to run the api application
        api_script = r"api_launch.txt"
        self.api_process = subprocess.Popen(api_script, shell=True)
        time.sleep(5)
        

    # function to pass database info to api
    def db_connect(self,db_info):

        # create a db configuration dict
        db_config = {
            'host' : db_info['host'],
            'port' : db_info['port'],
            'user' : db_info['user'],
            'password' : db_info['password'],
            'database' : db_info['database']
        }
        endpoint_url = f"{self.api_url}/db_config"
        try:
            requests.post(endpoint_url,json = db_config)
        except:
            print("API not running")
        endpoint_url2 = f"{self.api_url}/get_data"
        response = requests.get(endpoint_url2)
        print(response.json())
        
        























