import os

original_folder = "C:\\Users\\kathik\\OneDrive - Capgemini\\Desktop\\Test"
destination_folder = "C:\\Users\\kathik\\OneDrive - Capgemini\\Desktop\\Test\\CleanedUp"

os.mkdir(destination_folder)

for entry in os.scandir(destination_folder):
    original_location = os.path.join(original_folder, entry.name)
    destination_location = os.path.join(destination_folder, entry.name)

    if os.path.isfile(destination_location):
        os.rename(destination_location, original_location)
