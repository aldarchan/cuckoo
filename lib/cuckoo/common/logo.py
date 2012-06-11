# Copyright (C) 2010-2012 Cuckoo Sandbox Developers.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import sys
import random

from lib.cuckoo.common.colors import color, yellow
from lib.cuckoo.common.constants import CUCKOO_VERSION

def logo():
    """Cuckoo asciiarts.
    @return: asciiarts array.
    """
    logos = []

    logos.append("""
                          __
                         [  |  _
   .---.  __   _   .---.  | | / ]  .--.    .--.
  / /'`\\][  | | | / /'`\\] | '' < / .'`\\ \\/ .'`\\ \\
  | \__.  | \\_/ |,| \\__.  | |`\\ \\| \\__. || \\__. |
  '.___.' '.__.'_/'.___.'[__|  \\_]'.__.'  '.__.'""")

    logos.append("""
                      \\                  
    ___  ,   .   ___  |   ,   __.    __. 
  .'   ` |   | .'   ` |  /  .'   \ .'   \\
  |      |   | |      |-<   |    | |    |
   `._.' `._/|  `._.' /  \\_  `._.'  `._.'""")

    logos.append("""
  01100011 01110101 01100011 01101011 01101111 01101111""")

    logos.append("""
                                 _|                            
     _|_|_|  _|    _|    _|_|_|  _|  _|      _|_|      _|_|    
   _|        _|    _|  _|        _|_|      _|    _|  _|    _|  
   _|        _|    _|  _|        _|  _|    _|    _|  _|    _|  
     _|_|_|    _|_|_|    _|_|_|  _|    _|    _|_|      _|_|""")

    logos.append("""
                      __                  
  .----..--.--..----.|  |--..-----..-----.
  |  __||  |  ||  __||    < |  _  ||  _  |
  |____||_____||____||__|__||_____||_____|""")

    logos.append("""
                          .:                 
                          ::                 
    .-.     ,  :   .-.    ;;.-.  .-.   .-.   
   ;       ;   ;  ;       ;; .' ;   ;';   ;' 
   `;;;;'.'`..:;._`;;;;'_.'`  `.`;;'  `;;'""")

    logos.append("""
  eeee e   e eeee e   e  eeeee eeeee 
  8  8 8   8 8  8 8   8  8  88 8  88 
  8e   8e  8 8e   8eee8e 8   8 8   8 
  88   88  8 88   88   8 8   8 8   8 
  88e8 88ee8 88e8 88   8 8eee8 8eee8""")

    logos.append("""
  _____________________________________/\/\_______________________________
  ___/\/\/\/\__/\/\__/\/\____/\/\/\/\__/\/\__/\/\____/\/\/\______/\/\/\___
  _/\/\________/\/\__/\/\__/\/\________/\/\/\/\____/\/\__/\/\__/\/\__/\/\_
  _/\/\________/\/\__/\/\__/\/\________/\/\/\/\____/\/\__/\/\__/\/\__/\/\_
  ___/\/\/\/\____/\/\/\/\____/\/\/\/\__/\/\__/\/\____/\/\/\______/\/\/\___
  ________________________________________________________________________""")

    logos.append("""
   _______ _     _ _______ _     _  _____   _____ 
   |       |     | |       |____/  |     | |     |
   |_____  |_____| |_____  |    \\_ |_____| |_____|""")

    logos.append("""
                     _ 
    ____ _   _  ____| |  _ ___   ___
   / ___) | | |/ ___) |_/ ) _ \ / _ \\
  ( (___| |_| ( (___|  _ ( |_| | |_| |
   \\____)____/ \\____)_| \\_)___/ \\___/""")

    logos.append("""
           _______                   _____                    _____          
          /::\\    \\                 /\\    \\                  /\\    \\         
         /::::\\    \\               /::\\____\\                /::\\    \\        
        /::::::\\    \\             /::::|   |               /::::\\    \\       
       /::::::::\\    \\           /:::::|   |              /::::::\\    \\      
      /:::/~~\\:::\\    \\         /::::::|   |             /:::/\\:::\\    \\     
     /:::/    \\:::\\    \\       /:::/|::|   |            /:::/  \\:::\\    \\    
    /:::/    / \\:::\\    \\     /:::/ |::|   |           /:::/    \\:::\\    \\   
   /:::/____/   \\:::\\____\\   /:::/  |::|___|______    /:::/    / \\:::\\    \\  
  |:::|    |     |:::|    | /:::/   |::::::::\\    \\  /:::/    /   \\:::\\ ___\\ 
  |:::|____|     |:::|    |/:::/    |:::::::::\\____\\/:::/____/  ___\\:::|    |
   \\:::\\    \\   /:::/    / \\::/    / ~~~~~/:::/    /\\:::\\    \\ /\\  /:::|____|
    \\:::\\    \\ /:::/    /   \\/____/      /:::/    /  \\:::\\    /::\\ \\::/    / 
     \\:::\\    /:::/    /                /:::/    /    \\:::\\   \\:::\\ \\/____/  
      \\:::\\__/:::/    /                /:::/    /      \\:::\\   \\:::\\____\\    
       \\::::::::/    /                /:::/    /        \\:::\\  /:::/    /    
        \\::::::/    /                /:::/    /          \\:::\\/:::/    /     
         \\::::/    /                /:::/    /            \\::::::/    /      
          \\::/____/                /:::/    /              \\::::/    /       
           ~~                      \\::/    /                \\::/____/        
                                    \\/____/                                  
                                                       it's Cuckoo!""")

    logos.append("""
                               ),-.     /
  Cuckoo Sandbox              <(a  `---',' 
     no chance for malwares!  ( `-, ._> )
                               ) _>.___/
                                   _/""")

    logos.append("""
  .-----------------.
  | Cuckoo Sandbox? |
  |     OH NOES!    |\\  '-.__.-'   
  '-----------------' \\  /oo |--.--,--,--.
                         \\_.-'._i__i__i_.'
                               \"\"\"\"\"\"\"\"\"""")

    print(color(random.choice(logos), random.randrange(31, 37)))
    print
    print(" Cuckoo Sandbox %s" % yellow(CUCKOO_VERSION))
    print(" www.cuckoobox.org")
    print(" Copyright (c) 2010-2012")
    print