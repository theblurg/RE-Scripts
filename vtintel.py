#!/usr/bin/python

import requests
import sys

if __name__ == "__main__":
        for x in sys.argv[1:]:
                print "Attempting to fetch %s" % x
                params = {'apikey': '', 'hash': x}
                response = requests.get('https://www.virustotal.com/vtapi/v2/file/download', params=params)
                print "Response: %s" % response
                downloaded_file = response.content
                file = open(x,'wb')
                file.writelines(downloaded_file)
                file.close()
