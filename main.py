from fastapi import FastAPI, status
from typing import Optional
from financial_control.balance import Accounting, CategoryOptions
from financial_control.data_types import FinancialOperation

app = FastAPI()
accounting = Accounting()


@app.get('/')
def root():
    return 'Welcome to the financial control app!'


@app.get('/transactions/')
def list_transactions(
    month_year: Optional[str] = None,
    category: Optional[CategoryOptions] = None,
):
    return accounting.find_by_field(month_year, category)


@app.get('/operation/{item_id}')
def show_transaction(item_id: int):
    return accounting.find_by_id(item_id)


@app.get('/balance')
def show_accounting(
    month_year: Optional[str] = None,
    category: Optional[CategoryOptions] = None,
):
    return accounting.calculate_balance(month_year, category)


@app.delete('/', status_code=status.HTTP_204_NO_CONTENT)
def remove_transaction(item_id: int):
    return accounting.delete_item(item_id)


@app.post('/', status_code=status.HTTP_201_CREATED)
def add_transaction(transaction: FinancialOperation):
    return accounting.insert(transaction.dict())
