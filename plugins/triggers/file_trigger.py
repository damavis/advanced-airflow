import asyncio
import datetime
import os
from glob import glob
from typing import Any, AsyncIterator, Tuple, Dict

from airflow.hooks.filesystem import FSHook
from airflow.triggers.base import BaseTrigger, TriggerEvent


class FileTrigger(BaseTrigger):

    def __init__(self, filepath, fs_conn_id="fs_default", recursive=False, poll_interval: float = 5.0):
        self.filepath = filepath
        self.fs_conn_id = fs_conn_id
        self.recursive = recursive
        self.poll_interval = poll_interval
        super().__init__()

    def serialize(self) -> Tuple[str, Dict[str, Any]]:
        return ("triggers.file_trigger.FileTrigger",
                {
                    "filepath": self.filepath,
                    "fs_conn_id": self.fs_conn_id,
                    "recursive": self.recursive,
                    "poll_interval": self.poll_interval
                })

    async def run(self) -> AsyncIterator["TriggerEvent"]:
        hook = FSHook(self.fs_conn_id)
        basepath = hook.get_path()
        full_path = os.path.join(basepath, self.filepath)

        while True:
            for path in glob(full_path, recursive=self.recursive):
                if os.path.isfile(path):
                    mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y%m%d%H%M%S")
                    self.log.info("Triggerer: Found File %s last modified: %s", str(path), mod_time)
                    yield TriggerEvent({"path": path})

                for _, _, files in os.walk(path):
                    if len(files) > 0:
                        self.log.info("Triggerer: Found Files in %s ", str(path))
                        yield TriggerEvent({"path": path})
            self.log.info("Triggerer: File not found yet. Sleeping for %.2f seconds", self.poll_interval)
            await asyncio.sleep(self.poll_interval)
