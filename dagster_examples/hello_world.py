from dagster import execute_pipeline, pipeline, solid, lambda_solid


@solid
def hello_world(_):
    return 'hello'


@pipeline
def hello_world_pipeline():
    hello_world()
