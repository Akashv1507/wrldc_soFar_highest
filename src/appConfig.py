import pandas as pd 

def getAppConfigDict(sheetName:str)->dict:
    """returns dictionary that contains appConfiguration
    Returns:
        dict: dictionary containing app configuration.
    """    
   
    # file path of config excel
    configFilePath = "config.xlsx"

    # for app config
    if sheetName == 'appConfig':
        # get the config excel into a df
        configDf = pd.read_excel(configFilePath, header=None, sheet_name=sheetName)
        # make the first column as index
        configDf.set_index(configDf.columns[0], inplace=True)
        # convert the first column into a series and then to a dictionary
        # now we have a dictionary that has config key as key and config value as value
        configDict = configDf[configDf.columns[0]].to_dict()
        # return the config value based on it key from the config dictionary
        return configDict
    # for scada and psp config, return list of dictionary
    else:
        # get the config excel into a df
        configDf = pd.read_excel(configFilePath, sheet_name=sheetName)
        metricList= configDf.to_dict('records')
        return metricList

    
