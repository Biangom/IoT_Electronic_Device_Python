#!/user/bin/env python
# coding=utf8
# vi:set sw=4 ts=4 expandtab:
# -*- coding: utf8 -*-

import sys

sys.path.insert(0, "../../")

from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

##  @brief This sample code demonstrate how to send sms through CoolSMS Rest API PHP
if __name__ == "__main__":

    # set api key, api secret
    api_key = "NCSBQ9QL4QIB6AHB"
    api_secret = "NO3K7ATJ8B8FKZNWKBNHPDRXUQQTYSE6"

    ## 4 params(to, from, type, text) are mandatory. must be filled
    params = dict()
    params['type'] = 'lms' # Message type ( sms, lms, mms, ata )
    params['to'] = '01074704184' # Recipients Number '01000000000,01000000001'
    params['from'] = '01074704184' # Sender number
    params['text'] = '문자테스트에 성공하였습니다. 빨리 대처하시기 바랍니다.  와이파이 및 3g유심테스트 성공!  문자테스트가 잘풀려서 순조롭게 진행될듯합니다 ' # LMS Message Until 2000 byte Message

    cool = Message(api_key, api_secret)
    try:
        response = cool.send(params)
        print("Success Count : %s" % response['success_count'])
        print("Error Count : %s" % response['error_count'])
        print("Group ID : %s" % response['group_id'])

        if "error_list" in response:
            print("Error List : %s" % response['error_list'])

    except CoolsmsException as e:
        print("Error Code : %s" % e.code)
        print("Error Message : %s" % e.msg)

    sys.exit()
