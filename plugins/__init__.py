from airflow.plugins_manager import AirflowPlugin

from timetables.custom_timetable import TimetableWorkdayWeekend


class PluginSchedulingExamples(AirflowPlugin):
    name = "plugin_scheduling_examples"
    timetables = [TimetableWorkdayWeekend]
