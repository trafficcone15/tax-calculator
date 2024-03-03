def calculate_income_tax(income):
    brackets = [
        (14000, 0.105),
        (48000 - 14000, 0.175),
        (70000 - 48000, 0.30),
        (180000 - 70000, 0.33),
    ]
    tax = 0
    remaining_income = income

    for bracket, rate in brackets:
        taxable = min(remaining_income, bracket)
        tax += taxable * rate
        remaining_income -= taxable
        if remaining_income <= 0:
            break

    if remaining_income > 0:
        tax += remaining_income * 0.39

    return tax

def calculate_ietc(income):
    if 24000 <= income <= 44000:
        return 520
    elif 44000 < income <= 48000:
        return 520 - (0.13 * (income - 44000))
    else:
        return 0

def main():
    total_gross = float(input("Enter your total gross amount for the financial year: "))
    total_paye_deducted = float(input("Enter the total PAYE deducted: "))
    total_acc_earners_levy = float(input("Enter the total ACC earners' levy: "))

    income_tax_liability = calculate_income_tax(total_gross)
    ietc = calculate_ietc(total_gross)
    total_tax = total_paye_deducted - total_acc_earners_levy
    total_tax_deductions = total_tax + ietc
    refund_or_due = total_tax_deductions - income_tax_liability

    print(f"Independant Earners Tax Credit is {ietc:.2f}.")
    print(f"Income tax liability is {income_tax_liability:.2f}.")
    print(f"Total tax deductions is {total_tax_deductions:.2f}.")

    if refund_or_due > 0:
        print(f"Congratulations, you are eligible for a tax refund of NZD {refund_or_due:.2f}.")
    elif refund_or_due < 0:
        print(f"You owe NZD {-refund_or_due:.2f} in taxes.")
    else:
        print("Your tax payments and liabilities are equal. You neither owe taxes nor receive a refund.")

if __name__ == "__main__":
    main()