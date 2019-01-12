#!/usr/bin/python3
#Shutdown your PC when you need
#TODO:
#1)Time from that moment
#Sorry for my English, I know it not wery good ~(-_-)~
import time, re, os, sys, argparse

class text:
    RED = '\x1b[31m'
    GREEN = '\x1b[32m'
    YELLOW = '\x1b[33m'
    DARK_BLUE = '\x1b[34m'
    PURPUR = '\x1b[35m'
    LIGHT_BLUE = '\x1b[36m'
    
    INVERT = '\x1b[7m'
    GLITCH = '\x1b[5m'
    LINE = '\x1b[4m'
    STRONG = '\x1b[1m'
    END = '\x1b[0m'

def main():
	print(logo)
	TIME = [100, 100]
	while (((int (TIME[0])) >= 24) or ((int (TIME[1])) >= 60)):
		TIME = input(text.GREEN + text.STRONG + "Shutdown time" + text.YELLOW + " HH MM" + text.END + text.GREEN + ": " + text.END)
		TIME = (re.findall(r"[\w']+", TIME))

	HOURS = str(TIME[0])
	MINUTES = str(TIME[1])
	execute(HOURS, MINUTES)
	print("execute: OK")


def execute(HOURS, MINUTES):
	cmd = "shutdown -h " + HOURS + ":" + MINUTES
	while True:
		answ = input(text.RED + text.STRONG + "Execute \'" + cmd + "\'? Y/n: ")
		if(answ == '' or answ == 'y' or answ == 'Y'):
			print("Running: " + cmd)
			os.system(cmd)
			break
		elif(answ == 'n' or answ == 'N'):
			break
		else:
			print("Error input, try again")
	exit("Exit...")

def argload():
	if os.geteuid() != 0:
		exit(text.RED + text.STRONG + "Programm need root.\nPlease, try again with 'sudo'.\nExit..." + text.END)
	if(len(sys.argv) == 1):
		sys.argv[1:] = ["-h"]
	parser = argparse.ArgumentParser()
	parser.add_argument ('-M', '--minutes',  type=int, help='At how many mins')
	parser.add_argument ('-H', '--hours',  type=int, help='At how many hours')
	parser.add_argument ('-G', '--textgui', action='store_const', const='1', help='Turn on text-ui')
	arg = parser.parse_args()
	if (format(arg.textgui) == '1'):
		try:
			os.system("clear")
			main()
		except KeyboardInterrupt:
			os.system("clear")
			print(logo)
			print(text.GREEN + text.STRONG + "Exit..." + text.END)
			time.sleep(0.5)
			os.system("clear")
			exit() 
	if (int(format(arg.hours)) >= 24 or int(format(arg.minutes)) >= 60):
		exit(text.RED + text.STRONG + "One ore more params is not true\nExit..." + text.END)
	execute((format(arg.hours)), (format(arg.minutes)))

if __name__ == '__main__':
    
    
    logo = text.YELLOW + text.GLITCH + text.STRONG + '''

 (           (       )             (        )             )  
 )\ )  (     )\ ) ( /(        *   ))\ )  ( /( (  (     ( /(  ''' + text.RED + '''
(()/(  )\   (()/( )\())   ( ` )  /(()/(  )\()))\))(   ')\()) 
 /(_)|((_)   /(_)|(_)\    )\ ( )(_))(_))((_)\((_)()\ )((_)\  
(_)) )\___  (_))  _((_)_ ((_|_(_()|_))_   ((_)(())\_)()_((_) ''' + text.END + text.GREEN + text.STRONG + '''
| _ ((/ __| / __|| || | | | |_   _||   \ / _ \ \((_)/ / \| | 
|  _/| (__  \__ \| __ | |_| | | |  | |) | (_) \ \/\/ /| .` | 
|_|   \___| |___/|_||_|\___/  |_|  |___/ \___/ \_/\_/ |_|\_| 
                                                             
    
    ''' + text.LIGHT_BLUE + '''By allespro 
    github.com/Allespro
    ''' + text.END
    
    argload()
