#=begin
#Copyright (c) 2011 Litle & Co.
#
#Permission is hereby granted, free of charge, to any person
#obtaining a copy of this software and associated documentation
#files (the "Software"), to deal in the Software without
#restriction, including without limitation the rights to use,
#copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the
#Software is furnished to do so, subject to the following
#conditions:
#
#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.
#=end

#
# Used for all transmission to Litle over HTTP or HTTPS
# works with or without an HTTP proxy
#
# URL and proxy server settings are derived from the configuration file
#


#from litleOnline import *
import urllib2

class Communications:
    ##For http or https post with or without a proxy
    def http_post(self,post_data):
#      config_hash = {
#               'proxy_addr': 'smoothproxy',
#               'proxy_port': '8080',
#               'url': 'https://www.testlitle.com/sandbox/communicator/online'
#               }
#
#
#      proxy_addr = config_hash['proxy_addr']
#      proxy_port = config_hash['proxy_port']
#      litle_url = config_hash['url']
  

      
      proxy_handler = urllib2.ProxyHandler({'https': 'smoothproxy:8080'})
      opener = urllib2.build_opener(proxy_handler)

      req = urllib2.Request(url='https://www.testlitle.com/sandbox/communicator/online', data=post_data)
      req.add_header('Content-type', 'text/xml')
      response = opener.open(req)

      responseXml = response.read()
      return responseXml
