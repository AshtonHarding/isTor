#!/usr/bin/env python2
#-*- coding: utf-8 -*-

"""
Small script to check if an IP is a TOR Node or not.
Created for the lainchan staff -- But usable for anyone.
"""

import lxml.html
import urllib2
from sys import exit

def check_ip():
    """Query ip address to search, then checks if it's a tor node"""
    user_ip=raw_input('\tType "quit" or an address to check.\n')

    if user_ip == 'quit':
        print('finished.')
        exit(0) # exits the program
    else:
        site='https://www.dan.me.uk/torcheck?ip='+str(user_ip)
        try:
            response = urllib2.urlopen(site)
        except:
            print('Error: The site is offline.')
        else:
            html=lxml.html.document_fromstring(response.read())
            display=html.cssselect('pre')[0].text_content()
            print(display)


if __name__=='__main__':
    while True:
        check_ip()
