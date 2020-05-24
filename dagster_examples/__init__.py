def get_hello_world_pipelines():
    from dagster_examples.hello_world import (
        hello_world_pipeline,
    )

    return [
        hello_world_pipeline,
    ]

def get_hello_dag_pipelines():
    from dagster_examples.hello_dag import (
        hello_dag_pipeline,
    )

    return [
        hello_dag_pipeline,
    ]   

def get_actual_dag_pipelines():
    from dagster_examples.actual_dag import (
        actual_dag_pipeline,
    )

    return [
        actual_dag_pipeline,
    ]   

def get_inputs_pipelines():
    from dagster_examples.inputs import (
        hello_inputs_pipeline,
    )

    return [
        hello_inputs_pipeline,
    ]       

def define_repo():
    from dagster import lambda_solid, pipeline, RepositoryDefinition

    pipeline_defs = (
        get_hello_world_pipelines() +
        get_hello_dag_pipelines() + 
        get_actual_dag_pipelines() + 
        get_inputs_pipelines()
    )

    return RepositoryDefinition(
        name='demo_repository',
        pipeline_defs=pipeline_defs,
    )    