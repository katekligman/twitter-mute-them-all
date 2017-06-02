import os
import sys
import time

import twitter

def usage():
    print("Environment is missing. Please read the installation docs to set your access keys and tokens.\n")
    print("See https://github.com/katekligman/twitter-mute-them-all for details")
    sys.exit()

if __name__ == '__main__':
    print("twitter-mute-them-all v1.0 by Kate Kligman. Copyright 2017, License: GPL v2.0\n")

    # Check that the environment parameters are set
    settings = (
        'CONSUMER_KEY', 'CONSUMER_SECRET',
        'ACCESS_TOKEN_KEY', 'ACCESS_TOKEN_SECRET'
    )
    if not set(settings).issubset(os.environ):
        usage()

    # Authenticate
    try:
        api = twitter.Api(
            consumer_key = os.environ['CONSUMER_KEY'],
            consumer_secret = os.environ['CONSUMER_SECRET'],
            access_token_key = os.environ['ACCESS_TOKEN_KEY'],
            access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
        )
    except Exception as e:
        if e['code'] == 32:
            print("There was an authentication issue with your account. Please read the documentation to correctly set your access keys")
        else:
            print(e)
        sys.exit(-1)

    # Verify the total number of friends to mute and prompt the user to confirm

    try:
        muted = api.GetMutesIDs()
        friends = api.GetFriendIDs()
    except Exception as e:
        print(e)
        sys.exit(-1)

    to_mute = set(friends) - set(muted)

    # Has everyone already been muted?
    if len(to_mute) <= 0:
        print("You have already muted everyone you are following.")
        sys.exit(0)

    print("You are about to mute %d unmuted friends. Continue? Y/N" % (len(to_mute),))

    c = sys.stdin.read(1)
    if not (c == 'Y' or c == 'y'):
        print("Aborting...")
        sys.exit(0)

    # Mute them all!

    tally = 0
    for friend in to_mute:
        try:
            status = api.CreateMute(friend, include_entities=False)
        except Exception as e:
            print(e)
            print("An error occured, likely a rate limit issue. Please wait a few minutes and try running this again.")
            sys.exit(0)
        print("Muted %s" % (status.screen_name))
        tally += 1
        time.sleep(5) # respect likely rate limit of 180 calls per 15 minute interval

    print("Successfully muted %d friends!" % tally)

    sys.exit(0)