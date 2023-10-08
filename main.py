# Import the zipfile and itertools libraries
import zipfile
import itertools

# Define a function for brute force zip file decryption
def brute_force_zip(zip_file, password_length, alphabet):
  # Create a ZipFile object from the zip file name
  zip = zipfile.ZipFile(zip_file)
  # Generate a list of possible password combinations
  passwords = itertools.product(alphabet, repeat=password_length)
  # Iterate through password combinations
  for password in passwords:
    # Convert the password combination into a string
    password = "".join(password)
    try:
      # Attempt to extract the zip file with the current password
      zip.extractall(pwd=password.encode())
      # If successful, return the password and exit the loop
      return password
      break
    except:
      # If unsuccessful, continue the loop with the next password combination
      continue

# Call the brute force function with the provided parameters
zip_file = "/storage/emulated/0/Download/hackme.zip" # Name of the zip file to unlock
password_length = 20 # Length of the password
alphabet = "abcdefghijklmnopqrstuvwxyz0123456789" # Character set for the password
password = brute_force_zip(zip_file, password_length, alphabet) # Call the function and store the result in the 'password' variable

# Print the password to the screen if found, or a message indicating failure if not found
if password:
  print("The password for the zip file is:", password)
else:
  print("Unable to find the password for the zip file")
