# Zoho Analytics Connector v2
[![Supported Versions](https://img.shields.io/pypi/pyversions/requests.svg)]()
[![License](https://img.shields.io/npm/l/express.svg)]()

[Old version](README_OLD_VERSION.md)

## Install

```python
pip install requests
pip install sphinx
pip install .
```

## Authentication

Zoho Analytics REST API supports OAuth 2.0 protocol to authorize and authenticate API calls. Follow the steps listed here to use OAuth 2.0 protocol in Zoho Analytics APIs.

- **Step 1:** [Registering New Client](https://www.zoho.com/analytics/api/#registering-new-client)
- **Step 2:** [Generating Code](https://www.zoho.com/analytics/api/#generating-grant-token)
- **Step 3:** [Generating Refresh Token](https://www.zoho.com/analytics/api/#generating-refresh-token)
- **Step 4:** [Generating Access Token](https://www.zoho.com/analytics/api/#generating-access-token)

<b>The scope for full access</b>

    ZohoAnalytics.fullaccess.all

## Import

```python
from connector_analytics.analyticsV2 import zohoConnectV2
```

## Config File

```python
class Config:
    SERVERAUTH = ''
    SERVERURL = ''
    LOGINEMAILID = ''
    CLIENTID = ''
    CLIENTSECRET = ''
    REFRESHTOKEN = ''
```
<p>&nbsp;</p>

| Data Centre         | ZohoAnalytics_Server_URI | ZohoAccounts_Server_URI |
|---------------------|--------------------------|-------------------------|
| US  (United States) |   analyticsapi.zoho.com  |    accounts.zoho.com    |
|     EU  (Europe)    |   analyticsapi.zoho.eu   |     accounts.zoho.eu    |
|     IN  (India)     |   analyticsapi.zoho.in   |     accounts.zoho.in    |
|   AU  (Australia)   | analyticsapi.zoho.com.au |   accounts.zoho.com.au  |
|     CN  (China)     | analyticsapi.zoho.com.cn |   accounts.zoho.com.cn  |

<p>&nbsp;</p>

**Example for Config.py**

```python

class  Config:
	SERVERAUTH = 'https://accounts.zoho.com'
	SERVERURL = 'https://analyticsapi.zoho.com/api/user@domain.com/table'
	LOGINEMAILID = 'user@domain.com'
	CLIENTID = '******'
	CLIENTSECRET = '******'
	REFRESHTOKEN = '******'
	
```

## Initialize Zoho Object

```python
        
objZoho = zohoConnectV2(srvUrl=Config.SERVERAUTH,
					tokenToRefresh=Config.REFRESHTOKEN,
					clientId=Config.CLIENTID,
					clientSecret=Config.CLIENTSECRET)

```
## Add Row

**Tip** : Where are workspace and view_id ? check the url of your table
https://analytics.zoho.com/workspace/<workspace_id>/view/<view_id>
orgid is the organization id check you setting in zoho

```python

columns = {
	'Id':'1',
	'Name':'Armando Aguilar',
	'Cell':'52-55555-555',
	'Country':'CDMEX'}
	
url = 'https://analyticsapi.zoho.com'
objZoho.addRow(srvUrl=url,
                    workspace='51001910',
                    view_id='5100191000',
                    orgid='99999',
                    columns=columns)

```

## Update Row

**Tip** : Where are workspace and view_id ? check the url of your table
https://analytics.zoho.com/workspace/<workspace_id>/view/<view_id>
orgid is the organization id check you setting in zoho

```python

criteria = '\"users\".\"Id\"=\'1\''

columns = {
    'Cell':'52-6666-666',
	'Country':'California'
}

update = objZoho.updateRow(srvUrl='https://analyticsapi.zoho.com',
                         workspace='3100191',
                         view_id='310019',
                         orgid='5987',
                         criteria=criteria,
                         columns=columns)

```

## Delete row
**Tip** : Where are workspace and view_id ? check the url of your table
https://analytics.zoho.com/workspace/<workspace_id>/view/<view_id>
orgid is the organization id check you setting in zoho
```python

criteria = '"users"."Id"=4'
delete = objZoho2.deleteRow(srvUrl='https://analyticsapi.zoho.com',
                         workspace='3100191,
                         view_id='310019',
                         orgid='5987',
                         criteria=criteria,
                         deleteAllRows='true')

```
<p>&nbsp;</p>

## Work with multiple rows
<p>&nbsp;</p>

### CVS File
Use a simple cvs or format in a string to insert rows in the table of zoho in this example we used this files called users.cvs.

- **APPEND** Appends the data into the table.
- **TRUNCATEADD** - Deletes all exisiting rows in the table and adds the imported data as new entry.
- **UPDATEADD** Updates the row if the mentioned column values are matched, else a new entry will be added.
<p>&nbsp;</p>

|Id|Name  |Country |
|-|-|-|
|1|User 1|MX|
|2|User 2|CAD|
|3|User 3|UK|
|4|User 4|USA|
|  |  |

<p>&nbsp;</p>

```python

with open('users.csv', 'r') as f:
	data = f.read()
	autoIdentify = "true"
	onError = "ABORT"

```

### Add rows
APPEND Appends the data into the table.

**Tip**: ImportRows can be data of real csv file or string with the format cvs.

```python

objZoho.importRows(srvUrl='https://analyticsapi.zoho.com',
    workspace='4100191',
    view_id='4100191000', 
    data=data, 
    importType='APPEND', 
    orgid='897665555',
    autoIdentify='true',
    delimiter='1')

```

### Update rows


**Tip** : matchingColumns is the criterian for make the MATCHING, it can be one or more values separate by coma.
```python

columns = {'id','Name','Country'}
objZoho.importRows(srvUrl='https://analyticsapi.zoho.com',
    workspace='4100191',
    view_id='4100191000', 
    data=data, 
    importType='UPDATEADD', 
    orgid='897665555',
    autoIdentify='true',
    matchingColumns=columns)

```

### Truncat rows

```python

objZoho.importRows(srvUrl='https://analyticsapi.zoho.com',
    workspace='4100191',
    view_id='4100191000', 
    data=data, 
    importType='TRUNCATEADD', 
    orgid='897665555',
    autoIdentify='true')

```

## SQL IN  ANALYTICS ZOHO

**Tip** : When you write the sentences SQL you need add %20 in the blank spaces.

```python

sql_query = "SELECT%20id,name,country%20FROM%20dusers%20WHERE%20country='MX'"
data = objZoho.zohoQuery(srvUrl='https://analyticsapi.zoho.com',
                                                orgid='000000', 
                                                workspace='workspace name', 
                                                table_name='users',
                                                email='user@domain.com', 
                                                sql_query=sql_query)

```

## 🍺 Buy me a beer

|BTC|LTC|
|--|--|
|<img src="http://armando-aguilar.com/wp-content/uploads/2022/07/wallet_btc.png" width="150">|<img src="http://armando-aguilar.com/wp-content/uploads/2022/07/wallet_ltc.png" width="150">|
|1JDA4DEkVnB9rvLgLD5Xe9jfU2pJtnCZiG|LhBrMcs7i3mD2wjiUv3KGtx9eEQeyBE4Dg|

<p>&nbsp;</p>


