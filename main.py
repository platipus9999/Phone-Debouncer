from pyshade import *
import random, os, time
from threading import Thread, Lock
import phonenumbers
from phonenumbers import carrier

banner = """
______ _                     __   __
| ___ \ |  Nows ~ Platipus   \ \ / /
| |_/ / |__   ___  _ __   ___ \ V / 
|  __/| '_ \ / _ \| '_ \ / _ \/   \ 
| |   | | | | (_) | | | |  __/ /^\ \\
\_|   |_| |_|\___/|_| |_|\___\/   \/ """

Sys.Title("Nows@PLATIPUS ~ Phone Debouncer")
val  = 0

class PhoneX:
        def count_phone():
                total = 0
                dir = os.listdir('Valid/')
                for Opera in dir:
                        with open(f"Valid/{Opera}", "r+") as f:
                                res = len(f.read().splitlines())
                                total += res
                Mode.Horizontal(colors.purple_to_cyan, f"\n[!]You Have About {total} Phone Numbers", 4)

        def phone_debouncer(display):
                global val

                while True :
                        try:    
                                num = "+33"+"".join(random.choice("0123456789") for _ in range(9))
                                valid = phonenumbers.parse(num)
                                opera = carrier.name_for_number(valid, 'fr') 

                                os.makedirs("Valid/", exist_ok=True)

                                if phonenumbers.is_valid_number(valid) and opera !="":
                                        val +=1
                                        Sys.Title(f"Nows@PLATIPUS ~ Phone Debouncer [Valid: {val}]")
                                        if display == 'T':
                                                Mode.Horizontal(colors.purple_to_red,f"[+] Valid: {num}: [Counter : {val}]",5, False)

                                        if "e*Message" in opera:
                                                opera = "eMessage"
                                                
                                        with open(f"Valid/{opera}.txt" , 'a+') as file :
                                                file.write(num + '\n')
                                Lock.acquire()
                                val += 1
                                Lock.release()
                        except:
                                pass
        def main():

                choice = int(Mode.Vertical(colors.purple_to_red, """                                                                              
        ##### ##      /                                     ###          ##     
     ######  /###   #/                                     /####       ####  /  
    /#   /  /  ###  ##                                    /   ###      /####/   
   /    /  /    ### ##                                         ###    /   ##    
       /  /      ## ##                                          ###  /          
      ## ##      ## ##  /##      /###   ###  /###     /##        ###/           
      ## ##      ## ## / ###    / ###  / ###/ #### / / ###        ###           
    /### ##      /  ##/   ###  /   ###/   ##   ###/ /   ###       /###          
   / ### ##     /   ##     ## ##    ##    ##    ## ##    ###     /  ###         
      ## ######/    ##     ## ##    ##    ##    ## ########     /    ###        
      ## ######     ##     ## ##    ##    ##    ## #######     /      ###       
      ## ##         ##     ## ##    ##    ##    ## ##         /        ###      
      ## ##         ##     ## ##    ##    ##    ## ####    / /          ###   / 
      ## ##         ##     ##  ######     ###   ### ######/ /            ####/  
 ##   ## ##          ##    ##   ####       ###   ### ##### /              ###   
###   #  /                 /                                                    
 ###    /                 /                                                     
  #####/                 /                                                      
    ###                 /                                                       
                    Phone Debouncer -> By PLATIPUS#5696
[1]Phone Debouncer
[2]Count Valid Phone Number
>  """, 2,False, True))
                if choice == 1:
                        thread = Mode.Horizontal(colors.purple_to_red, "\n\n[!]Above 1 thread, the display will be messy\nNumber of Threads > ", 4, False, True)
                        display = Mode.Horizontal(colors.purple_to_red, "\nDisplay Result [T/F]: ", 4, False, True).upper()
                        
                        return choice, thread, display
                else:       
                        return choice
if '__main__' == __name__:

        result = PhoneX.main() 

        if result == 2:
                Sys.Clear()
                Mode.Vertical(colors.purple_to_cyan, banner, 1, False, True)
                PhoneX.count_phone()  

        elif result[0] == 1:
                
                print("\n")

                Sys.Clear()
                Mode.Vertical(colors.purple_to_red, f"""{banner}\n\n[!] Starting...""", 3, False, True)
                print("\n")

                for _ in range(int(result[1])): 
                        Thread(target=PhoneX.phone_debouncer, args=result[2]).start()

