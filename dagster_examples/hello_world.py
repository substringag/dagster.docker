from dagster import execute_pipeline, pipeline, solid, lambda_solid


@lambda_solid
def hello_world():
    return 'hello'


@pipeline
def hello_world_pipeline():
    return hello_world()
