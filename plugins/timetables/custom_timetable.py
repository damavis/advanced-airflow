from __future__ import annotations

from airflow.timetables.base import DataInterval, TimeRestriction, DagRunInfo
from airflow.timetables.interval import _DataIntervalTimetable
from pendulum import DateTime


class TimetableWorkdayWeekend(_DataIntervalTimetable):
    """Every 8 hours during workdays. Every 24 hours during weekends"""

    WORKDAY_DELTA_HOURS = 8
    WEEKEND_DELTA_HOURS = 24

    def _get_prev(self, current: DateTime) -> DateTime:
        if current.subtract(seconds=1).weekday() >= 5:
            return current.subtract(hours=self.WEEKEND_DELTA_HOURS)
        else:
            return current.subtract(hours=self.WORKDAY_DELTA_HOURS)

    def _get_next(self, current: DateTime) -> DateTime:
        if current.weekday() >= 5:
            return current.add(hours=self.WEEKEND_DELTA_HOURS)
        else:
            return current.add(hours=self.WORKDAY_DELTA_HOURS)

    def _align_to_prev(self, current: DateTime) -> DateTime:
        if current.weekday() >= 5:
            # Align to the start of the current day
            return current.start_of('day')
        else:
            # Align to the last workday_delta_hours interval in the day
            prev_hour = (current.hour // self.WORKDAY_DELTA_HOURS) * self.WORKDAY_DELTA_HOURS
            return current.start_of('day').set(hour=prev_hour)

    def _align_to_next(self, current: DateTime) -> DateTime:
        return self._get_next(self._align_to_prev(current))

    def _skip_to_latest(self, earliest: DateTime | None) -> DateTime:
        current_time = DateTime.utcnow()
        end = self._align_to_prev(current_time)
        start = self._get_prev(end)
        return max(start, self._align_to_next(earliest))

    def infer_manual_data_interval(self, *, run_after: DateTime) -> DataInterval:
        end = self._align_to_prev(run_after)
        start = self._get_prev(end)
        return DataInterval(start=start, end=end)

    def next_dagrun_info(self, *, last_automated_data_interval: DataInterval | None, restriction: TimeRestriction) -> DagRunInfo | None:
        return super().next_dagrun_info(last_automated_data_interval=last_automated_data_interval, restriction=restriction)


