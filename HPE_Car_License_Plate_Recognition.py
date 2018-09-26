#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""@author: sourabh
 #Description:Car License plate detection of India
 #Version:1.1
 #Revision Date:27/08/2016

"""
from havenondemand.hodclient import *
import json
import pandas as pd

client = HODClient("695e513c-1e1e-4e39-a666-95b3ed0ad945", "v1") #apikey

params = {'url': 'https://www.havenondemand.com/sample-content/videos/gb-plates.mp4', 'source_location': 'GB'} ##if using url
#params = {'file': 'E:/abcd.mp4', 'source_location': 'GB'} ## or if using a local file
response_async = client.post_request(params, 'recognizelicenseplates', async=True)
jobID = response_async['jobID']
#print jobID

## Wait some time afterwards for async call to process...
response = client.get_job_result(jobID)
print response

#dump data in a json file
with open('data.json', 'w') as outfile:
    json.dump(response, outfile)
