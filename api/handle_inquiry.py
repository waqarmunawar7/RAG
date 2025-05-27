from fastapi import Request, status
from fastapi.responses import JSONResponse
from service import SendInquiryEmail

async def inquiry(request: Request):
    data = await request.json()
    await SendInquiryEmail.sendEmail(request.client.host , data)
    return JSONResponse(content={"message":"Form Submited successfully!"})