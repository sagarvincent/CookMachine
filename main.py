import os
import data_handler


cwd = str(os.getcwd())
path = os.path.join(cwd+r'\data\dataset\llmdataset\recipe.csv')


# create data handler
data_handler = data_handler.data_handler(path)
data_handler.disp_info()
