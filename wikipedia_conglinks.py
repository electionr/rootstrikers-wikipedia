import wiki
import legislators_current
import dump

import getopt, sys

def usage():
    print "--help"

def check_imdb(x,A,B) :
    a=None
    b=None
    if "imdb" in  A['id']:
        a =A['id']['imdb']
    if 'imdb' in B:
        b=B['imdb']
    if b is not None:
        if b.find("nm") > 0 :
            print x,a,b

def compare_cong(x,A,B) :
    for k in B.keys():   
        a=None
        b=None
        if k in  A['id']:
            a =A['id'][k]
        b=B[k]
        if (a is not None):
            if (not a == b):
                print x,k,a,b
    for k in  A['id'].keys() :
        print "O",k,A['id'][k]

def compare_votesmart(x,A,B) :
    k="votesmart"
    k=u'votesmart'
    a=None
    b=None
    if k in  A['id']:
        try :
            a =int(A['id'][k])

            if (a is not None):
                b=B[k]                
                if  b is None :
                    print "* [[%s]] %s" % (x,a)
                    print B
                else:
                    b = int(b)
                    if (not a == b):
                        print "* [[%s]] %s %s " % (x,a,b)
                #print "O",k,A['id'][k]
        except:
            print "* [[%s]] %s %s:" % (x,a,b)
    else:
        print "* [[%s]]  %s " % (x,b)

def compare_washpo(x,A,B) :
    k="washpo"
    k=u'washpo'
    a=None
    b=None
    try :
        if k in  A['id']:              
            a =A['id'][k]

            if (a is not None):
                a=a.strip()
                a=a.rstrip()

                b=None
                if (k in B):
                    b=B[k]                
                    if b is not None :
                        b=b.strip()
                        b=b.rstrip()
                        b=b.strip("\'")
                        b=b.rstrip("\'")
                        if (b==""):
                            b=None
                if  b is None :
                    #print "* [[%s]] washpo = %s" % (x,a)
                    pass
                else:                    
                    if (not str(a) == str(b)):
                        #print "* [[%s]] washpo = %s | not \'%s\' " % (x,a,b)
                        A['id'][k]=b
                        pass
        else:
            b=None
            if (k in B):
                b=B[k]                
                b=b.strip()
                b=b.rstrip()
                b=b.strip("\'")
                b=b.rstrip("\'")
                if (b==""):
                    b=None            

            if (b is not None):
                A['id'][k]=b

                #print "O",k,A['id'][k]
        if (not a == b) :
            print "* [[%s]] {{Mdupont:washpo|%s|%s}} {{Mdupont:washpo|%s|%s}}" % (x,b,x,a,v)
        else:
            print "* [[%s]] {{Mdupont:washpo|%s|%s}}" % (x,b,x)

    except Exception,e:
        print e,"ERROR* [[%s]] %s %s:" % (x,a,b)

def check_wikipedia(x,A,B) :
    a=None
    b=None
    k="wikipedia"
    if k in  A['id']:
        a =A['id'][k]
    if k in B:
        b=B[k]
    if b is not None:
        print x,a,b

# def check_washpo(x,A,B) :
#     a=None
#     b=None
#     k="washpo"
#     if k in  A['id']:
#         a =A['id'][k]
#     if k in B:
#         b=B[k]
#     if b is not None:
#         print x,a,b

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hv", [])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    verbose = False

    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        else:
            assert False, "unhandled option"

    legs= legislators_current.load()
    #print legs
    #    print legs['wp'].keys()
    #    print legs['wp'].items()
    names = sorted(legs['wp'].keys())
#    print names
    for x in  names:
#        print legs['wp'][x]
        try :
            d =wiki.parse_wiki_source(x,legs)
            A = legs['wp'][x]
            #check_imdb(x,A,d)
            #check_wikipedia(x,A,d)
            #compare_cong(x,A,d)
            #compare_votesmart(x,A,d)
            compare_washpo(x,A,d)
        except Exception,e:
            print "error1:",e
    dump.dump(legs)

if __name__ == "__main__":
    main()
