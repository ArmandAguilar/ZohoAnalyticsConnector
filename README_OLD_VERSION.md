# Zoho Analytics Connector
[![Supported Versions](https://img.shields.io/pypi/pyversions/requests.svg)]()
[![License](https://img.shields.io/npm/l/express.svg)]()

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
from connector_analytics.analytics import zohoConnect
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

objZoho = zohoConnect(srvUrl=Config.SERVERAUTH,
					tokenToRefresh=Config.REFRESHTOKEN,
					clientId=Config.CLIENTID,
					clientSecret=Config.CLIENTSECRET)

```
## Add Row

```python

payload = {
	'Id':'1',
	'Name':'Armando Aguilar',
	'Cell':'52-55555-555',
	'Country':'CDMEX'}
	
objZoho.addRow(tableURL=Config.SERVERURL,columnsValues=payload)

```

## Update Row

```python

conditional = 'Id=1'

payload = {
	'Name':'Armando Aguilar L.',
	'Cell':'52-895578-6789',
	'Country':'UK'}

update = objZoho.updateRow(tableURL=Config.SERVERURL,
						updateInfo=payload,
						conditionalInfo=conditional)

```

## Delete row
```python

conditional = 'Id=1'
delete = objZoho.deleteRow(tableURL=Config.SERVERURL,
							conditionalInfo=conditional)

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

|ID|Name  |Country |
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

objZoho.ImportRows(tableURL= Config.SERVERURL,
					importType='APPEND',
					importData=data, Identify=False)

```

### Update rows
Updates the row if the mentioned column values are matched, else a new entry will be added.

**Tip** : Columns is the criterian for make the MATCHING, it can be one or more values separate by coma.
```python

objZoho.ImportRows(tableURL=Config.SERVERURL, 
                    importType='UPDATEADD',
                    importData=data,
                    Identify=False,
                    Columns='Id')

```

### Truncateadd rows
Deletes all exisiting rows in the table and adds the imported data as new entry.
```python

objZoho.ImportRows(tableURL=Config.SERVERURL,
                importType='TRUNCATEADD',
                importData=data)

```

## Read Data

<p>&nbsp;</p>

### Criteria field
The criteria field is the way to make match in the table.

```python

conditional = 'Id=1'

objZoho.readData(tableURL=Config.SERVERURL,criteria=conditional)

```

### SQL RUN
Literal SQL Query can be used as criteria.Export using joining tables and specific columns can be done using.

```python

sql_query = 'SELECT \"Id\",\"Name\" FROM users Where  \"Id\" = \'1\''

objZoho.readQuery(tableURL=Config.SERVERURL,queryStr=sql_query)

```

## 🍺 Buy me a beer

|BTC|LTC|
|--|--|
|<img src="http://armando-aguilar.com/wp-content/uploads/2022/07/wallet_btc.png" width="150">|<img src="http://armando-aguilar.com/wp-content/uploads/2022/07/wallet_ltc.png" width="150">|
|1JDA4DEkVnB9rvLgLD5Xe9jfU2pJtnCZiG|LhBrMcs7i3mD2wjiUv3KGtx9eEQeyBE4Dg|

<p>&nbsp;</p>


