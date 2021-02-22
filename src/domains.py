import nltk
from collections import defaultdict
from nltk.corpus import wordnet as wn

nltk.download('wordnet')
nltk.download('omw')

# Loading the Wordnet domains.
domain2synsets = defaultdict(list)
synset2domains = defaultdict(list)
for i in open('./WordNet/wn-domains-3.2/wn-domains-3.2-20070223', 'r'):
    ssid, doms = i.strip().split('\t')
    doms = doms.split()
    synset2domains[ssid] = doms
    for d in doms:
        domain2synsets[d].append(ssid)

# Gets domains given synset.
for ss in wn.all_synsets():
    ssid = str(ss.offset).zfill(8) + "-" + ss.pos()
    if synset2domains[ssid]: # not all synsets are in WordNet Domain.
        print(ss, ssid, synset2domains[ssid])

# Gets synsets given domain.        
for dom in sorted(domain2synsets):
    print(dom, domain2synsets[dom][:3])