from selenium import webdriver
from typing import List
import json

class Driver:

    def __init__(self,config_path:str):

        self.settings = self.load_config(config_path)
        self.driver   = self.assign_driver()

        pass

    def load_config(self,path:str)-> None:
        
        settings = None
        
        try:
            with open(path,"r") as file:
                settings = json.loads(file)
        except FileNotFoundError as FNFE:
            print(f"SCRAPER - load_config | Error: could not find file {path}")
            exit(1)

        return settings

    def assign_driver(self,driver_name: str)->:
        
        driver_name = driver_name.lower()

        match driver_name:

            case "chrome":
                self.driver = webdriver.Chrome()

            case "firefox":
                self.driver = webdriver.FireFox() 
            
            case "edge":
                self.driver = webdriver.Edge()

            case "ie":
                self.driver = webdriver.Ie()

            case "safari":
                self.driver = webdriver.Safari()

            case _:
                print(f"SCRAPER - assign_driver | Warning: Could not find web driver {driver_name}, assinging chrome instead")

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

