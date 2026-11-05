from selenium import webdriver
from typing import List
import json

class Driver:

    def __init__(self,config_path:str):

        self.settings = self.load_config(config_path)
        self.driver   = None
        self.assign_driver(self.settings)


    def load_config(self,path:str)-> None:
        
        settings = None
        
        try:
            with open(path,"r") as file:
                settings = json.load(file)
        except FileNotFoundError as FNFE:
            print(f"SCRAPER - load_config | Error: could not find file {path}")
            exit(1)

        return settings

    def assignOptions(self, settings:dict,options): # not even going to attempt to figure out the type hint for this one
        
        for argument in settings.get("arguments",[]):
            options.add_argument(argument)
        for key, value in settings.get("capabilities",{}).items():
            setattr(options,key,value)

        return options

    def assign_driver(self,options:dict)->None:

        driver_name = options["driver"].lower()

        match driver_name:

            case "chrome":
                self.driver = webdriver.Chrome(
                        self.assignOptions(self.settings,webdriver.ChromeOptions())
                        )

            case "firefox":
                self.driver = webdriver.Firefox(
                        self.assignOptions(self.settings,webdriver.FirefoxOptions())
) 
            
            case "edge":
                self.driver = webdriver.Edge(
                        self.assignOptions(self.settings,webdriver.EdgeOptions())
                        )

            case "ie":
                self.driver = webdriver.Ie(
                        self.assignOptions(self.settings,webdriver.IeOptions())
                )

            case "safari":
                self.driver = webdriver.Safari(
                        assignOptions(self.settings,webdriver.SafariOptions())
                        )

            case _:
                print(f"SCRAPER - assign_driver | Warning: Could not find web driver {driver_name}, assinging chrome instead")

    def combine_arguments(self, args: dict)->str: # turns out protondb doesnt use bloomin URL arguments

        arg_str = "/?"

        for key,value in args.items():
            arg_str += f"{key}={value}&"

        return arg_str[:-1]

    def getPage(self,url:str, query_params: dict = None)->None:

        if self.driver == None:
            print(f"SCRAPER - getPage | Error: self.driver was not initiated")
            exit(1)
        else:

            request_url = url
            if query_params != None:
                url += self.combine_arguments(query_params)
            self.driver.get(f"{url}")


