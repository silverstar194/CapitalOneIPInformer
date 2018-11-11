# Capital One IP Informer
Let web traffic  intelligently inform you about your next market move.

## Description
The main idea behind IP Informer is to make it easy for merchants to combine their Capital One transaction information with their web traffic .
By finding an area where web traffic  is high but sales are lacking it will make targeted advertising high effective and new lead generation more economically.


## Structure  of the Project
I have broken the project up in Django services allowing easy import and upkeep of data.


## End User Setup for their Site
1. User adds a single decorator to their existing Django views
```
@record_ip
def index_view(request):
  pass
```
The decorator  tracks uses are they access the site. Note: The record_ip only logs ips initially. Services will batch the reverse lookup later so ensures has no decease in web site speed.


## General Data Gathering
I pull data from several sources. They are outlined below:
1. Transactions and Merchants from your history are pulled from Capital Ones API's. This is done with the ```merchants``` service. (Additionally, I generated demo merchant relationships.)
2. Each merchant from your transactions is reverse looked up using latitude and longitude to determine the FIPS county code. This is done with the ```gather_fips``` service
3. Once each merchant is mapped to a FIP additional FIBS data is added from US Census data. This is done with the ```gather_fips_data``` service

## ML and Analysis (all the fun stuff!)
I use two main techniques to identify potential market leads and marketing targets: dbscan clustering and multi. variable nearest neighbors. Additionally, I leverage MatterMark for local companies once cluster locations are determined. Below is a walk through of the data flow:

1. Transactions and Traffic is difference based on linear distance computed from latitude and longitude
2. Points are plotted and clustered.
3. Clusters are scored in terms of similarity to the merchants past transactions demographics based on FIBS data
4. Highly rated clusters are displayed and use can select of their choice.
5. Companies in the cluster area with similar tags to the merchants past transactions are gathered from MatterMark along with proper information for contact and promotion.

## List of services with a brief description

### Production/Batch Services

```merchants```

Pulls all merchants associated with your account from Capital One and into the local database.

```compute_fib_scores```

Computes a score for how close a FIB is to the market demographics of your past transactions. Does so through normalization and a linear combination.

```gather_fips```

Maps latitudes and longitudes to FIBS. This is done so it can be used with US Census data.

```gather_fips_data```

Imports and maps US Census data to each FIB in local database.

```mattermark```

Runs FIBS and tags through MatterMark to gather related businesses in the cluster area.


### Demo Seeding Services

```core_merchant```

Sets up the main account. This is what an ensusers  account would look like.

```generate_traffic```

I don't have a long time to monitor people visiting a site so I simulated some traffic.

```generate_transactions```

Wanted more transactions then could pull from API. I simulated some as well.

```sync_transactions```

Creates traffic for each transaction as the people must have had a traffic record when they checked out.

```scatter_merchants```

Merchants tended to be within a very small radius. I provide some variation to the dataset I scattered them out.

```scatter_traffic```

Initial traffic was too tightly bound. I added more variation.





