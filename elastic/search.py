from elasticsearch_dsl import connections, DocType, Text, Date, Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models


# ElasticSearch instance (url)
client = connections.Elasticsearch(["http://localhost:9200/"])



#Search function with elasticsearch_dsl library: execute our search by calling the .execute() method
# that will return a Response object. The
#Response object allows you access to any key from the response dictionary via attribute access

'''
LIBRARIES AND EXAMPLES:
https://grimoirelab.gitbooks.io/tutorial/content/python/elasticsearch-dsl.html
http://elasticsearch-dsl.readthedocs.io/en/latest/search_dsl.html
https://github.com/elastic/elasticsearch-dsl-py
https://www.freshconsulting.com/how-to-create-a-fuzzy-search-as-you-type-feature-with-elasticsearch-and-django/
'''

#Search return response dictionary with all data from ES
def search_nested_dict(company_name):
    request = Search().using(client).filter("match", COMPANY_NAME=company_name)
    response = request.execute()
    search_result = response.to_dict()
    return search_result
#Search return response dictionary with specific values


def search(company_name):
    search_result = dict()
    request = Search().using(client).query("match", COMPANY_NAME=company_name)
    response = request.execute()
    for hit in response:
        if 'meta.id' in hit:
            search_result['ID'] = hit.meta.id
        if 'meta.index' in hit:
            search_result['INDEX'] = hit.meta.index
        if 'COMPANY_NAME' in hit:
            search_result['COMPANY_NAME'] = hit.COMPANY_NAME
        if 'EMAIL_ADDRESS' in hit:
            search_result['EMAIL_ADDRESS'] = hit.EMAIL_ADDRESS
        if 'ADDRESS' in hit:
            search_result['ADDRESS'] = hit.ADDRESS
        if 'CITY' in hit:
            search_result['CITY'] = hit.CITY
        if 'STATE' in hit:
            search_result['STATE'] = hit.STATE
        if 'ZIPCODE' in hit:
            search_result['ZIPCODE'] = hit.ZIPCODE
        if 'PHONE_NUMBER' in hit:
            search_result['PHONE_NUMBER'] = hit.PHONE_NUMBER
        if 'FAX_NUMBER' in hit:
            search_result['FAX_NUMBER'] = hit.FAX_NUMBER
        if 'SIC_CODE' in hit:
            search_result['SIC_CODE'] = hit.SIC_CODE
        if 'SIC_DESCRIPTION' in hit:
            search_result['SIC_DESCRIPTION'] = hit.SIC_DESCRIPTION
        if 'WEB_ADDRESS' in hit:
            search_result['WEB_ADDRESS'] = hit.WEB_ADDRESS
    return search_result