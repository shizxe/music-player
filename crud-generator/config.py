# from pathlib import Path

# PROJECT_ROOT = Path(__file__).resolve().parent.parent
# TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"
# APP_DIR = PROJECT_ROOT / "app"
# MIGRATIONS_DIR = PROJECT_ROOT / "database" / "migrations"
# PROVIDERS_FILE = APP_DIR / "Providers" / "RepositoryServiceProvider.php"
# BOOTSTRAP_PROVIDERS_FILE = PROJECT_ROOT / "bootstrap" / "providers.php"
# BOOTSTRAP_APP_FILE = PROJECT_ROOT / "bootstrap" / "app.php"
# ROUTES_API_FILE = PROJECT_ROOT / "routes" / "api.php"


from pathlib import Path

# Adjust PROJECT_ROOT to include the 'src' directory where Laravel resides
PROJECT_ROOT = Path(__file__).resolve().parent.parent / "src"

TEMPLATES_DIR = Path(__file__).resolve().parent / "templates"
APP_DIR = PROJECT_ROOT / "app"
MIGRATIONS_DIR = PROJECT_ROOT / "database" / "migrations"
PROVIDERS_FILE = APP_DIR / "Providers" / "RepositoryServiceProvider.php"
BOOTSTRAP_PROVIDERS_FILE = PROJECT_ROOT / "bootstrap" / "providers.php"
BOOTSTRAP_APP_FILE = PROJECT_ROOT / "bootstrap" / "app.php"
ROUTES_API_FILE = PROJECT_ROOT / "routes" / "api.php"