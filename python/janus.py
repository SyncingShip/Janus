import os, re, json, time

def locate_janus_saves():
    return [f for f in os.listdir(".\\Saves\\") if re.search(r'^.+?\.sav$', f)]

def copy_file(file1, file2):
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
        return home_dir + "\\Documents\\Saved Games\\Hades"
    else:
        print("Cannot automatically find Hades directory. Please manually copy .sav files to Janus/Saves")

def get_hades_savs(dir):
    return [f for f in os.listdir(dir) if re.search(r'^Profile\d\.sav$', f)]

def cleanup_files(profile_number):
    if os.path.isfile(HADES_SAV_DIR + "\\activeProfile"): os.remove(HADES_SAV_DIR + "\\activeProfile") 
    if os.path.isfile(HADES_SAV_DIR + "\\activeProfile.bak"): os.remove(HADES_SAV_DIR + "\\activeProfile.bak")
    copy_file(".\\config\\default.ctrls", f"{HADES_SAV_DIR}\\Profile{profile_number}.ctrls")
    copy_file(".\\config\\default.ctrls", f"{HADES_SAV_DIR}\\Profile{profile_number}.ctrls.bak")
    copy_file(".\\config\\default.xml", f"{HADES_SAV_DIR}\\Profile{profile_number}.xml")
    copy_file(".\\config\\default.xml", f"{HADES_SAV_DIR}\\Profile{profile_number}.xml.bak")

def delete_profile(profile_number):
    files = [f for f in os.listdir(HADES_SAV_DIR) if re.search(r'^Profile' + re.escape(profile_number) + r'(\.|_).+$', f)]
    for f in files:
        os.remove(HADES_SAV_DIR + "\\" + f)
    # cleanup_files(profile_number)
    print(f"Profile {profile_number} successfully deleted")

def handle_deletion():
    if len(HADES_SAVS) > 0:
        print("Choose a save to delete")
        for count, sav in enumerate(HADES_SAVS):
            print(f"{count+1}. {sav}")

        choice = input("> ")
        if re.search(r'^\d$', choice) and int(choice) <= len(HADES_SAVS):
            delete_profile(choice)
    else:
        print("No Hades saves found")

def handle_backup():
    print("Choose a save to back up")

    for count, sav in enumerate(HADES_SAVS):
        print(f"{count+1}. {sav}")

    choice = input("> ")
    if re.search(r'^\d{1,4}$', choice) and int(choice) <= len(HADES_SAVS):
        filename = ""
        while not re.search(r'[\w\d\-\. ]+', filename):
            filename = input("Enter a filename to save as (File extension not required)\n > ")
            file1 = HADES_SAV_DIR + "\\" + HADES_SAVS[int(choice) - 1]
            file2 = ".\\Saves\\" + filename + ".sav"
            print(f"Backing up {HADES_SAVS[int(choice) - 1]} into {filename}.sav")
            copy_file(file1, file2)
            print("Success!")

def handle_restore():
    print("Select which Janus sav you wish to Load")

    for count, sav in enumerate(JANUS_SAVS):
        print(f"{count+1}. {sav}")
    
    choice = input("> ")
    while not (re.search(r'^\d{1,4}$', choice) and int(choice) <= len(JANUS_SAVS)):
        choice = input("> ")

    for x in range(1, 5):
        if f"Profile{x}.sav" in HADES_SAVS:
            print(f"{x}. Profile {x}")
        else:
            print(f"{x}. Profile {x} (Empty)")

    profile_slot = input("> ")
    while not re.search(r'^[1-4]$', profile_slot):
        print(f"Please enter a valid option (1-4)")
        profile_slot = input("> ")

    janus_filepath = ".\\Saves\\" + JANUS_SAVS[int(choice)-1]
    hades_filepath = f"{HADES_SAV_DIR}\\Profile{profile_slot}.sav"
    print(f"Loading {JANUS_SAVS[int(choice)-1]} into Profile{profile_slot}.sav")
    copy_file(janus_filepath, hades_filepath)
    print("Performing cleanup...")
    cleanup_files(int(profile_slot))
    print("Success")

if __name__ == "__main__": 
    user_exit = False
    HADES_SAV_DIR = check_hades_dir()
    HADES_SAVS = get_hades_savs(HADES_SAV_DIR)
    JANUS_SAVS = locate_janus_saves()

    with open("./config.json") as jfile:
        CONFIG = json.load(jfile)
        jfile.close()

    print("\nHades Save Dir has been automatically detected as " + HADES_SAV_DIR)

    if CONFIG["override_hades_dir"].lower() == "true":
        HADES_SAV_DIR = CONFIG["hades_dir"]
        print("Hades Save Dir has been overriden to be " + HADES_SAV_DIR)

    print("Loaded configuration")
    
    saves = locate_janus_saves()
    if saves != []:
        print(f"{len(saves)} backed up files found\n")

    
    while not user_exit:
        choice = ""
        while not re.search(r'[1-4]', choice):
            choice = input("Please choose an option:\n1. Back up a Hades save\n2. Load a backed up save into Hades\n3. Delete profile\n4. Exit\n> ")
        if choice == "4":
            user_exit = True
        elif choice == "1":
            handle_backup()
            JANUS_SAVS = locate_janus_saves()
        elif choice == "2":
            handle_restore()
            HADES_SAVS = get_hades_savs(HADES_SAV_DIR)
        elif choice == "3":
            handle_deletion()
            HADES_SAVS = get_hades_savs(HADES_SAV_DIR)
