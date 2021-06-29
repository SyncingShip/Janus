# Janus
Janus is a save manager for Hades by Supergiant Games.   
This allows you to manage multiple saves, making it easier to back up and load saves with specific seeds.  
### Prerequistites and first time setup
Janus requires [Python 3](www.python.org/downloads/release/latest)  
IMPORTANT: Make sure to tick "Add Python to PATH" when installing Python 3

To keep your controls and settings between saves, replace default.ctrls and default.xml in the config folder with Profile1.ctrls and Profile1.xml from `\Documents\Saved Games\Hades`
Run Janus with run.bat
### Backing up
Pick which Hades profile you want to back up.   
Enter a name to back up as when prompted
### Loading
Choose which sav file you want to load  
Choose which profile number you want to load this save to
### Deleting
Choose which Hades profile you want to wipe.  
If you want to remove a backed up save, delete the .sav file in the Saves folder of Janus.

### Common issues / Solutions
If Janus isn't running:

Go to "Manage App Execution Aliases" in windows settings
If there are any aliases for Python.exe or Python3.exe, disable them

Open cmd and type `python` or `python --version`
If you get `'python' is not recognized as an internal or external command, operable program or batch file.` then there is something wrong with your python installation.  
If you didn't choose to add python to your PATH, follow [this guide](https://geek-university.com/python/add-python-to-the-windows-path/) or reinstall python with this option

If you have OneDrive enabled and your Documents folder is backed up in OneDrive, this will cause many problems. I highly recommend you [disable OneDrive](https://support.microsoft.com/en-us/office/turn-off-disable-or-uninstall-onedrive-f32a17ce-3336-40fe-9c38-6efb09f944b0) if you are not using it 

In a similar problem, disabling steam cloud saves may also solve this problem. To do this, right click on Hades in Steam, select Properties and then untick "Keep games saves in the Steam Cloud for Hades"

There is a possibility that Janus is detecting a Hades directory that is different to the one used by the Hades game itself. This again is a common issue if the Documents folder is backed up by OneDrive. If OneDrive is disabled, you should try editing config.json.  

1. With the key "override_hades_dir" set "false" to "true"
2. With the key "hades_dir" set the empty quotes to the directory you wish Janus to use. Please use double backslashes instead of single backslashes or single forward slashes as the separator. For example if the directory you want to use is "C:/Users/Player/OneDrive/Documents/Saved Games/Hades" you should enter this in the empty quotes: "C:\\Users\\Player\\OneDrive\\Documents\\Saved Games\\Hades"

### Disclaimer
Modding Hades is not officially endorsed by Supergiant Games.  
Any game crashes, save corruption, crashes or other problems resulting from modding are not their responsibility to deal with.  
If you have any questions about modding, or are having issues with any of my mods, feel free to contact me on Discord (Ship#0101)
