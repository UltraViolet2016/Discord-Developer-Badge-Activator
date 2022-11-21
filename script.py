import os
import subprocess
import sys
import time
import json

output = subprocess.check_output('node -v', shell=True).decode("utf-8")

print("""\
  _____             _    _       _____  _                       _   ____            _                           _   _            _             
 |  __ \           | |  ( )     |  __ \(_)                     | | |  _ \          | |                /\       | | (_)          | |            
 | |  | | __ _ _ __| | _|/ ___  | |  | |_ ___  ___ ___  _ __ __| | | |_) | __ _  __| | __ _  ___     /  \   ___| |_ ___   ____ _| |_ ___  _ __ 
 | |  | |/ _` | '__| |/ / / __| | |  | | / __|/ __/ _ \| '__/ _` | |  _ < / _` |/ _` |/ _` |/ _ \   / /\ \ / __| __| \ \ / / _` | __/ _ \| '__|
 | |__| | (_| | |  |   <  \__ \ | |__| | \__ \ (_| (_) | | | (_| | | |_) | (_| | (_| | (_| |  __/  / ____ \ (__| |_| |\ V / (_| | || (_) | |   
 |_____/ \__,_|_|  |_|\_\ |___/ |_____/|_|___/\___\___/|_|  \__,_| |____/ \__,_|\__,_|\__, |\___| /_/    \_\___|\__|_| \_/ \__,_|\__\___/|_|   
                                                                                       __/ |                                                   
                                                                                      |___/                                                  """)
time.sleep(2)

if (output[0] == 'v'): 
    print('━━━━━━━━━━━━━━━━━━━━━', 'Node.js is installed.', sep='\n')
    time.sleep(2)

else: 
    print('━━━━━━━━━━━━━━━━━━━━━', 'Node.js is not installed.', 'Install it via https://nodejs.org/en/download/ then run this script again.', sep='\n')
    sys.exit()

discordjs = os.path.exists('package.json')
if (discordjs == False):
    print('━━━━━━━━━━━━━━━━━━━━━', 'Installing discord.js onto your system.', sep='\n')
    time.sleep(2)
    os.system('npm i discord.js')
else:
    print('━━━━━━━━━━━━━━━━━━━━━', 'Skipping installation of discord.js as it is already installed', 'If this is an error, delete the package.json & package-lock.json', sep='\n')


time.sleep(2)
print('━━━━━━━━━━━━━━━━━━━━━', 'Head over to https://discord.com/developers/applications', 'Create a new application', sep='\n')
time.sleep(2)
client_id = input('Copy and paste Application ID: ')
print('━━━━━━━━━━━━━━━━━━━━━', 'Click Bot and click Add Bot', sep='\n')
time.sleep(2)
discord_token = input('Click reset token and paste in your token: ')
print('━━━━━━━━━━━━━━━━━━━━━', 'Create a discord server', sep='\n')
time.sleep(2)
guild_id = input('Right-click the server icon and Copy ID, paste the ID here: ')
time.sleep(2)

config = {
	"token": discord_token,
	"clientId": client_id,
	"guildId": guild_id
}

with open('config.json', 'w') as outfile:
    outfile.write(json.dumps(config))


print("Successfully created your config.json file.")
time.sleep(2)
os.system('node deploy-command.js')
time.sleep(2)
print("Type /badge in your discord server and follow the last instructions.")
os.system('node .')