import pandas as pd


class data_handler():

    def __init__(self,path):

        self.dataset = pd.read_csv(path)

    def disp_info(self):

        self.dataset.info()

    # function to parse the ingredients of the recipe
    def parse_ingredients(self):

        self.ingredients = None
        

        return self.ingredients
    
    # function to parse the directions for cooking
    def parse_direction(self):

        self.direction = None


        return self.direction





































