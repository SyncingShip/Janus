import os, re

def locate_janus_saves():
    return [f for f in os.listdir(".\\Saves\\") if re.search(r'^.+?\.sav$', f)]

def overwrite_file(file1, file2):
    """
    Takes in two file paths
    Replaces file2 with the contents of file1
    """
    with open(file1, mode='rb') as f:
        file1_content = f.read()
    with open(file2, mode='wb') as f:
        f.write(file1_content)
    
def check_hades_dir():
    home_dir = os.path.expanduser('~')
    if "Hades" in os.listdir(home_dir + "\\Documents\\Saved Games"):
        print("Hades save directory found")
        return home_dir + "\\Documents\\Saved Games\\Hades"
    else:
        print("Cannot automatically find Hades directory. Please manually copy .sav files to Janus/Saves")

def get_hades_savs(dir):
    return [f for f in os.listdir(dir) if re.search(r'^Profile\d\.sav$', f)]

def handle_backup():
    hades_sav_dir = check_hades_dir()
    hades_savs = get_hades_savs(hades_sav_dir)
    print("Choose a save to back up")

    for count, sav in enumerate(hades_savs):
        print(f"{count+1}. {sav}")

    choice = input("> ")
    if re.search(r'^\d{1,3}$', choice) and int(choice) <= len(hades_savs):
        filename = ""
        while not re.search(r'[\w\d\-\. ]+', filename):
            filename = input("Enter a filename to save as (File extension not required)\n > ")
            file1 = hades_sav_dir + "\\" + hades_savs[int(choice) - 1]
            file2 = ".\\Saves\\" + filename + ".sav"
            print(f"Writing from {file1} to {file2}")
            overwrite_file(file1, file2)
            print("Success!")

def handle_restore():
    hades_sav_dir = check_hades_dir()
    hades_savs = get_hades_savs(hades_sav_dir)
    janus_savs = locate_janus_saves()
    print("Select sav which you which to restore")

    for count, sav in enumerate(janus_savs):
        print(f"{count+1}. {sav}")
        


if __name__ == "__main__":
    print("Janus starting...")
    saves = locate_janus_saves()
    if saves != []:
        print(f"{len(saves)} backed up files found")

    choice = ""
    while not re.search(r'[1-3]', choice):
        choice = input("Please choose an option:\n1. Back up a Hades save\n2. Load a backed up save into Hades\n3. Exit\n> ")
    if choice == "3":
        exit(1)
    elif choice == "1":
        handle_backup()
    elif choice == "2":
        handle_restore()
