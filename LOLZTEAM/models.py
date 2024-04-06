from pydantic import BaseModel


class Payment(BaseModel):
    status: str
    status_code: int
    message: str
    payment_data: dict = None
    parameters: dict
