import logging

import azure.functions as func
import azure.durable_functions as df


INSTANCE_ID = '1'

async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    client = df.DurableOrchestrationClient(starter)

    try:
        status = await client.get_status(INSTANCE_ID)
    except:
        await client.start_new('SqlSyncOrchestrator', INSTANCE_ID, None)
        
    return func.HttpResponse('OK')
