import rich.prompt as prompt
from   rich_menu import Menu
from   utils     import Utils
from   termcolor import colored
from   conn      import Connection
import info, sys, os
from models import Conext

class Interface():

    @staticmethod
    def banner():
        
        if sys.platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')

        base_dir = Utils.get_base_dir()
        banner   = colored(Utils.read_file(f'{base_dir}/icons/banner.ico'), 'blue')
        print(banner)
        print(f'Author:  {info.__author__} ')
        print(f'Version: {info.__version__}')
        print(f'Year:    {info.__release__}')
        print(f'License: {info.__license__}')

    @staticmethod
    def menu():

        main_menu = Menu("Create new connection"            , 
                         "Connect"                          ,
                         "List connections"                 , 
                         "Remove connection"                ,
                         "System exit"                      ,
                         color="blue"                       ,
                         align="center"                     ,
                         rule_title="Docker Context Manager",
                         panel_title="Options"              ,
                         selection_char="->"                ,
                        )
        
        match main_menu.ask(screen=False):
            case "Create new connection":

                return Connection.new()
                
            case "Connect":
                

                hosts = Conext().get_all()

                connecions_menu = Menu("Create new connection"            , 
                                       "Connect"                          ,
                                       "List connections"                 , 
                                       "Back"                             ,
                                       "System exit"                      ,
                                       color="blue"                       ,
                                       align="left"                       ,
                                       rule_title="Docker Context Manager",
                                       panel_title="Connections"          ,
                                       selection_char="->"                ,
                                  )
                
                connecions_menu.ask(screen=False)
                
                match connecions_menu.ask(screen=False):
                    case "Back":
                        Interface.menu()
                    case "System exit":
                        exit()
                    
                return Connection.connect(host)
            case "List connections":

                return Connection.list()
            case "Remove connection":

                return Connection.remove()
            case "System exit":
                exit()
class Cli():
    
    @staticmethod
    def new_connection():        
        
        host = prompt.Prompt.ask('Type a hostname')

        return True