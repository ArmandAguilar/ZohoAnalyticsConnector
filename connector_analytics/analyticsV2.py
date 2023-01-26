import sys
import json
import requests


class zohoConnectV2:

    def __init__(self, srvUrl, tokenToRefresh, clientId, clientSecret):
        self.token = ''
        self.error = ''
        try:
            dict = {}
            dict["client_id"] = clientId
            dict["client_secret"] = clientSecret
            dict["refresh_token"] = tokenToRefresh
            dict["grant_type"] = 'refresh_token'
            req_refresh_token = requests.post(
                srvUrl + '/oauth/v2/token', data=dict)
            json_refrech_token = json.loads(req_refresh_token.text)
            self.token = json_refrech_token['access_token']
        except Exception as err:
            self.error = str(err)

    def addRow(self, srvUrl='', workspace='', view_id='', orgid='', columns={}):
        """
        Add a single row in the specified table.
        @param:srvUrl : URL https://<ZohoAnalytics_Server_URI>/
        @type:str

        @param:workspace
        @type:str
        Sample:510019100001668201911111

        @param:workspace 
        @type:str
        Sample:510019100001668201911111

        @param:columns
        @type:list
        Sample:{"columnName1":"value1","columnName2":"value2"}	Columns JSON object.

        Return {}
        """
        json_return = []
        _CONFIG_ = {}
        try:
            if srvUrl != '' and workspace != '' and view_id != '' and orgid != '' and columns != None:
                if len(columns) >= 1:
                    headers = {'ZANALYTICS-ORGID': orgid,
                               'Authorization': 'Zoho-oauthtoken ' + str(self.token)}
                    _CONFIG_['columns'] = columns
                    # Send The Request
                    URL_API = "{0}/restapi/v2/workspaces/{1}/views/{2}/rows?CONFIG={3}".format(
                        srvUrl, workspace, view_id, json.dumps(_CONFIG_))
                    req_zoho = requests.post(URL_API, headers=headers)
                    json_return.append({'message': req_zoho.text})
                else:
                    json_return.append(
                        {'message': 'Filed columns or critaria has a bad config.'})

        except Exception as err:
            json_return.append({'status': 'Error', 'message': str(err)})
        return json.dumps(json_return)

    def updateRow(self, srvUrl='', workspace='', view_id='', orgid='', criteria='', columns=None, updateAllRows='false'):
        """
        Update rows in the specified table.

        @param:srvUrl : URL https://<ZohoAnalytics_Server_URI>/
        @type:str

        @param:workspace
        @type:str
        Sample:510019100001668201911111

        @param:workspace 
        @type:str
        Sample:510019100001668201911111

        @param:criteria 
        @type:str
        Sample: "\"<table-name>\".\"<column-name>\"='value'"

        @param:columns
        @type:list
        Sample:{"columnName1":"value1","columnName2":"value2"}	Columns JSON object.

        @param: updateAllRows
        @type:str
         true/false
        Return {}
        """
        json_return = []
        _CONFIG_ = {}
        try:
            # Create the config
            if srvUrl != '' and workspace != '' and view_id != '' and orgid != '' and criteria != '' and columns != None:
                if len(columns) >= 1:
                    headers = {'ZANALYTICS-ORGID': orgid,
                               'Authorization': 'Zoho-oauthtoken ' + str(self.token)}
                    _CONFIG_['columns'] = columns
                    _CONFIG_['criteria'] = criteria
                    _CONFIG_['updateAllRows'] = updateAllRows
                    # Send The Request
                    URL_API = "{0}/restapi/v2/workspaces/{1}/views/{2}/rows?CONFIG={3}".format(
                        srvUrl, workspace, view_id, json.dumps(_CONFIG_))
                    req_zoho = requests.put(URL_API, headers=headers)
                    json_return.append({'message': req_zoho.text})
                else:
                    json_return.append(
                        {'message': 'Filed columns or critaria has a bad config.'})
            else:
                json_return.append(
                    {'message': 'I need all params'})
        except Exception as err:
            json_return.append({'message': str(err)})
        return json.dumps(json_return)

    def deleteRow(self, srvUrl='', workspace='', view_id='', orgid='', criteria='', deleteAllRows='false'):
        """
        Delete rows in the specified table.

        @param:srvUrl : URL https://<ZohoAnalytics_Server_URI>/
        @type:str

        @param:workspace
        @type:str
        Sample:510019100001668201911111

        @param:workspace 
        @type:str
        Sample:510019100001668201911111

        @param:criteria 
        @type:str
        Sample: "\"<table-name>\".\"<column-name>\"='value'"

        @param:deleteAllRows
        @type:str
        Sample:true/false	
        To delete all the rows in the table.

        Return {}
        """
        json_return = []
        _CONFIG_ = {}
        try:
            if srvUrl != '' and workspace != '' and view_id != '' and orgid != '' and criteria != '':
                if len(criteria) >= 1:
                    headers = {'ZANALYTICS-ORGID': orgid,
                               'Authorization': 'Zoho-oauthtoken ' + str(self.token)}

                    _CONFIG_['criteria'] = criteria
                    URL_API = "{0}/restapi/v2/workspaces/{1}/views/{2}/rows?CONFIG={3}".format(
                        srvUrl, workspace, view_id, json.dumps(_CONFIG_))

                    req_zoho = requests.delete(URL_API, headers=headers)
                    json_return.append({'message': str(req_zoho.text)})
                else:
                    json_return.append(
                        {'message': 'problems with the citerian param'})
            else:
                json_return.append(
                    {'message': 'Some file can not be empty [srvUrl,workspace,view_id,orgid,criteria ]'})

        except Exception as err:
            json_return.append({'message': str(err)})
        return json.dumps(json_return)

    def importRows(self, srvUrl='', workspace='', view_id='', orgid='', data='', importType='', fileType='csv', autoIdentify='true', matchingColumns=None,
                   selectedColumns=None, thousandSeparator='', dateFormat='', columnDateFormat=None, delimiter='', quoted='', retainColumnNames=''):
        """
        Bulk APIs are used to import bulk data into Zoho Analytics table and also offers APIs 
        to export your tables, reports, dashboards in PDF, Excel, JSON, HTML, Image, and CSV formats.

        @param:srvUrl : URL https://<ZohoAnalytics_Server_URI>/
        @type:str

        @param:workspace 2100191000004922089
        @type:str

        @param:data 
        @type:file or data
        FILE - The file to be imported

        @param: importType The type of import.
        @type:str
        Can be one of
         1. APPEND .- Appends the data into the table.
         2. TRUNCATEADD .- Deletes all exisiting rows in the table and adds the imported data as new entry.
         3. UPDATEADD .- Updates the row if the mentioned column values are matched, else a new entry will be added.

        @param: fileType
        @type:str
         1. csv
         2. json

        @param: autoIdentify
        @type:str
         true/false

        @param: autoIdentify
        @type:str
         abort
         skiprow
         setcolumnempty

        @param: matchingColumns
        @type:list
         (mandatory only when the importType is updateadd)
         Sample:["column1","column2"]

        @param: selectedColumns
        @type:list
        JSON array of column names
        Sample:
        ["column1","column2"]

        @param: skipTop
        @type:number
        Number of rows that are to be skipped from the top in the CSV file being imported.

        @param: thousandSeparator
        @type:str

         0 - COMMA
         1 - DOT
         2 - SPACE
         3 - SINGLE QUOTE

        @param: decimalSeparator
        @type:str
         0 - DOT
         1 - COMMA

        @param: dateFormat
        @type:str
         Format of the date.
         Sample:
         dd-MMM-YYYY

        @param: columnDateFormat
        @type:list
        JSON Object with column name as key and date format as value.
        Sample:
            {"columnName1":"dd-MMM-YYYY","columnName2":"MM/dd/yyyy"}

        @param:delimiter
        @type:str
         Sample 0/1/2/3
         0 - COMMA
         1 - TAB
         2 - SEMICOLON
         3 - SPACE

        @param:quoted
        @type:str
         Sample 0/1/2
          0 - NONE
          1 - SINGLE QUOTE
          2 - DOUBLE QUOTE

        @param:retainColumnNames
        @type:str
         Sample true/false
         true - the final key attribute alone will be considered as column name.
         false - the column name will be constructed by appending all the parent
         attributes separated by dot (.). This will result in column names which captures
         the full JSON tree hierarchy eg., employee.Name, employee.Department

        @return {}
        """
        json_return = []
        _CONFIG_ = {}
        _CONFIG_["importType"] = importType
        _CONFIG_["fileType"] = fileType
        _CONFIG_["autoIdentify"] = autoIdentify
        _CONFIG_["matchingColumns"] = matchingColumns
        _CONFIG_["selectedColumns"] = selectedColumns
        _CONFIG_["thousandSeparator"] = thousandSeparator
        _CONFIG_["dateFormat"] = dateFormat
        _CONFIG_["columnDateFormat"] = columnDateFormat
        try:
            if srvUrl != '' and workspace != '' and view_id != '' and orgid != '':
                headers = {'ZANALYTICS-ORGID': orgid,
                           'Authorization': 'Zoho-oauthtoken ' + str(self.token)}
                # Check the config
                if _CONFIG_["fileType"] == 'csv':
                    # Add especial config
                    _CONFIG_["delimiter"] = delimiter
                    _CONFIG_["quoted"] = quoted
                    if _CONFIG_["delimiter"] != '':
                        # Delete all elements empty
                        _CONFIG_FILTER_ = {}
                        for item in _CONFIG_:
                            if _CONFIG_[item] != '' and _CONFIG_[item] != None and len(_CONFIG_[item]) > 0:
                                _CONFIG_FILTER_[item] = _CONFIG_[item]
                        # Send The Request
                        URL_API = "{0}/restapi/v2/workspaces/{1}/views/{2}/data?CONFIG={3}".format(
                            srvUrl, workspace, view_id, json.dumps(_CONFIG_FILTER_))
                        files = {'FILE': data}
                        req_zoho = requests.post(
                            URL_API, files=files, headers=headers)
                        json_return.append({'message': str(req_zoho.text)})
                elif _CONFIG_["fileType"] == 'json':
                    _CONFIG_['retainColumnNames'] = retainColumnNames
                    # Here make the validation autoIdentify false
                    if autoIdentify == 'false' and retainColumnNames != '':
                        if retainColumnNames == 'true' or retainColumnNames == 'false':
                            pass
                        else:
                            json_return.append(
                                {'message': 'retainColumnNames need be true/false'})
                    elif autoIdentify == 'true' and retainColumnNames == '':
                        # Delete all elements empty
                        _CONFIG_FILTER_ = {}
                        for item in _CONFIG_:
                            if _CONFIG_[item] != '' and _CONFIG_[item] != None and len(_CONFIG_[item]) > 0:
                                _CONFIG_FILTER_[item] = _CONFIG_[item]
                        # Send The Request
                        URL_API = "{0}/restapi/v2/workspaces/{1}/views/{2}/data?CONFIG={3}".format(
                            srvUrl, workspace, view_id, json.dumps(_CONFIG_FILTER_))
                        files = {'FILE': data}
                        req_zoho = requests.post(
                            URL_API, files=files, headers=headers)
                        json_return.append({'message': req_zoho.text})
                    else:
                        json_return.append(
                            {'message': 'autoIdentify need be true/false'})
                else:
                    json_return.append(
                        {'message': 'Only support CVS and JSON files'})
            else:
                json_return.append(
                    {'message': 'This param can not be empty [srvUrl,workspace,view_id,orgid]'})
        except Exception as err:
            return json_return.append({'message': str(err)})
        return json.dumps(json_return)
    
    def zohoQuery(self, srvUrl='',orgid='', workspace='', table_name='',email='', sql_query=''):
        """
        Zoho Analytics has implemented the Zoho CloudSQL technology 
        as an extension to its HTTP Web API. Using the HTTP API, users
        can query Zoho Analytics Workspace by providing the SQL queries.

        @param:srvUrl : URL https://<ZohoAnalytics_Server_URI>/
        @type:str

        @param:workspace 2100191000004922089
        @type:str

        @param:email some@domain.com
        @type:str

        @param:table_name users
        @type:str

        @param: sql_query
        @type:str

        """
        json_return = []
        try:
            if srvUrl != '' and workspace != '' and sql_query != '':
                # Send The Request

                headers = {'ZANALYTICS-ORGID': orgid,
                           'Authorization': 'Zoho-oauthtoken ' + str(self.token)}

                URL_API_V2 ="{0}/api/{1}/{2}/{3}?ZOHO_ACTION=EXPORT&ZOHO_OUTPUT_FORMAT=JSON&ZOHO_ERROR_FORMAT=JSON&ZOHO_API_VERSION=1.0&ZOHO_SQLQUERY={4}".format(
                    srvUrl,
                    email,
                    workspace,
                    table_name,
                    sql_query)

                req_zoho = requests.get(URL_API_V2,  headers=headers)
                json_return = json.loads(req_zoho.text)

            else:
                json_return = {'error':'check the params of def we need all..'}
        except Exception as err:
            return json_return.append({'message': str(err)})
        return json_return
