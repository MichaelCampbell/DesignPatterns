#!/usr/bin/env python

# Config should hold all of your desired compabilities
# Browsers to run on, versions, locally, sauce, etc....

class Config(object):
    
    def config(self):
        desired_caps   = {}
        desired_caps['version'] = '1.0'
        desired_caps['browser'] = 'netscape'
        return desired_caps

