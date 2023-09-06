import asyncio
from aiochclient import ChClient
from aiohttp import ClientSession

from core.settings.database import DATABASE_SETTINGS
from v1.utils.constants.constants import TABLES


def get_async_db_client(session):
    return ChClient(
        session, 
        url="http://" + DATABASE_SETTINGS.get("host") + ":" + DATABASE_SETTINGS.get("port"),
        user=DATABASE_SETTINGS.get("user"),
        password=DATABASE_SETTINGS.get("password"),
        database=DATABASE_SETTINGS.get("database")
    )

def generate_query_for_id(id, table_name):
    query = f"""
        SELECT * 
        FROM {table_name}
        WHERE id = '{id}'
    """
    return query

async def get_info_from_db(id):
    info = []

    async with ClientSession() as session:
        async with get_async_db_client(session) as db_client:
            tasks = [asyncio.ensure_future(async_db_requests(db_client, info, id, table)) for table in TABLES]
            await asyncio.gather(*tasks)

    return info

async def async_db_requests(db_client, info, id, table):
    query = generate_query_for_id(id, table)
    answer = await db_client.fetch(query, json=True)
    
    if answer:
        info.append(answer)
    else:
        print("Not Found information for id: {} in table: {}".format(id, table))

    return 



