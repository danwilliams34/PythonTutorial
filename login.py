username = raw_input("Please enter your username: ")
if username == 'user1':
    print ("You have logged in with basic rights")
    while username == 'admin':
        print ("You have logged in with admin rights")
    
while username == 'user1' or 'admin':
    password = raw_input("Please enter your password: ")
if username == 'user1':
    password = 'qwerty'
    while username == 'admin':
        password = '1234'
    