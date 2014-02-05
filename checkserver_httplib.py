#!/usr/bin/env python

import httplib
import sys

def check_webserver(address, port, resource):
	if not resource.startswith('/'):
		resource = '/' + resoruce
	try:
		conn = httplib.HTTPConnection(address, port)
		print "http connection create succesfully"
		req = conn.request('GET', resource)
		print 'Request for %s succesfully' % resource
		response = conn.getresponse()
		print 'Response status: %s' % response.status
	except socket.error, e:
		print 'http connection failed: %s' % e
		return False
	finally:
		conn.close()
		print 'Connection close succesfully'
	if response.status in ['200', '301']:
		return True
	else:
		return False
if __name__=='__main__':
	from optparse import OptionParser
	parser = OptionParser()
	parser.add_option("-a", "--address", dest="address", default='localhost', help="ADDRESS for webserver", metavar="ADDRESS")
	parser.add_option("-p", "--port", dest="port", type="int", default=80, help="PORT for webserver", metavar="PORT")
	parser.add_option("-r", "--resource", dest="resource", default='index.html', help="RESOURCE to check", metavar="RESOURCE")
	(options, args) = parser.parse_args()
	print 'options: %s, args: %s' % (options, args)
	check = check_webserver(options.address, options.port, options.resource)
	print 'check_webserver returned %s' % check
	sys.exit(not check)








