import Ballotpedia

def parse_senate () :
    return Ballotpedia.parse ('http://ballotpedia.org/wiki/index.php/Template:Simple_senate_list?printable=yes')

parse_senate()
