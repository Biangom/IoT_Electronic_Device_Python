from _future_ import print_function
import gammu
import sys

state_machine = gammu.StateMachine()

if len(sys.argv) > 2:
    state_machine.ReadConfig(Filename=sys.argv[1]
    del sys.argv[1]

else:
    state_machine.ReadConfig()

if len(sys.argv) != 2:
    print('Usage: sendsms.py [configfile] RECIPIENT_NUMBER')
    sys.exit(1)

state_machine.Init()

message = {
    'Text': 'test22',
    'SMSC': {'Location': 1},
    'Number': sys.argv[1],
}

state_machine.SendSMS(message)