from dagster import execute_pipeline, lambda_solid, pipeline, String


@lambda_solid
def add_hello_to_word(word: String):
    return 'Hello, ' + word + '!'


@pipeline
def hello_inputs_pipeline():
    add_hello_to_word()