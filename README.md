# step 1
create python file for running processes and commit file to github
# step 2
log in to jenkins server and and install plugin publish over ssh
# step 3
create freestyle job on jenkins 
# step 4 
give source code that is our github url
# step 5
In post build section select publish over ssh and add details of our machine like user, password and ip address
# step 6 
in execute command section 
$ python process.py
# step 6 
Build pipeline then your python file will be deployed on server and log.txt file will be created
