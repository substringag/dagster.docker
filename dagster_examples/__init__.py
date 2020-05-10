def get_hello_world_pipelines():
    from dagster_examples.hello_world import (
        hello_world_pipeline,
    )

    return [
        hello_world_pipeline,
    ]

def define_repo():
    from dagster import lambda_solid, pipeline, RepositoryDefinition

    pipeline_defs = (
        get_hello_world_pipelines()
    )

    return RepositoryDefinition(
        name='demo_repository',
        pipeline_defs=pipeline_defs,
    )    