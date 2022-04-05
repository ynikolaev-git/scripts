# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 14:16:11 2022

@author: 1
"""
#!/usr/bin/env python
from __future__ import print_function
import sys
import requests
from datetime import datetime, timedelta

API_HOST = 'https://access.redhat.com/hydra/rest/securitydata'


def get_data(query):

    full_query = API_HOST + query
    r = requests.get(full_query)
 
    if r.status_code != 200:
        print('ERROR: Invalid request; returned {} for the following '
              'query:\n{}'.format(r.status_code, full_query))
        sys.exit(1)

    if not r.json():
        print('No data returned with the following query:')
        print(full_query)
        sys.exit(0)

    return r.json()


# # Get a list of issues and their impacts for RHSA-2016:1847
# endpoint = '/cve.json'
# prod = '.el6'
# date = datetime.now() - timedelta(days=300)
# params = 'package='+prod+'&after=' + str(date.date())
# #params = 'advisory=RHSA-2021:2735'
# #params = 'advisory=RHSA-2016:1847'
# #params = ''

# data = get_data(endpoint + '?' + params)


# for cve in data:
#     if (prod in str(cve['affected_packages'])):
# #        print(cve['CVE'], cve['severity'], cve['affected_packages'])
#         print(cve['CVE'], cve['severity'], cve['advisories'])
#         print('===========')
# print(len(data))


print('-----')
# Get a list of kernel advisories for the last 30 days and display the
# packages that they provided.
y = 2015
rhel = open(str(y)+'_'+'rhel.csv','w')
print('product', 'year ', 'RHSA', 'severity', 'released_on', 'CVEs', sep =';', file=rhel, flush=True)
endpoint = '/cvrf.json'
date_before = datetime(y+1,1,1)
date_after = datetime(y,1,1)

prod = '.el6'
params = 'package='+prod+'&after=' + str(date_after.date()) + '&before=' + str(date_before.date())
data = get_data(endpoint + '?' + params)
for advisory in data:
    s = advisory['released_on']
    print(prod, y, advisory['RHSA'], advisory['severity'], s[:s.find('T')],','.join(advisory['CVEs']), sep =';', file=rhel, flush=True)
print(y, prod, '| total =', len(data), sep = ' ')

prod = '.el7'
params = 'package='+prod+'&after=' + str(date_after.date()) + '&before=' + str(date_before.date())
data = get_data(endpoint + '?' + params)
for advisory in data:
    s = advisory['released_on']
    print(prod, y, advisory['RHSA'], advisory['severity'], s[:s.find('T')],','.join(advisory['CVEs']), sep =';', file=rhel, flush=True)
print(y, prod, '| total =', len(data), sep = ' ')

prod = '.el8'
params = 'package='+prod+'&after=' + str(date_after.date()) + '&before=' + str(date_before.date())
data = get_data(endpoint + '?' + params)
for advisory in data:
    s = advisory['released_on']
    print(prod, y, advisory['RHSA'], advisory['severity'], s[:s.find('T')],','.join(advisory['CVEs']), sep =';', file=rhel, flush=True)
print(y, prod, '| total =', len(data), sep = ' ')
rhel.close()


# print('-----')
# # From the list of advisories saved in the previous example (as
# # `kernel_advisories`), get a list of affected products for each advisory.
# endpoint = '/cvrf/'

# for advisory in kernel_advisories:
#     data = get_data(endpoint + advisory + '.json')
#     print(advisory)
#     product_branch = data['cvrfdoc']['product_tree']['branch']
#     for product_branch in data['cvrfdoc']['product_tree']['branch']:
#         if product_branch['type'] == 'Product Family':
#             if type(product_branch['branch']) is dict:
#                 print('-', product_branch['branch']['full_product_name'])
# #            else:
#                print('-', '\n- '.join(pr['full_product_name'] for pr in product_branch['branch']))
                
                
                
                
