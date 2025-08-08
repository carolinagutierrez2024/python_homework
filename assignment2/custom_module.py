#this variable stores the secret
secret = "shazam!"

# So I can change the value of the secret
def set_secret(new_secret):
   global secret
   secret = new_secret