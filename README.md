# Capital One IP Informer
Let webtraffic intelligently inform you about your next market move.

## Description
The main idea behind IP Informer is to make it easy for mergents to combine their Capital One transaction information with their webtraffic.
By finding an area where webtraffic is high but sales are lacking it will make targeted advertizing high effective and new lead generation more economically.


## Strutuce of the Project
I have broken the project up in Django services allowing easy import and upkeep of data.


## End User Setup for their Site
1. User adds a single decorator to their existing Django views
```
@record_ip
def index_view(request):
  pass
```
The dectorator tracks uses are they access the site. Note: The record_ip only logs ips initally. Services will batch the reverse lookup later so enduser has no descease in access speed


## General Data Gathering
I pull data from several sources. They are outlined below:
1. Transactions and Merchants from your history are pulled from Capital Ones API's. This is done with the ```merchants``` service. (Additionally, I generated demo merchant relationships.)
2. Each merchant from your transactions is reverse looked up using latitude and longitude to determine the FIPS county code. This is done with the ```gather_fips``` service
3. Once each merchant is mapped to a FIP additional FIBS data is added from US Census data. This is done with the ```gather_fips_data``` service

## ML and Anylistis (all the fun stuff!)
I use two main techniques to identify potential market leads and marketing targets: dbscan clustering and multi. variable nearest neighboors. Additionally, I leverage MatterMark for local companies once cluster locations are determined. Below is a walk through of the data flow:

1. Transactions and Traffic is difference based on linear distance computed from latitude and longitude
2. Points are plotted and clustered.
3. Clusters are scored in terms of similarity to the merchants past transactions demographics based on FIBS data
4. Highly rated clusters are displayed and use can select of their choice.
5. Companies in the cluster area with similar tags to the merchants past transactions are gathered from MatterMark along with proper information for contact and promotion.

## List of services with a brief description

### Demo Seeding Services
core_merchant
generate_traffic
generate_transactions
scatter_merchants
scatter_traffic


### Production/Batch Services
merchants
compute_fib_scores
gather_fips
gather_fips_data
mattermark
sync_transactions







