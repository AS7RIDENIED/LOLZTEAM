<font size=6 style="margin: auto"><center>
[Forum docs](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Forum.md) - [Market docs](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Market.md) - [Antipublic Docs](https://github.com/AS7RIDENIED/LOLZTEAM/blob/main/LOLZTEAM/Documentation/Antipublic.md)
</center></font>

<details>

<summary><font size="4">Method tree</font></summary>

* [Check payment](#check-payment)

</details>

---

## Check payment

*Displays a list of accounts in a specific category according to your parameters.*

**Parameters:**

- **amount** (any): The amount to check for payment. Not recomended to use it without comment
- **comment** (str): Optional comment for the payment
- **user_id** (int): Optional forum user_id to check payment
- **allow_hold** (bool): Allow payments with hold. True to allow, False to disallow. Allowed by default
- **include_payment_data** (bool): Include detailed payment data

**Status codes:**

- **0** - Payment not found
- **1** - Paid
- **2** - Paid by incorrect user 
    > If the set user_id is different from the user_id of the user who has paid
- **3** - Paid in hold
- **23** - Paid in hold by incorrect user 
    > If the set user_id is different from the user_id of the user who has paid in hold

**Example**

```python
from LOLZTEAM.Utils import CheckPayment
from LOLZTEAM.API import Market
async def main():
    market = Market(token="token", language="en")
    amount = 500
    comment = "unique_comment123"
    result = await CheckPayment(market, amount=amount, comment=comment)
    print("Status: " + result.status)
    print("Status code: " + result.status_code)
    print("Message: " + result.message)
    print("Payment data: " + result.payment_data)
    print("Parameters: " + result.parameters)
asyncio.run(main())
```

```python
# If not found
Status: error
Status code: 0
Message: Not found
Payment data: None
Parameters: {'amount': 500, 'comment': 'unique_comment123', 'user_id': None, 'allow_hold': None}

# If found
Status: success
Status code: 1
Message: Paid
Payment data: None
Parameters: {'amount': 500, 'comment': 'unique_comment123', 'user_id': None, 'allow_hold': None}
```
