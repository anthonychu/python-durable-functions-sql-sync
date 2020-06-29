import logging

import azure.functions as func
import azure.durable_functions as df


async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    client = df.DurableOrchestrationClient(starter)

    status = await client.get_status('1')
    return func.HttpResponse(status)
    # instance_id = await client.start_new('SqlSyncOrchestrator', '1', None)

    # logging.info(f"Started orchestration with ID = '{instance_id}'.")

    # return client.create_check_status_response(req, instance_id)