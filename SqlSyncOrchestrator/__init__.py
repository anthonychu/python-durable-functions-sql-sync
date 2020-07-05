# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json
from datetime import timedelta 

import azure.functions as func
import azure.durable_functions as df


polling_interval = 15

def orchestrator_function(context: df.DurableOrchestrationContext):
    # prev_rowversion = context.get_input()
    # current_rowversion = yield context.call_activity('Sync', prev_rowversion)

    # next_check = context.current_utc_datetime + timedelta(seconds=polling_interval)
    # logging.warning(f'Next: {str(next_check)}')
    # yield context.create_timer(next_check)
    logging.warning(f'Continuing as new')
    yield context.continue_as_new("")


main = df.Orchestrator.create(orchestrator_function)