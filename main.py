#!/usr/local/bin/python2.7
import subprocess

global GoDaddy
GoDaddy = 0
global AWS
AWS = 0
global NetSolutions
NetSolutions = 0
global MarkMonitor
MarkMonitor = 0

def RegisterCount(chunk):
    global GoDaddy
    global AWS
    global NetSolutions
    global MarkMonitor
    if "GODADDY.COM" in chunk:
        GoDaddy += 1
        print color.YELLOW + "GoDaddy" + color.END
        print >> Log, "GoDaddy"
    if "AMAZON" in chunk:
        AWS += 1
        print color.YELLOW + "Amazon Web Services (AWS)" + color.END
        print >> Log, "Amazon Web Services (AWS)"
    if "NETWORK SOLUTIONS" in chunk:
        NetSolutions += 1
        print color.YELLOW + "Network Solutions" + color.END
        print >> Log, "Network Solutions"
    if "MARKMONITOR INC." in chunk:
        MarkMonitor += 1
        print color.YELLOW + "MarkMonitor, Inc." + color.END
        print >> Log, "MarkMonitor, Inc."

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

Log = open('Results.txt', 'w')
print >> Log, "---------","---------"

f = open("Domains.txt")
lines = f.readlines()
def FindReg(lines):
    for line in lines:
        lines = line.replace('\n','')
        cmd = subprocess.Popen('whois %s | grep -E "Registrar:|Last Updated by Registrar:"  ' % lines, shell=True, stdout=subprocess.PIPE)
        chunk = cmd.stdout.read(1024)
        print color.PURPLE + lines + color.END
        print >> Log, lines
        RegisterCount(chunk)
        print chunk
        print >> Log, chunk
        print ""
FindReg(lines)

print color.DARKCYAN + "AWS:" + color.END,AWS
print color.DARKCYAN + "GoDaddy:" + color.END,GoDaddy
print color.DARKCYAN + "Network Solutions:" + color.END,NetSolutions
print color.DARKCYAN + "MarkMonitor:" + color.END,MarkMonitor
