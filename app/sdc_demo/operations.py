from app.sdk import sdk
from aiohttp import web


@sdk.operation(["GET"], ["demo", "$create-patient"], public=True)
async def create_patient(operation, request):

    patient = sdk.client.resource("Patient", **{
        "id": "demo-patient",
        "name": [{
            "text": "Jack Black",
            "given": ["Jack"],
            "family": "Black"
        }]})
    await patient.save()

    return web.json_response({"resource": patient}, status=200)


@sdk.operation(["GET"], ["demo", "$create-patient"], public=True)
async def create_patient(operation, request):

    patient = sdk.client.resource("Patient", **{
        "id": "demo-patient",
        "name": [{
            "text": "Jack Black",
            "given": ["Jack"],
            "family": "Black"
        }]})
    await patient.save()

    return web.json_response({"resource": patient}, status=200)
