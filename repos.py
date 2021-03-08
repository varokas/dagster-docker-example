from dagster import repository, schedule, sensor, RunRequest
import os

from pipelines import hello_pipeline, log_file_pipeline

@schedule(
    cron_schedule="*/5 * * * *", pipeline_name="hello_pipeline", execution_timezone="Asia/Bangkok"
)  # 
def test_schedule(date):
    pass

@sensor(pipeline_name="log_file_pipeline")
def my_directory_sensor(_context):
    my_directory = "./files"
    for filename in os.listdir(my_directory):
        filepath = os.path.join(my_directory, filename)
        if os.path.isfile(filepath):
            yield RunRequest(
                run_key=filename,
                run_config={"solids": {"process_file": {"config": {"filename": filename}}}},
            )

@repository
def hello_repository():
    return [hello_pipeline, log_file_pipeline, test_schedule, my_directory_sensor]
