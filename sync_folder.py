# sync_folder.py - This program uses ADB to sync a folder on my android phone with a folder on my home PC. WIP

# Instructions: Run python script from folder you wish to sync with. Requires ADB and related DLLs in sync folder.


import os, re, subprocess, time

#from adb import adb_commands


# Set filepaths for android device and PC
pcPath = '.\\syncFolder'
os.makedirs(pcPath, exist_ok=True)
androidPath = '/storage/emulated/0/Documents/syncFolder/'
# Path for ADB executable.
adbPath = '.\\adb' 
# IP address for android device.
addr = '192.168.0.11'
port = '5555'

# Verify connection and correct device.
check_connect = subprocess.check_output(adbPath + ' connect %s' % addr)

# Attempts to repair connection if broken.
if 'No connection could be made because the target machine actively refused it' in str(check_connect):
	try:
		input('Device refused connection. Check device developer settings, connect via USB, and press [Enter]')
		print('Restarting ADB server listening on USB')
		subprocess.run(adbPath + ' usb', shell=True)
		time.sleep(5)
		subprocess.run(adbPath + 'tcpip 5555', shell=True)
	except:
		print('Failed to connect to device')
elif 'connected' in str(check_connect):
	print('Connection successful, syncing folders...')
else:
	print('Unable to connect. Exiting program...')
	exit()

# Sync folders.
try:
	push = subprocess.run(adbPath + ' -s ' + addr + ':' + port + ' push ' + pcPath + ' ' + androidPath, shell=True)
	print(push)
	pull = subprocess.run(adbPath + ' -s ' + addr + ':' + port + ' pull ' + androidPath + ' ' + pcPath, shell=True)
	print(pull)
	print('sync completed')
except:
	print('Unable to sync folders.')
	print(push)
	print(pull)