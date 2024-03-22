from typing import Any, Dict

from airflow.models import BaseOperator
from airflow.utils.context import Context

from triggers.file_trigger import FileTrigger


class FileSensorAsync(BaseOperator):

    def __init__(self, *, filepath, fs_conn_id="fs_default", recursive=False, poll_interval: float = 5.0, **kwargs):
        self.filepath = filepath
        self.fs_conn_id = fs_conn_id
        self.recursive = recursive
        self.poll_interval = poll_interval
        super().__init__(**kwargs)

    def execute(self, context: Context) -> Any:
        self.defer(trigger=FileTrigger(self.filepath,
                                       self.fs_conn_id,
                                       self.recursive,
                                       self.poll_interval),
                   method_name="execute_complete")

    def execute_complete(self, context: Context, event: Dict[str, Any]):
        print(event)
        return event
