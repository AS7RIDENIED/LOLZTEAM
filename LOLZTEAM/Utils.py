from .Tweaks import SendAsAsync
from .models import Payment

async def CheckPayment(
    self,
    amount,
    comment: str = None,
    user_id: int = None,
    allow_hold: bool = None,
    include_payment_data: bool = False,
):
    """
    A function to check payment status based on given parameters.

    :param amount: The amount to check for payment. Not recomended to use it without comment
    :param comment: Optional comment for the payment
    :param user_id: Optional forum user_id to check payment
    :param allow_hold: Allow payments with hold. True to allow, False to disallow. Allowed by default
    :param include_payment_data: Include detailed payment data
    :return: a dictionary containing the status, status code, message, and payment data
    """
    from .API import Market
    if type(self) is not Market:
        raise TypeError("You need to pass Market object")
    payments = await SendAsAsync(
        self.payments.history,
        pmin=amount,
        pmax=amount,
        comment=comment,
        operation_type="income",
        is_hold=allow_hold,
    )
    payments_json = payments.json()
    response = {}
    # Status codes:
    # 0 - Payment not found
    # 1 - Paid
    # 2 - Paid by incorrect user
    # 3 - Paid in hold
    if payments_json["payments"]:
        for payment in reversed(payments_json["payments"].values()):
            response["status"] = "success"
            response["status_code"] = 1
            response["message"] = "Paid"
            if include_payment_data:
                response["payment_data"] = payment
            if user_id:
                if payment["data"]["user_id"] != user_id:
                    response["status"] = "error"
                    response["status_code"] = 2
                    response["message"] = "Paid by incorrect user"
            if not allow_hold:
                if payment["is_hold"]:
                    response["status"] = "error"
                    if response["status_code"] != 1:
                        response["status_code"] = int(
                            str(response["status_code"]) + "3"
                        )
                        response["message"] += " | Payment in hold"
                    else:
                        response["status_code"] = 3
                        response["message"] = "Payment in hold"
            break
    else:
        response["status"] = "error"
        response["status_code"] = 0
        response["message"] = "Not found"
    response["parameters"] = {
        "amount": amount,
        "comment": comment,
        "user_id": user_id,
        "allow_hold": allow_hold,
    }
    response = Payment(**response)
    return response
