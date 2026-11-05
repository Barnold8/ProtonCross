from selenium import webdriver
from typing import List

class Driver:

    def __init__(self):

        self.driver = None

        pass

    def load_config(self,path:str)-> None:
        
        
        pass

    def combine_arguments(self, args: dict)->str:

        arg_str = "/?"

        for key,value in args.items():
            arg_str += f"{key}={value}&"

        return arg_str[:-1]

    def getPage(self,url:str, query_params: dict)->None:

        if self.driver == None:
            print(f"SCRAPER - getPage | Error: self.driver was not initiated")
            exit(1)
        else:
            self.driver.get(f"{url}")

