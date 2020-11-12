import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    #BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'ENTER_STORAGE_ACCOUNT_NAME'
    #BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'ENTER_BLOB_STORAGE_KEY'
    #BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'ENTER_IMAGES_CONTAINER_NAME'
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'ttnstorageacct'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'R6mN9tjDLoGHRCWHw/GP7ODWtMNn3+voTDU8x/JdC912VNrHU44eJVue8fgc/iwLsmEYzZ4HgPkEN3LLma+4+g=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'ttnstoragecontainer'

    #SQL_SERVER = os.environ.get('SQL_SERVER') or 'ENTER_SQL_SERVER_NAME.database.windows.net'
    #SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'ENTER_SQL_DB_NAME'
    #SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'ENTER_SQL_SERVER_USERNAME'
    #SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'ENTER_SQL_SERVER_PASSWORD'
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'databasesqlwestttn.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'database-west'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'ttndbadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'admin123!'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    #SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    #CLIENT_SECRET = "ENTER_CLIENT_SECRET_HERE"
    CLIENT_SECRET = "BzD.2qT.~7NIdX-fNaO5_D-3c3O1OVLq5N" 
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    #CLIENT_ID = "ENTER_CLIENT_ID_HERE"
    CLIENT_ID = "0a0155a2-9fb7-4ec1-9550-1aeca04250a0"

    #REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD
    REDIRECT_PATH = "/ttnRedirectURIGetToken"

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session