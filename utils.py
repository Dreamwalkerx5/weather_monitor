#  Copyright (c) 2019. Steven Taylor. All rights reserved.
import sys
from datetime import datetime


def pad_string(text='', length=0, pad_char='', back=True):
    padding = length - len(text)
    if padding >= 0:
        if back:
            text += pad_char * padding
        else:
            text = (pad_char * padding) + text
    else:
        text = text[:length]

    return text


def convert_date(timestamp):

    try:
        d = datetime.utcfromtimestamp(timestamp)
        formatted_date = d.strftime('%d %b %Y')
        return formatted_date
    except:
        print("Unexpected error:", sys.exc_info()[0])
        print(sys.exc_info()[1])


def convert_time(timestamp):
    try:
        d = datetime.utcfromtimestamp(timestamp)
        formatted_time = d.strftime('%H:%M:%S')
        return formatted_time
    except:
        print("Unexpected error:", sys.exc_info()[0])
        print(sys.exc_info()[1])
