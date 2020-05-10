# paper-tracker

## Run in background on GNU screen
'''
screen -S paper-tracker -dm zsh -c "cd PATH_TO_SCRIPT; python3 tracker.py; exec sh"
'''

## Username & Password
Implement the following Python script to provide username and passwords. 
`auth.py`

'''python
def getPayload():
    return {'username': '...',
            'password': '...'}

def getNatureUsername():
    return '...'

def getNaturePassword():
    return '...'


def getGRLUsername():
    return '...'


def getGRLPassword():
    return '...'


def getGJIUsername():
    return '...'


def getGJIPassword():
    return '...'


def getGmailAddress():
    return '...'

def getGmailPassword():
    return '...'

'''
