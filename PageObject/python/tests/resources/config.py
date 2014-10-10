#!/usr/bin/env python

class Config(object):
    
    def config(self):
        desired_caps   = {}
        desired_caps['version'] = '1.0'
        desired_caps['browser'] = 'netscape'
        return desired_caps

