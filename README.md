# Zoho AnalyticsConnector
[![Supported Versions](https://img.shields.io/pypi/pyversions/requests.svg)]()

## Authentication

Zoho Analytics REST API supports OAuth 2.0 protocol to authorize and authenticate API calls. Follow the steps listed here to use OAuth 2.0 protocol in Zoho Analytics APIs.

- **Step 1:** [Registering New Client](https://www.zoho.com/analytics/api/#registering-new-client)
- **Step 2:** [Generating Code](https://www.zoho.com/analytics/api/#generating-grant-token)
- **Step 3:** [Generating Refresh Token](https://www.zoho.com/analytics/api/#generating-refresh-token)
- **Step 4:** [Generating Access Token](https://www.zoho.com/analytics/api/#generating-access-token)

<b>The scope for full access</b>

    ZohoAnalytics.fullaccess.all

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
	SERVERURL = 'https://analyticsapi.zoho.com/api/user@domain.com'
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

### CVS File

|ID|Name  |Country |
|-|-|-|
|1|User 1|MX|
|2|User 2|CAD|
|3|User 3|UK|
|4|User 4|USA|
|  |  |


```python
with open('files.csv', 'r') as f:
	data = f.read()
	autoIdentify = "true"
	onError = "ABORT"
```

### Add rows
```python
objZoho.importData(tableURL= Config.SERVERURL,
						importType='APPEND',
						importData=data, Identify=False)
