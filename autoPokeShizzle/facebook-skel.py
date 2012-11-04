FBPASS = 'facebook password here'
FBLOGIN = 'facebook username/email here'
SQL_CONNECT_STRING='sqlalchemy connection string'


#Below are some variables that control the frequency of poking
#We give some reasonable defaults here. Change them at your own
#peril.

#Number of seconds between each check for pokes
POKE_LOOP_PAUSE = 3600

#Varition in the loop pause (seconds)
POKE_LOOP_JITTER = 180

#Time between each poke when poking people (seconds)
POKE_PAUSE = 2.5

#Variation in between books (seconds)
POKE_JITTER = 0.5
