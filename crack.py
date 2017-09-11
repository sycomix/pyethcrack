from keys import decode_keystore_json #keys.py from pyethereum, we only want the decode_keystore_json function
from sys import argv
import json
import itertools
import sys

script, wallet = argv

f = open(wallet) # the json account file from keystore, here renamed
jsondata=json.load(f)

# Constructing passwords from possible combinations (see doc of pyethrecover)
grammar=[
    ('S', 's', '$'),
    ('', 'wordfish', 'else'),
    ('111', '123')
]


pwds=[]
def generate_all(el, tr): #taken from pyethrecover
    if el:
        for j in xrange(len(el[0])):
            for w in generate_all(el[1:], tr + el[0][j]):
                yield w
    else:
        yield tr


pwds = itertools.chain(pwds, generate_all(grammar,''))
pwds_l = list(pwds)
n_pws = len(pwds_l)
print 'Number of passwords to test: %d' % (n_pws,)
i=1
for l in pwds_l:
    try:
        decode_keystore_json(jsondata,l)
        print '\n*** found password in grammar list:'
        print l
        break
    except:
        sys.stdout.write("\r#%d %s" % (i,l)) #prints simple progress with # in list that is tested and the pw string
        sys.stdout.flush()
        i+=1
