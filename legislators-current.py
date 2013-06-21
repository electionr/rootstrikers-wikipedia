import yaml
import cache


def loadlegis ():
    legis = yaml.load(file('congress-legislators/legislators-current.yaml', 'rb').read())
    return legis

def load():
    data = {}
    legis = cache.cache ( "legis",loadlegis)
    for l in legis:
        if 'wikipedia' in l['id'] :
            wp = l['id']['wikipedia']
            data[wp]=l
    return data

#print legis
#print legis.keys
