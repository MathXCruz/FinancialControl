from pydantic import BaseModel
from pydantic.types import constr
from financial_control.balance import CategoryOptions


class FinancialOperation(BaseModel):
    name: str
    month_year: constr(regex='(0[1-9]|1[0-2])-[1-2][9, 0]\d{2}')
    category: CategoryOptions
    amount: float
