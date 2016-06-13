from config import source_list

from elasticsearch import Elasticsearch
#from multiprocessing.dummy import Pool as ThreadPool
#from redis import Redis
import json

def get_targets():
    with open(source_list) as fd:
        lines = [line.strip() for line in fd]
    return lines

def get_es_info(hosts):
    es = Elasticsearch(hosts)

    info = es.info()
    if not info:
        return 0

    stats = es.indices.stats()
    #print stats

    print "***********************************info of elasticsearch server : %s************************************" % hosts[0]
    for index in stats["indices"].keys():
        indices = dict(es.indices.get(index))
        #print "|Index Name\tDoc Count\tType"
        print "|",index,"\t",stats["indices"][index]["total"]["docs"]["count"],"\t",indices[index]["mappings"].keys()

        #print indices[index]["mappings"].keys()
        for type in indices[index]["mappings"].keys():

            print "----------------------------------------------%s-------------------------------------------------------" % type
            doc = es.search(index=index,doc_type=type)
            #print doc
            for hits in doc["hits"]["hits"]:
                record = dict(hits)
                for key in record["_source"].keys():
                    print key,":",record["_source"][key]
            print "\n"

    print "****************************************************end*********************************************************"
    print "\n\n"

if __name__ == '__main__':
    target_list = get_targets()
    for ip in target_list:
        hosts = list()
        hosts.append(ip)
        try:
            get_es_info(hosts)
        except:
            pass