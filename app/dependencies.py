# Built-ins
import json
from pathlib import Path

# 3rd party
from fastapi.exceptions import HTTPException

# Init
app_root_path = Path(__file__).resolve()
config_path   = Path(app_root_path, 'config')
default_cache_path = Path(app_root_path, 'cache')

default_paths = {
    "APP_ROOT_PATH": app_root_path,
    "CONFIG_PATH"  : config_path,
    "CACHE_PATH"   : default_cache_path
} 

pathspec = { **default_paths }

config_file = Path( config_path, 'config.json' )
if ( config_file.is_file() ):
    config = json.load( open(config_file) )['paths']
    
    pathspec = { **config }


# Functions
def get_path( alias: str ):
    path = pathspec.get( alias )
    if (path is not None):
        return path

    raise HTTPException(
        status_code=500,
        detail="Invalid path"
    )
