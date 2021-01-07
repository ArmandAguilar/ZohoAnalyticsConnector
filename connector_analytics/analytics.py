import sys
import json
import requests

class zohoConnect:

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

    def addRow(self, tableURL, columnsValues=None, Conf=None):
        """
        Adds a row to the specified table identified by the URI.

        @param tableURL: The URL of the table. See U{https://<ZohoAnalytics_Server_URI>/api/<OwnerEmail>/<WorkspaceName>/<TableName>}.
        @type tableURL:string

        @param columnValues: Contains the values for the row <key:value>.
        @type columnValues:dictionary

        @param config: Contains any additional control parameters. Can be {None}.
        @type config:dictionary

        @return: The values of the row.
        @rtype:dictionary

        """
        json_return = []
        try:
            if columnsValues != None or len(columnsValue) > 0:
                if Conf == None:    
                    Conf = {}
                    Conf['ZOHO_ACTION'] = 'ADDROW'
                    Conf['ZOHO_OUTPUT_FORMAT']=  'JSON',
                    Conf['ZOHO_ERROR_FORMAT']= 'JSON',
                    Conf['ZOHO_API_VERSION'] = '1.0',

                    if columnsValues != None:
                        Conf = dict(Conf, **columnsValues)
                headers = {'Authorization': 'Zoho-oauthtoken ' + str(self.token)}
                req_zoho = requests.post(tableURL, data=Conf, headers=headers)
            
                if int(req_zoho.status_code) != 200:
                    json_return.append({'status': 'Error', 'message': json.loads(req_zoho.text)})
                else:
                    json_return.append({'status': 'Oka', 'message': json.loads(req_zoho.text)})
            else:
                json_return.append({'status': 'Error', 'message': 'columnsValues is empty'})

        except Exception as err:
            json_return.append({'status': 'Error', 'message': str(err)})
        return json.dumps(json_return)

    def updateRow(self, tableURL, updateInfo=None, conditionalInfo=None, Conf=None):
        """
        Update a row to the specified table identified by the URI.

        @param tableURL: The URL of the table. See U{https://<ZohoAnalytics_Server_URI>/api/<OwnerEmail>/<WorkspaceName>/<TableName>}.
        @type tableURL:string

        @param updateInfo: Contains the values for the row of update <key:value>.
        @type updateInfo:dictionary

        @param conditionalInfo: If that parameter is not sent, then all the rows are updated. If criteria is sent the rows matching the criteria alone are updated [user_id=xxx].
        @type conditionalInfo:string

        @param config: Contains any additional control parameters. Can be {None}.
        @type config:dictionary

        @return: The values of the row.
        @rtype:dictionary

        """
        json_return = []
        try:
            if updateInfo != None:
                if Conf == None:
                    Conf = {}
                    Conf['ZOHO_ACTION'] = 'UPDATE'
                    Conf['ZOHO_OUTPUT_FORMAT'] = 'JSON',
                    Conf['ZOHO_ERROR_FORMAT'] = 'JSON',
                    Conf['ZOHO_API_VERSION'] = '1.0',

                    Conf = dict(Conf, **updateInfo)

                    if conditionalInfo != None:
                        Conf['ZOHO_CRITERIA'] = conditionalInfo
                
                headers = {'Authorization': 'Zoho-oauthtoken ' + str(self.token)}
                req_zoho = requests.post(tableURL, data=Conf, headers=headers)

                if int(req_zoho.status_code) != 200:
                    json_return.append(
                        {'status': 'Error', 'message': json.loads(req_zoho.text)})
                else:
                    json_return.append(
                        {'status': 'Oka', 'message': json.loads(req_zoho.text)})
            else:
                json_return.append(
                    {'status': 'Error', 'message': 'columnsValues is empty'})

        except Exception as err:
            json_return.append({'status': 'Error', 'message': str(err)})
        return json.dumps(json_return)

    def deleteRow(self, tableURL, conditionalInfo=None, Conf=None):
        """
        Update a row to the specified table identified by the URI.

        @param tableURL: The URL of the table. See U{https://<ZohoAnalytics_Server_URI>/api/<OwnerEmail>/<WorkspaceName>/<TableName>}.
        @type tableURL:string

        @param conditionalInfo: If that parameter is not sent, then all the rows are deleted. If criteria is sent the rows matching the criteria alone are deleted [user_id=xxx].
        @type conditionalInfo:string

        @param config: Contains any additional control parameters. Can be {None}.
        @type config:dictionary

        @return: The values of the row.
        @rtype:dictionary

        """
        json_return = []
        try:
            if conditionalInfo != None:
                if Conf == None:
                    Conf = {}
                    Conf['ZOHO_ACTION'] = 'DELETE'
                    Conf['ZOHO_OUTPUT_FORMAT'] = 'JSON',
                    Conf['ZOHO_ERROR_FORMAT'] = 'JSON',
                    Conf['ZOHO_API_VERSION'] = '1.0',
                    Conf['ZOHO_CRITERIA'] = conditionalInfo
                        
                
                headers = {'Authorization': 'Zoho-oauthtoken ' + str(self.token)}
                req_zoho = requests.post(tableURL, data=Conf, headers=headers)

                if int(req_zoho.status_code) != 200:
                    json_return.append(
                        {'status': 'Error', 'message': json.loads(req_zoho.text)})
                else:
                    json_return.append(
                        {'status': 'Oka', 'message': json.loads(req_zoho.text)})
            else:
                json_return.append(
                    {'status': 'Error', 'message': 'conditionalInfo is empty'})

        except Exception as err:
            json_return.append({'status': 'Error', 'message': str(err)})
        return json.dumps(json_return)


    def ImportRows(self, tableURL, importType, importData, Identify="TRUE", Delimiter=0, Quoted=0, Columns='', Conf=None):
        """
        Import cvs into a tabla of zoho analitycs.
        @param tableURL: The URI of the table. See U{https://<ZohoAnalytics_Server_URI>/api/<OwnerEmail>/<WorkspaceName>/<TableName>}.
        @type tableURL:string

        @param importType: The type of import.
        Can be one of
         1. APPEND
         2. TRUNCATEADD
         3. UPDATEADD
        @type importType:string
        See U{Import types<https://www.zoho.com/analytics/api/#import-data>} for more details.

        @param Delimiter
        @type Delimiter:int
        Can be one of
        0 - if the delimiter is COMMA
        1 - if the delimiter is TAB
        2 - if the delimiter is SEMICOLON
        3 - if the delimiter is SPACE

        @param Quoted
        @type Quoted:int
        Can be one of
        The Text Qualifier.
        0 - None
        1 - SINGLE QUOTE
        2 - DOUBLE QUOTE

        @param Columns: Names filed separate by coma for the key. 
        @type Columns:string


        @param importData: The data in csv format include firts column like names' filed.
        @type importData:string

        @param Identify: Used to specify whether to auto identify the CSV format [True or False].
        @type Identify:string

        @param Conf: Contains any additional control parameters.
        @type Confnfig:dictionary
        See U{Import types<https://www.zoho.com/analytics/api/#import-data>} for more details.
        
        @return: {}
        """
        json_return = [] 
        try:

            if (Conf == None):
                Conf = {}
                Conf['ZOHO_ACTION'] = 'IMPORT'
                Conf['ZOHO_OUTPUT_FORMAT'] = 'JSON',
                Conf['ZOHO_ERROR_FORMAT'] = 'JSON',
                Conf['ZOHO_IMPORT_TYPE'] = importType
                Conf['ZOHO_API_VERSION'] = '1.0',
                Conf['ZOHO_ON_IMPORT_ERROR'] = 'ABORT'
                Conf['ZOHO_AUTO_IDENTIFY'] = Identify
                Conf['ZOHO_IMPORT_DATA'] = importData
                Conf['ZOHO_DELIMITER'] = Delimiter
                Conf['ZOHO_QUOTED'] = Quoted

                if importType.upper() == 'UPDATEADD':
                    if Columns != '':
                        Conf['ZOHO_MATCHING_COLUMNS'] = Columns
                    else:
                        json_return.append(
                            {'status': 'Error', 
                            'message': 'Specify the columns to be imported into the Zoho Analytics table from the data being uploaded'})

            if not ("ZOHO_CREATE_TABLE" in Conf):
                Conf["ZOHO_CREATE_TABLE"] = 'false'

            headers = {'Authorization': 'Zoho-oauthtoken ' + str(self.token)}
            req_zoho = requests.post(
                tableURL, data=Conf, headers=headers)

            if int(req_zoho.status_code) != 200:
                json_return.append({'status':'Error', 'message':json.loads(req_zoho.text)})
            else:
                json_return.append({'status':'Oka', 'message':json.loads(req_zoho.text)})

        except Exception as err:
            return json_return.append({'status':'Error', 'message':str(err)})
        return json.dumps(json_return)
    
    def readData(self,tableURL,criteria=None):
        """
        @param tableURL: The URI of the table. See U{https://<ZohoAnalytics_Server_URI>/api/<OwnerEmail>/<WorkspaceName>/<TableName>}.
        @type tableURL:string

        @param criteria: Used to make match example Id='1'.
        @type criteria:string

        @return: {}
        """
        json_return = []
        try:
            Conf = {}
            Conf['ZOHO_ACTION'] = 'EXPORT'
            Conf['ZOHO_OUTPUT_FORMAT'] = 'JSON',
            Conf['ZOHO_ERROR_FORMAT'] = 'JSON',
            Conf['ZOHO_ON_IMPORT_ERROR'] = 'ABORT'
            Conf['ZOHO_API_VERSION'] = '1.0'
            
            if criteria != None:
                Conf['ZOHO_CRITERIA'] = criteria
            else:
                json_return.append({'status': 'Error', 'message': str(err)})
                
            headers = {'Authorization': 'Zoho-oauthtoken ' + str(self.token)}
            req_zoho = requests.post(tableURL, data=Conf, headers=headers)

            if int(req_zoho.status_code) != 200:
                json_return.append(
                    {'status': 'Error', 'message': json.loads(req_zoho.text)})
            else:
                json_return.append({'status': 'Oka', 'message': json.loads(req_zoho.text)})

        except Exception as err:
            return json_return.append({'status': 'Error', 'message': str(err)})
        return json.dumps(json_return)


    def readQuery(self, tableURL, queryStr=None):
        """
        @param tableURL: The URI of the table. See U{https://<ZohoAnalytics_Server_URI>/api/<OwnerEmail>/<WorkspaceName>/<TableName>}.
        @type tableURL:string

        @param queryStr: Simple SQL.
        @type queryStr:string

        @return: {JSON}
        """
        json_return = []
        try:
            Conf = {}
            Conf['ZOHO_ACTION'] = 'EXPORT'
            Conf['ZOHO_OUTPUT_FORMAT'] = 'JSON',
            Conf['ZOHO_VALID_JSON'] = 'true',
            Conf['KEY_VALUE_FORMAT'] = 'true',
            Conf['ZOHO_ERROR_FORMAT'] = 'JSON',
            Conf['ZOHO_ON_IMPORT_ERROR'] = 'ABORT'
            Conf['ZOHO_API_VERSION'] = '1.0'
            
            if queryStr != None:
                Conf['ZOHO_SQLQUERY'] = queryStr
                headers = {'Authorization': 'Zoho-oauthtoken ' + str(self.token)}
                req_zoho = requests.post(tableURL, data=Conf, headers=headers)

                if int(req_zoho.status_code) != 200:
                    json_return.append(
                        {'status': 'Error', 'message': json.loads(req_zoho.text)})
                else:
                    dt = json.loads(req_zoho.text)
                    json_return = dt
            else:
                json_return.append({'status': 'Error', 'message': 'query cannot be empty'})

        except Exception as err:
            return json_return.append({'status': 'Error', 'message': str(err)})
        return json_return

