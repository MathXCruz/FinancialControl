from typing import List, Optional, Dict, Union
from enum import Enum
from fastapi import HTTPException


class CategoryOptions(str, Enum):
    income = 'income'
    transport = 'transport'
    food = 'food'
    clothing = 'clothing'
    subscriptions = 'subscriptions'
    housing = 'housing'
    others = 'others'


Item = Dict[str, Union[str, CategoryOptions, float, int]]


class Accounting:
    transactions: List[Item] = []
    current_id: int = -1

    def insert(self, operation: Item) -> Item:
        self.current_id += 1
        operation['id'] = self.current_id
        self.transactions.append(operation)
        return operation

    def find_by_id(self, item_id: int) -> Item:
        item = filter(lambda x: x['id'] == item_id, self.transactions)
        return list(item)[0]

    def find_by_field(self, month_year: Optional[str], category: Optional[CategoryOptions]) -> List[Item]:
        filtered_transactions: List[Item] = []
        if month_year is not None:
            for transaction in self.transactions:
                if transaction['month_year'] == month_year:
                    filtered_transactions.append(transaction)
        elif category is not None:
            for transaction in self.transactions:
                if transaction['category'] == category:
                    filtered_transactions.append(transaction)
        elif month_year is not None and category is not None:
            for transaction in self.transactions:
                if transaction['month_year'] == month_year and transaction['category'] == category:
                    filtered_transactions.append(transaction)
        else:
            for transaction in self.transactions:
                filtered_transactions.append(transaction)
        return filtered_transactions

    def calculate_balance(self, month_year: Optional[str], category: Optional[CategoryOptions]) -> str:
        total_balance: float = 0
        for transaction in self.find_by_field(month_year, category):
            if transaction['category'] == CategoryOptions.income:
                total_balance += transaction['amount']
            else:
                total_balance -= transaction['amount']
        return f'R${total_balance:.2f}'

    def delete_item(self, item_id: int):
        for transaction in self.transactions:
            if transaction['id'] == item_id:
                return self.transactions.remove(self.transactions[item_id])
            else:
                raise HTTPException(status_code=404, detail="Item not found")
