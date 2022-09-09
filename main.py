from investments import investments
from installments import installments
import numpy_financial as npf

cashflows = {}

def calc_irr():
    data = []
    for amount in cashflows.values():
        data.append(amount)

    irr = round(npf.irr(data), 2)
    print("TIR:", irr)


if __name__ == "__main__":

    for investment in investments:
        cashflows[investment['created_at']] =  -1*float(investment['amount']) 
        for installment in installments:
            if investment['id'] == installment['investment_id']:
                cashflows[installment['due_date']] = installment['amount']
        calc_irr()
        cashflows.clear()

