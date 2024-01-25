# import libraries
import requests



# define a api class
class db_api():

    # define constructors
    def __init__(self,api_url):
        self.api_url = api_url

        pass

    # function to pass database info to api
    def db_connect(self,ip_add,port_no,db_name,db_user,db_pass):

        # create a db configuration dict
        db_config = {
            'host' : ip_add,
            'port' : port_no,
            'database' : db_name,
            'user' : db_user,
            'password' : db_pass
        }

        requests.post(self.api_url+'/db_config',db_config)
        























