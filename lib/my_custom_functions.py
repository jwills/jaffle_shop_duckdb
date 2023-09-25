from duckdb import DuckDBPyConnection

from dbt.adapters.duckdb.plugins import BasePlugin
from dbt.adapters.duckdb.utils import TargetConfig


def foo() -> int:
    return 1729


# The python module that you create must have a class named "Plugin"
# which extends the `dbt.adapters.duckdb.plugins.BasePlugin` class.
class Plugin(BasePlugin):
    def configure_connection(self, conn: DuckDBPyConnection):
        conn.create_function("foo", foo)
