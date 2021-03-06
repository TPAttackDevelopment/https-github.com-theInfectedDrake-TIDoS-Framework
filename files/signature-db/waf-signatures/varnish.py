#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    TIDoS Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID (Modified version from wascan)
#This module requires TIDoS Framework
#https://github.com/the-Infected-Drake/TIDoS-Framework

from re import search,I 

def varnish(headers,content):
	detect = False
	detect |= search(r'varnish|x-varnish',str(headers.values()),I) is not None
	if detect : 
		return "Varnish FireWall (OWASP)"
