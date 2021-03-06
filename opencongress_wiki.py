import re
import json
import encode
import dump
from pprint import pprint
import legislators_current as leg
import cache 
import urllib
import urllib2 
import dump 
"""
extract open congress data and records
"""
import getopt, sys
from lxml import etree
from StringIO import StringIO
def load():
    legs= leg.load()
    out = open("report.wiki", 'w')

    for x in sorted(legs['wp'].keys()):
        idsobj= legs['wp'][x]['id'] 
        gt = idsobj['govtrack']
        oname = idsobj['opencongwiki']
        name = unicode(oname)
        name = name.encode('utf-8')
        name= urllib.quote_plus(name)

        url = "http://www.opencongress.org/w/index.php?title=%s&printable=yes" % name

        try :
            data = cache.cacheweb( url)
        except urllib2.HTTPError, e: 
            if ( e.code == 404) :
                p='http://www.opencongress.org/people/show/%d' % gt
                #            print u"* Missing [[" , unicode(oname) , u"]] from [", unicode(p),  u" ", unicode(oname) ,  u"]"
                s=u"* Missing [[{}]] from [{} {}]\n".format(unicode(oname),p,unicode(oname))
                print s
                out.write(s.encode('utf-8'))
                idsobj['opencongwiki']="Error"
                
        except Exception, e:
#            print "Missing [[",name,"]]"
            print "failed", name ,e
            idsobj['opencongwiki']="Error2"
        except KeyboardInterrupt:
            print "bye"
            exit()
    dump.dump(legs)        

def usage():
    print "--help --verbose"


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hv", ["help", "verbose"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    verbose = False
    convertInt=False
    for o, a in opts:
        if (o == "-v", "--verbose"):
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        else:
            assert False, "unhandled option"

    load()



if __name__ == "__main__":
    main()
