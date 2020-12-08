from .utils import get_project_root  # pathlib is seriously awesome!

DATA_DIR = get_project_root() / "data"
CENSUS_DATA_PATH = DATA_DIR / "raw" / "census_2018.csv"
ESI_DATA_PATH = DATA_DIR / "raw" / "esi_2018.csv"