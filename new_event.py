#====================================================
# new_event.py
# Microsofdt Taiwan <=> 長佳
# GENERATE AN ONLINE MEETING PROGRAMMATICALLY

# Created by YIHAN HISAO on Jun 16, 2021.
# Copyright © 2021 Microsofdt Taiwan & YIHAN HSIAO. All rights reserved.
#====================================================
import math
import os
import random
import sys
import time
import json

### Get current time
def get_time( time_category ):
  if time_category == "reservation": # return the reservation date & time
    return_time = time.ctime()
    
  # elif time_category == "treatment": # return the treatment date & time
  #   seconds = time.time()
  #   result = time.localtime(seconds)
  #   return_time = str(result.tm_mon) + " " + str(result.tm_mday)

  return return_time


def create_event(token, subject, start, end, attendees=None, body=None, timezone='UTC'):
  #### create event object
  new_event = {
    'subject': subject,
    'start': {
      'dateTime': start,
      'timeZone': timezone
    },
    'end': {
      'dateTime': end,
      'timeZone': timezone
    }
  }

  #### add attendees
  if attendees:
    attendee_list = []
    for email in attendees:
      # Create an attendee object
      # https://docs.microsoft.com/graph/api/resources/attendee?view=graph-rest-1.0
      attendee_list.append({
        'type': 'required',
        'emailAddress': { 'address': email }
      })

    new_event['attendees'] = attendee_list

  #### add body
  if body:
    # Create an itemBody object
    # https://docs.microsoft.com/graph/api/resources/itembody?view=graph-rest-1.0
    new_event['body'] = {
      'contentType': 'text',
      'content': body
    }


  return

if __name__ == "__main__":
  print("Start reservation...")

  ### 