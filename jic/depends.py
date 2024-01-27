async def common_download_parameters(key: str = None, year: int = 2023):
    """
    
    A function to get the common download parameters.
    
    """
    return {"key": key, "year": year}

async def dashboard_key_parameter(key: str = None):
    """
    
    A function to get the dashboard key parameter.
    
    """
    return key