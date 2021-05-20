import random


# Reads .txt file that contains only the token
def token(file="token.txt"):
    fi = open(file)
    key = fi.read()
    fi.close()
    return key


def affirmation_of_the_day(file="affirmations.txt"):
    fi = open(file)
    lines = fi.read().splitlines()
    line = random.choice(lines)
    fi.close()
    return line

# Not used atm
def get_user_id(file="user.txt"):
    fi = open(file)
    user = fi.read()
    fi.close()
    return user
