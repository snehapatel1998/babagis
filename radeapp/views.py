import logging
import traceback
from django.shortcuts import render


from .forms import CompanyDetailsForm, IncomeStatement_2019, IncomeStatement_2020, IncomeStatement_2021, Balancesheet_2019, Balancesheet_2020,Balancesheet_2021

# Create your views here.

def entry(request):
    cd = CompanyDetailsForm()
    inc = IncomeStatement_2019()
    inc1 = IncomeStatement_2020()
    inc2 = IncomeStatement_2021()
    bal = Balancesheet_2019()  
    bal1 = Balancesheet_2020()
    bal2 = Balancesheet_2021()
     
    return render(request, 'entry.html', {'cd':cd, 'inc':inc,'inc1':inc1,'inc2':inc2,'bal':bal,'bal1':bal1,'bal2':bal2})  
def ratio(request):
    #values in incomestatement_2019
    Revenue = request.POST.get('Revenue')
    Beginning_Inventory = request.POST.get('Beginning_Inventory')
    Purchases = request.POST.get('Purchases')
    Freight_in_Expenses = request.POST.get('Freight_in_Expenses')
    Ending_Inventory = request.POST.get('Ending_Inventory')
    Bill_Of_Materials = request.POST.get('Bill_Of_Materials')
    Labour_Charges = request.POST.get('Labour_Charges')
    Sub_Contract_Expenses = request.POST.get('Sub_Contract_Expenses')
    Cost_Of_Goods_Sold = request.POST.get('Cost_Of_Goods_Sold')
    Gross_Profit = request.POST.get('Gross_Profit')
    Business_Development_Expenses = request.POST.get('Business_Development_Expenses')
    Fuel_Expenses = request.POST.get('Fuel_Expenses') 
    Conveyance_Expenses = request.POST.get('Conveyance_Expenses')
    Telephone_Expenses = request.POST.get('Telephone_Expenses')
    Selling_and_Admin_Expenses = request.POST.get('Selling_and_Admin_Expenses')
    Electricity_Charges = request.POST.get('Electricity_Charges')  
    Vehicle_Manitainence = request.POST.get('Vehicle_Manitainence')
    Machine_Maintainence = request.POST.get('Machine_Maintainence')
    Rent = request.POST.get('Rent')
    Consumables = request.POST.get('Consumables')
    Bank_Charges = request.POST.get('Bank_Charges')
    Other_Operating_Expenses = request.POST.get('Other_Operating_Expenses')
    EBITDA = request.POST.get('EBITDA')
    Depreciation = request.POST.get('Depreciation')
    Amortization_Expense = request.POST.get('Amortization_Expense')
    Other_Expenses = request.POST.get('Other_Expenses')
    Operating_Profit = request.POST.get('Operating_Profit')
    Bank_Interest_Expense = request.POST.get('Bank_Interest_Expense')
    Other_Interest_Expense = request.POST.get('Other_Interest_Expense')
    Total_Interest_Expense = request.POST.get('Total_Interest_Expense')
    Bank_Interest_Income = request.POST.get('Bank_Interest_Income')
    Other_Interest_Income = request.POST.get('Other_Interest_Income')
    Total_Interest_Income = request.POST.get('Total_Interest_Income')
    Net_Income_Before_Taxes = request.POST.get('Net_Income_Before_Taxes')
    Income_Tax_Expense = request.POST.get('Income_Tax_Expense')
    Net_Income = request.POST.get('Net_Income')

    #values in incomestatement_2020
    Revenue1 = request.POST.get('Revenue1')

    Beginning_Inventory1 = request.POST.get('Beginning_Inventory1')
    
    Purchases1 = request.POST.get('Purchases1')
    Freight_in_Expenses1 = request.POST.get('Freight_in_Expenses1')
    Ending_Inventory1 = request.POST.get('Ending_Inventory1')
    Bill_Of_Materials1 = request.POST.get('Bill_Of_Materials1')
    Labour_Charges1 = request.POST.get('Labour_Charges1')
    Sub_Contract_Expenses1 = request.POST.get('Sub_Contract_Expenses1')
    Cost_Of_Goods_Sold1 = request.POST.get('Cost_Of_Goods_Sold1')
    Gross_Profit1 = request.POST.get('Gross_Profit1')
    Business_Development_Expenses1 = request.POST.get('Business_Development_Expenses1')
    Fuel_Expenses1 = request.POST.get('Fuel_Expenses1') 
    Conveyance_Expenses1 = request.POST.get('Conveyance_Expenses1')
    Telephone_Expenses1 = request.POST.get('Telephone_Expenses1')
    Selling_and_Admin_Expenses1 = request.POST.get('Selling_and_Admin_Expenses1')
    Electricity_Charges1 = request.POST.get('Electricity_Charges1')  
    Vehicle_Manitainence1 = request.POST.get('Vehicle_Manitainence1')
    Machine_Maintainence1 = request.POST.get('Machine_Maintainence1')
    Rent1 = request.POST.get('Rent1')
    Consumables1 = request.POST.get('Consumables1')
    Bank_Charges1 = request.POST.get('Bank_Charges1')
    Other_Operating_Expenses1 = request.POST.get('Other_Operating_Expenses1')
    EBITDA1 = request.POST.get('EBITDA1')
    Depreciation1 = request.POST.get('Depreciation1')
    Amortization_Expense1 = request.POST.get('Amortization_Expense1')
    Other_Expenses1 = request.POST.get('Other_Expenses1')
    Operating_Profit1 = request.POST.get('Operating_Profit1')
    Bank_Interest_Expense1 = request.POST.get('Bank_Interest_Expense1')
    Other_Interest_Expense1 = request.POST.get('Other_Interest_Expense1')
    Total_Interest_Expense1 = request.POST.get('Total_Interest_Expense1')
    Bank_Interest_Income1 = request.POST.get('Bank_Interest_Income1')
    Other_Interest_Income1 = request.POST.get('Other_Interest_Income1')
    Total_Interest_Income1 = request.POST.get('Total_Interest_Income1')
    Net_Income_Before_Taxes1 = request.POST.get('Net_Income_Before_Taxes1')
    Income_Tax_Expense1 = request.POST.get('Income_Tax_Expense1')
    Net_Income1 = request.POST.get('Net_Income1')

    #values in incomestatement_2021
    Revenue2 = request.POST.get('Revenue2')
    
    Beginning_Inventory2 = request.POST.get('Beginning_Inventory2')
    
    Purchases2 = request.POST.get('Purchases2')
    Freight_in_Expenses2 = request.POST.get('Freight_in_Expenses2')
    Ending_Inventory2 = request.POST.get('Ending_Inventory2')
    Bill_Of_Materials2 = request.POST.get('Bill_Of_Materials2')
    Labour_Charges2 = request.POST.get('Labour_Charges2')
    Sub_Contract_Expenses2 = request.POST.get('Sub_Contract_Expenses2')
    Cost_Of_Goods_Sold2 = request.POST.get('Cost_Of_Goods_Sold2')
    Gross_Profit2 = request.POST.get('Gross_Profit2')
    Business_Development_Expenses2 = request.POST.get('Business_Development_Expenses2')
    Fuel_Expenses2 = request.POST.get('Fuel_Expenses2') 
    Conveyance_Expenses2 = request.POST.get('Conveyance_Expenses2')
    Telephone_Expenses2 = request.POST.get('Telephone_Expenses2')
    Selling_and_Admin_Expenses2 = request.POST.get('Selling_and_Admin_Expenses2')
    Electricity_Charges2 = request.POST.get('Electricity_Charges2')  
    Vehicle_Manitainence2 = request.POST.get('Vehicle_Manitainence2')
    Machine_Maintainence2 = request.POST.get('Machine_Maintainence2')
    Rent2 = request.POST.get('Rent2')
    Consumables2 = request.POST.get('Consumables2')
    Bank_Charges2 = request.POST.get('Bank_Charges2')
    Other_Operating_Expenses2 = request.POST.get('Other_Operating_Expenses2')
    EBITDA2 = request.POST.get('EBITDA2')
    Depreciation2 = request.POST.get('Depreciation2')
    Amortization_Expense2 = request.POST.get('Amortization_Expense2')
    Other_Expenses2 = request.POST.get('Other_Expenses2')
    Operating_Profit2 = request.POST.get('Operating_Profit2')
    Bank_Interest_Expense2 = request.POST.get('Bank_Interest_Expense2')
    Other_Interest_Expense2 = request.POST.get('Other_Interest_Expense2')
    Total_Interest_Expense2 = request.POST.get('Total_Interest_Expense2')
    Bank_Interest_Income2 = request.POST.get('Bank_Interest_Income2')
    Other_Interest_Income2 = request.POST.get('Other_Interest_Income2')
    Total_Interest_Income2 = request.POST.get('Total_Interest_Income2')
    Net_Income_Before_Taxes2 = request.POST.get('Net_Income_Before_Taxes2')
    Income_Tax_Expense2 = request.POST.get('Income_Tax_Expense2')
    Net_Income2 = request.POST.get('Net_Income2')


    #values in balanesheet_2019
    Cash_And_Cash_Equivalents = request.POST.get('Cash_And_Cash_Equivalents')
    Deposit = request.POST.get('Deposit')
    Accounts_Receivable = request.POST.get('Accounts_Receivable')
    Inventory = request.POST.get('Inventory')
    Prepaid_Expenses = request.POST.get('Prepaid_Expenses')
    Other_Current_Assets = request.POST.get('Other_Current_Assets')
    Total_Current_Assets = request.POST.get('Total_Current_Assets')
    Property_Plant_And_Equipment = request.POST.get('Property_Plant_And_Equipment')
    Other_Long_Term_Assets = request.POST.get('Other_Long_Term_Assets')
    Research_and_development = request.POST.get('Research_and_development')
    Intangible_Assets = request.POST.get('Intangible_Assets')
    Good_Will = request.POST.get('Good_Will')
    Total_Long_Term_Assets = request.POST.get('Total_Long_Term_Assets')
    Total_Assets = request.POST.get('Total_Assets')
    Accounts_Payable = request.POST.get('Accounts_Payable')
    Revolving_Debt = request.POST.get('Revolving_Debt')
    Income_Taxes_Payable = request.POST.get('Income_Taxes_Payable')
    Current_Portion_Of_Long_Term_Debt = request.POST.get('Current_Portion_Of_Long_Term_Debt')
    Other_Current_Liabilities = request.POST.get('Other_Current_Liabilities')
    Total_Current_Liabilities = request.POST.get('Total_Current_Liabilities')
    Non_Current_Liabilities = request.POST.get('Non_Current_Liabilities')
    Other_Long_Term_Liabilities = request.POST.get('Other_Long_Term_Liabilities')
    Total_Long_Term_Liabilities = request.POST.get('Total_Long_Term_Liabilities')
    Total_Liabilities = request.POST.get('Total_Liabilities')
    Capital_Account = request.POST.get('Capital_Account')
    Total_owners_equity = request.POST.get('Total_owners_equity')
    Total_owners_equity_and_liabilities = request.POST.get('Total_owners_equity_and_liabilities')

    #values in balanesheet_2020
    Cash_And_Cash_Equivalents1 = request.POST.get('Cash_And_Cash_Equivalents1')
    Deposit1 = request.POST.get('Deposit1')
    Accounts_Receivable1 = request.POST.get('Accounts_Receivable1')
    Inventory1 = request.POST.get('Inventory1')
    Prepaid_Expenses1 = request.POST.get('Prepaid_Expenses1')
    Other_Current_Assets1 = request.POST.get('Other_Current_Assets1')
    Total_Current_Assets1 = request.POST.get('Total_Current_Assets1')
    Property_Plant_And_Equipment1 = request.POST.get('Property_Plant_And_Equipment1')
    Other_Long_Term_Assets1 = request.POST.get('Other_Long_Term_Assets1')
    Research_and_development1 = request.POST.get('Research_and_development1')
    Intangible_Assets1 = request.POST.get('Intangible_Assets1')
    Good_Will1 = request.POST.get('Good_Will1')
    Total_Long_Term_Assets1 = request.POST.get('Total_Long_Term_Assets1')
    Total_Assets1 = request.POST.get('Total_Assets1')
    Accounts_Payable1 = request.POST.get('Accounts_Payable1')
    Revolving_Debt1 = request.POST.get('Revolving_Debt1')
    Income_Taxes_Payable1 = request.POST.get('Income_Taxes_Payable1')
    Current_Portion_Of_Long_Term_Debt1 = request.POST.get('Current_Portion_Of_Long_Term_Debt1')
    Other_Current_Liabilities1 = request.POST.get('Other_Current_Liabilities1')
    Total_Current_Liabilities1 = request.POST.get('Total_Current_Liabilities1')
    Non_Current_Liabilities1 = request.POST.get('Non_Current_Liabilities1')
    Other_Long_Term_Liabilities1 = request.POST.get('Other_Long_Term_Liabilities1')
    Total_Long_Term_Liabilities1 = request.POST.get('Total_Long_Term_Liabilities1')
    Total_Liabilities1 = request.POST.get('Total_Liabilities1')
    Capital_Account1 = request.POST.get('Capital_Account1')
    Total_owners_equity1 = request.POST.get('Total_owners_equity1')
    Total_owners_equity_and_liabilities1 = request.POST.get('Total_owners_equity_and_liabilities1')

    #values in balanesheet_2021
    Cash_And_Cash_Equivalents2 = request.POST.get('Cash_And_Cash_Equivalents2')
    Deposit2 = request.POST.get('Deposit2')
    Accounts_Receivable2 = request.POST.get('Accounts_Receivable2')
    Inventory2 = request.POST.get('Inventory2')
    Prepaid_Expenses2 = request.POST.get('Prepaid_Expenses2')
    Other_Current_Assets2 = request.POST.get('Other_Current_Assets2')
    Total_Current_Assets2 = request.POST.get('Total_Current_Assets2')
    Property_Plant_And_Equipment2 = request.POST.get('Property_Plant_And_Equipment2')
    Other_Long_Term_Assets2 = request.POST.get('Other_Long_Term_Assets2')
    Research_and_development2 = request.POST.get('Research_and_development2')
    Intangible_Assets2 = request.POST.get('Intangible_Assets2')
    Good_Will2 = request.POST.get('Good_Will2')
    Total_Long_Term_Assets2 = request.POST.get('Total_Long_Term_Assets2')
    Total_Assets2 = request.POST.get('Total_Assets2')
    Accounts_Payable2 = request.POST.get('Accounts_Payable2')
    Revolving_Debt2 = request.POST.get('Revolving_Debt2')
    Income_Taxes_Payable2 = request.POST.get('Income_Taxes_Payable2')
    Current_Portion_Of_Long_Term_Debt2 = request.POST.get('Current_Portion_Of_Long_Term_Debt2')
    Other_Current_Liabilities2 = request.POST.get('Other_Current_Liabilities2')
    Total_Current_Liabilities2 = request.POST.get('Total_Current_Liabilities2')
    Non_Current_Liabilities2 = request.POST.get('Non_Current_Liabilities2')
    Other_Long_Term_Liabilities2 = request.POST.get('Other_Long_Term_Liabilities2')
    Total_Long_Term_Liabilities2 = request.POST.get('Total_Long_Term_Liabilities2')
    Total_Liabilities2 = request.POST.get('Total_Liabilities2')
    Capital_Account2 = request.POST.get('Capital_Account2')
    Total_owners_equity2 = request.POST.get('Total_owners_equity2')
    Total_owners_equity_and_liabilities2 = request.POST.get('Total_owners_equity_and_liabilities2')
        
        
    
    #Ratios calculation
    try:
        beginninginventory_ratio = round(int(Beginning_Inventory)/int(Revenue), 2)
        beginninginventory_ratio1 = round(int(Beginning_Inventory1)/int(Revenue1), 2)
        print(beginninginventory_ratio1)
        beginninginventory_ratio2 = round(int(Beginning_Inventory2)/int(Revenue2), 2)
        purchase_ratio = round(int(Purchases)/int(Revenue),2)
        purchase_ratio1 = round(int(Purchases1)/int(Revenue1),2)
        purchase_ratio2 = round(int(Purchases2)/int(Revenue2),2)
        freightExpenses_ratio = round(int(Freight_in_Expenses)/int(Revenue),2)
        freightExpenses_ratio1 = round(int(Freight_in_Expenses1)/int(Revenue1),2)
        freightExpenses_ratio2 = round(int(Freight_in_Expenses2)/int(Revenue2),2)
        ending_Inventory_ratio = round(int(Ending_Inventory)/int(Revenue),2)
        ending_Inventory_ratio1 = round(int(Ending_Inventory1)/int(Revenue1),2)
        ending_Inventory_ratio2 = round(int(Ending_Inventory2)/int(Revenue2),2)
        billmaterils_ratio = round(int(Bill_Of_Materials)/int(Revenue),2)
        billmaterils_ratio1 = round(int(Bill_Of_Materials1)/int(Revenue1),2)
        billmaterils_ratio2 = round(int(Bill_Of_Materials2)/int(Revenue2),2)
        labourcharges_ratio = round(int(Labour_Charges)/int(Revenue),2)
        labourcharges_ratio1 = round(int(Labour_Charges1)/int(Revenue1),2)
        labourcharges_ratio2 = round(int(Labour_Charges2)/int(Revenue2),2)
        labourchargesperworkinghour = round(int(Labour_Charges)/2400,2)
        labourchargesperworkinghour1 = round(int(Labour_Charges1)/2400,2)
        labourchargesperworkinghour2 = round(int(Labour_Charges2)/2400,2)
        subcontractexpenses_ratio = round(int(Sub_Contract_Expenses)/ int(Revenue),2)
        subcontractexpenses_ratio1 = round(int(Sub_Contract_Expenses1)/ int(Revenue1),2)
        subcontractexpenses_ratio2 = round(int(Sub_Contract_Expenses2)/ int(Revenue2),2)
        costofgoodssold_ratio = round(int(Cost_Of_Goods_Sold)/int(Revenue),2)
        costofgoodssold_ratio1 = round(int(Cost_Of_Goods_Sold1)/int(Revenue1),2)
        costofgoodssold_ratio2 = round(int(Cost_Of_Goods_Sold2)/int(Revenue2),2)  
        grossprofit_ratio = round(int(Gross_Profit)/int(Revenue),2)
        grossprofit_ratio1 = round(int(Gross_Profit1)/int(Revenue1),2)
        grossprofit_ratio2 = round(int(Gross_Profit2)/int(Revenue2),2)
        businessdevelopment_ratio = round(int(Business_Development_Expenses)/int(Revenue),2)
        businessdevelopment_ratio1 = round(int(Business_Development_Expenses1)/int(Revenue1),2)
        businessdevelopment_ratio2 = round(int(Business_Development_Expenses2)/int(Revenue2),2)
        fuelexpenses_ratio = round(int(Fuel_Expenses)/int(Revenue),2)
        fuelexpenses_ratio1 = round(int(Fuel_Expenses1)/int(Revenue1),2)
        fuelexpenses_ratio2 = round(int(Fuel_Expenses2)/int(Revenue2),2)
        conveyancexpenses_ratio = round(int(Conveyance_Expenses)/int(Revenue),2)
        conveyancexpenses_ratio1 = round(int(Conveyance_Expenses1)/int(Revenue1),2)
        conveyancexpenses_ratio2 = round(int(Conveyance_Expenses2)/int(Revenue2),2)
        telephoneexpenses_ratio = round(int(Telephone_Expenses)/int(Revenue),2)
        telephoneexpenses_ratio1 = round(int(Telephone_Expenses1)/int(Revenue1),2)
        telephoneexpenses_ratio2 = round(int(Telephone_Expenses2)/int(Revenue2),2)
        sellingandadminexpenses_ratio = round(int(Selling_and_Admin_Expenses)/int(Revenue),2)
        sellingandadminexpenses_ratio1 = round(int(Selling_and_Admin_Expenses1)/int(Revenue1),2)
        sellingandadminexpenses_ratio2 = round(int(Selling_and_Admin_Expenses2)/int(Revenue2),2)
        electricitycharges_ratio = round(int(Electricity_Charges)/int(Revenue),2)
        electricitycharges_ratio1 = round(int(Electricity_Charges1)/int(Revenue1),2)
        electricitycharges_ratio2 = round(int(Electricity_Charges2)/int(Revenue2),2)

        vechilemanitainence_ratio = round(int(Vehicle_Manitainence)/int(Revenue),2)
        vechilemanitainence_ratio1 = round(int(Vehicle_Manitainence1)/int(Revenue2),2)
        vechilemanitainence_ratio2 = round(int(Vehicle_Manitainence2)/int(Revenue2),2)
        machinemaintainence_ratio = round(int(Machine_Maintainence)/int(Revenue),2)
        machinemaintainence_ratio1 = round(int(Machine_Maintainence1)/int(Revenue1),2)
        machinemaintainence_ratio2 = round(int(Machine_Maintainence2)/int(Revenue2),2)
        rents_ratio = round(int(Rent)/int(Revenue),2)
        rents_ratio1 = round(int(Rent1)/int(Revenue1),2)
        rents_ratio2 = round(int(Rent2)/int(Revenue2),2)
        consumable_ratio = round(int(Consumables)/int(Revenue),2)
        consumable_ratio1 = round(int(Consumables1)/int(Revenue1),2)
        consumable_ratio2 = round(int(Consumables2)/int(Revenue2),2)
        bankcharges_ratio = round(int(Bank_Charges)/int(Revenue),2)
        bankcharges_ratio1 = round(int(Bank_Charges1)/int(Revenue1),2)
        bankcharges_ratio2 = round(int(Bank_Charges2)/int(Revenue2),2)
        otheroperatingexpenses_ratio = round(int(Other_Operating_Expenses)/int(Revenue),2)
        otheroperatingexpenses_ratio1 = round(int(Other_Operating_Expenses1)/int(Revenue1),2)
        otheroperatingexpenses_ratio2 = round(int(Other_Operating_Expenses2)/int(Revenue2),2)
        ebitda_ratio = round(int(EBITDA)/int(Revenue),2)
        ebitda_ratio1 = round(int(EBITDA1)/int(Revenue1),2)
        ebitda_ratio2 = round(int(EBITDA2)/int(Revenue2),2)
        depreciation_ratio = round(int(Depreciation)/int(Revenue),2)
        depreciation_ratio1 = round(int(Depreciation1)/int(Revenue1),2)
        depreciation_ratio2 = round(int(Depreciation2)/int(Revenue2),2)
        amortizationexpense_ratio = round(int(Amortization_Expense)/int(Revenue),2)
        amortizationexpense_ratio1 = round(int(Amortization_Expense1)/int(Revenue1),2)
        amortizationexpense_ratio2 = round(int(Amortization_Expense2)/int(Revenue2),2)
        otherexpenses_ratio = round(int(Other_Expenses)/int(Revenue),2)
        otherexpenses_ratio1 = round(int(Other_Expenses1)/int(Revenue1),2)
        otherexpenses_ratio2 = round(int(Other_Expenses2)/int(Revenue2),2)
        operatingProfit_ratio = round(int(Operating_Profit)/int(Revenue),2) 
        operatingProfit_ratio1 = round(int(Operating_Profit1)/int(Revenue1),2)
        operatingProfit_ratio2 = round(int(Operating_Profit2)/int(Revenue2),2)
        bank_Interest_Expense_ratio = round(int(Bank_Interest_Expense)/int(Revenue),2)
        bank_Interest_Expense_ratio1 = round(int(Bank_Interest_Expense1)/int(Revenue1),2)
        bank_Interest_Expense_ratio2 = round(int(Bank_Interest_Expense2)/int(Revenue2),2)
        other_Interest_Expense_ratio = round(int(Other_Interest_Expense)/int(Revenue),2)
        other_Interest_Expense_ratio1 = round(int(Other_Interest_Expense1)/int(Revenue1),2)
        other_Interest_Expense_ratio2 = round(int(Other_Interest_Expense2)/int(Revenue2),2)
        total_Interest_Expense_ratio = round(int(Total_Interest_Expense)/int(Revenue),2)
        total_Interest_Expense_ratio1 = round(int(Total_Interest_Expense1)/int(Revenue1),2)
        total_Interest_Expense_ratio2 = round(int(Total_Interest_Expense2)/int(Revenue2),2)
        Interest_Expense_per_hour = round(int(Total_Interest_Expense)/2400,2)
        Interest_Expense_per_hour1 = round(int(Total_Interest_Expense1)/2400,2)
        Interest_Expense_per_hour2 = round(int(Total_Interest_Expense2)/2400,2)
        bank_Interest_Income_ratio = round(int(Bank_Interest_Income)/int(Revenue),2)
        bank_Interest_Income_ratio1 = round(int(Bank_Interest_Income1)/int(Revenue1),2)
        bank_Interest_Income_ratio2 = round(int(Bank_Interest_Income2)/int(Revenue2),2)
        other_Interest_Income_ratio = round(int(Other_Interest_Income)/int(Revenue),2)
        other_Interest_Income_ratio1 = round(int(Other_Interest_Income1)/int(Revenue1),2)
        other_Interest_Income_ratio2 = round(int(Other_Interest_Income2)/int(Revenue2),2)
        total_Interest_Income_ratio = round(int(Total_Interest_Income)/int(Revenue),2)
        total_Interest_Income_ratio1 = round(int(Total_Interest_Income1)/int(Revenue1),2)
        total_Interest_Income_ratio2 = round(int(Total_Interest_Income2)/int(Revenue2),2)
        net_Income_Before_Taxes_ratio =  round(int(Net_Income_Before_Taxes)/int(Revenue),2)
        net_Income_Before_Taxes_ratio1 =  round(int(Net_Income_Before_Taxes1)/int(Revenue1),2)
        net_Income_Before_Taxes_ratio2 =  round(int(Net_Income_Before_Taxes2)/int(Revenue2),2)
        income_Tax_Expense_ratio = round(int(Income_Tax_Expense)/int(Revenue),2)
        income_Tax_Expense_ratio1 = round(int(Income_Tax_Expense1)/int(Revenue1),2)
        income_Tax_Expense_ratio2 = round(int(Income_Tax_Expense2)/int(Revenue2),2)
        net_Income_ratio = round(int(Net_Income)/int(Revenue),2)
        net_Income_ratio1 = round(int(Net_Income1)/int(Revenue1),2)
        net_Income_ratio2 = round(int(Net_Income2)/int(Revenue2),2)
    #Ratio calculation balancesheet
        Current_ratio = round(int(Total_Current_Assets)/int(Total_Current_Liabilities),2)
        Current_ratio1 = round(int(Total_Current_Assets1)/int(Total_Current_Liabilities1),2)
        Current_ratio2 = round(int(Total_Current_Assets2)/int(Total_Current_Liabilities2),2)
        Quick_ratio = round((int(Total_Current_Assets)-int(Inventory))/int(Total_Current_Liabilities),2)
        Quick_ratio1 = round((int(Total_Current_Assets1)-int(Inventory1))/int(Total_Current_Liabilities1),2)
        Quick_ratio2 = round((int(Total_Current_Assets2)-int(Inventory2))/int(Total_Current_Liabilities2),2)
        Return_on_Assets_ratio = round(int(Net_Income)/int(Total_Assets),2)
        Return_on_Assets_ratio1 = round(int(Net_Income1)/int(Total_Assets1),2)
        Return_on_Assets_ratio2 = round(int(Net_Income2)/int(Total_Assets2),2)
        Return_on_Equity_ratio = round(int(Net_Income)/int(Total_owners_equity),2)
        Return_on_Equity_ratio1 = round(int(Net_Income1)/int(Total_owners_equity1),2)
        Return_on_Equity_ratio2 = round(int(Net_Income2)/int(Total_owners_equity2),2)
        Gross_Margin_ratio = round(int(Gross_Profit)/int(Revenue),2)
        Gross_Margin_ratio1 = round(int(Gross_Profit1)/int(Revenue1),2)
        Gross_Margin_ratio2 = round(int(Gross_Profit2)/int(Revenue2),2)
        Profit_Margin_ratio = round(int(Net_Income)/int(Revenue),2)
        Profit_Margin_ratio1 = round(int(Net_Income1)/int(Revenue1),2)
        Profit_Margin_ratio2 = round(int(Net_Income2)/int(Revenue2),2)
        Operating_Margin_ratio = round(int(Operating_Profit)/int(Revenue),2)
        Operating_Margin_ratio1 = round(int(Operating_Profit1)/int(Revenue1),2)
        Operating_Margin_ratio2 = round(int(Operating_Profit2)/int(Revenue2),2)
        Asset_Turn_Over_ratio = round(int(Revenue)/int(Total_Assets),2)
        Asset_Turn_Over_ratio1 = round(int(Revenue1)/int(Total_Assets1),2)
        Asset_Turn_Over_ratio2 = round(int(Revenue2)/int(Total_Assets2),2)
        Accounts_Receivable_Turnover_ratio =round(int(Revenue)/int(Accounts_Receivable),2)
        Accounts_Receivable_Turnover_ratio1 =round(int(Revenue1)/int(Accounts_Receivable1),2)
        Accounts_Receivable_Turnover_ratio2 =round(int(Revenue2)/int(Accounts_Receivable2),2)
        Days_Receivable_ratio = round(int(Accounts_Receivable)/int(Revenue)/365,2)
        Days_Receivable_ratio1 = round(int(Accounts_Receivable1)/int(Revenue1)/365,2)
        Days_Receivable_ratio2 = round(int(Accounts_Receivable2)/int(Revenue2)/365,2)
        Average_Day_Sales_ratio = round(int(Accounts_Payable)/int(Revenue),2) 
        Average_Day_Sales_ratio1 = round(int(Accounts_Payable1)/int(Revenue1),2)
        Average_Day_Sales_ratio2 = round(int(Accounts_Payable2)/int(Revenue2),2)
        Day_Payable_ratio = round(int(Accounts_Payable)/(int(Revenue)/365),2)
        Day_Payable_ratio1 = round(int(Accounts_Payable1)/(int(Revenue1)/365),2)
        Day_Payable_ratio2 = round(int(Accounts_Payable2)/(int(Revenue2)/365),2)
        Inventory_turnover_ratio = round(int(Revenue)/int(Inventory), 2)
        Inventory_turnover_ratio1 = round(int(Revenue1)/int(Inventory1), 2)
        Inventory_turnover_ratio2 = round(int(Revenue2)/int(Inventory2), 2)
        Inventory_turnover_period = round(1/Inventory_turnover_ratio, 2)
        Inventory_turnover_period1 = round(1/Inventory_turnover_ratio1, 2)
        Inventory_turnover_period2 = round(1/Inventory_turnover_ratio2, 2)
        working_capital_turnover_ratio = round(int(Revenue)/(int(Total_Current_Assets)-int(Total_Current_Liabilities)))
        print(working_capital_turnover_ratio)
        working_capital_turnover_ratio1 = round(int(Revenue1)/(int(Total_Current_Assets1)-int(Total_Current_Liabilities1)))
        working_capital_turnover_ratio2 = round(int(Revenue2)/(int(Total_Current_Assets2)-int(Total_Current_Liabilities2)))
        Debt_ratio = round(int(Current_Portion_Of_Long_Term_Debt)/int(Total_Assets),2)
        Debt_ratio1 = round(int(Current_Portion_Of_Long_Term_Debt1)/int(Total_Assets1),2)
        Debt_ratio2 = round(int(Current_Portion_Of_Long_Term_Debt2)/int(Total_Assets2),2)
        Debt_to_Equity_ratio = round(int(Current_Portion_Of_Long_Term_Debt)/int(Total_owners_equity),2)
        Debt_to_Equity_ratio1 = round(int(Current_Portion_Of_Long_Term_Debt1)/int(Total_owners_equity1),2)
        Debt_to_Equity_ratio2 = round(int(Current_Portion_Of_Long_Term_Debt2)/int(Total_owners_equity2),2)
    except Exception as e:
        print(e)

        #Context
    context = {
        'Revenue':Revenue,
        'Revenue1':Revenue1,
        'Revenue2':Revenue2,
        'beginninginventory_ratio':beginninginventory_ratio,
        'beginninginventory_ratio1':beginninginventory_ratio1,
        'beginninginventory_ratio2':beginninginventory_ratio2,
        'purchase_ratio':purchase_ratio,
        'purchase_ratio1':purchase_ratio1,
        'purchase_ratio2':purchase_ratio2,
        'freightExpenses_ratio':freightExpenses_ratio,
        'freightExpenses_ratio1':freightExpenses_ratio1,
        'freightExpenses_ratio2':freightExpenses_ratio2,
        'ending_Inventory_ratio':ending_Inventory_ratio,
        'ending_Inventory_ratio1':ending_Inventory_ratio1,
        'ending_Inventory_ratio2':ending_Inventory_ratio2,
        'billmaterils_ratio':billmaterils_ratio,
        'billmaterils_ratio1':billmaterils_ratio1,
        'billmaterils_ratio2':billmaterils_ratio2,
        'labourcharges_ratio':labourcharges_ratio,
        'labourcharges_ratio1':labourcharges_ratio1,
        'labourcharges_ratio2':labourcharges_ratio2,
        'labourchargesperworkinghour':labourchargesperworkinghour,
        'labourchargesperworkinghour1':labourchargesperworkinghour1,
        'labourchargesperworkinghour2':labourchargesperworkinghour2,
        'subcontractexpenses_ratio':subcontractexpenses_ratio,
        'subcontractexpenses_ratio1':subcontractexpenses_ratio2,
        'subcontractexpenses_ratio2':subcontractexpenses_ratio2,
        'costofgoodssold_ratio':costofgoodssold_ratio,
        'costofgoodssold_ratio1':costofgoodssold_ratio1,
        'costofgoodssold_ratio2':costofgoodssold_ratio2,
        'grossprofit_ratio':grossprofit_ratio,
        'grossprofit_ratio1':grossprofit_ratio1,
        'grossprofit_ratio2':grossprofit_ratio2,
        'businessdevelopment_ratio':businessdevelopment_ratio,
        'businessdevelopment_ratio1':businessdevelopment_ratio1,
        'businessdevelopment_ratio2':businessdevelopment_ratio2,
        'fuelexpenses_ratio':fuelexpenses_ratio,
        'fuelexpenses_ratio1':fuelexpenses_ratio1,
        'fuelexpenses_ratio2':fuelexpenses_ratio2,
        'conveyancexpenses_ratio':conveyancexpenses_ratio,
        'conveyancexpenses_ratio1':conveyancexpenses_ratio1,
        'conveyancexpenses_ratio2':conveyancexpenses_ratio2,
        'telephoneexpenses_ratio':telephoneexpenses_ratio,
        'telephoneexpenses_ratio1':telephoneexpenses_ratio1,
        'telephoneexpenses_ratio2':telephoneexpenses_ratio2,
        'sellingandadminexpenses_ratio':sellingandadminexpenses_ratio,
        'sellingandadminexpenses_ratio1':sellingandadminexpenses_ratio1,
        'sellingandadminexpenses_ratio2':sellingandadminexpenses_ratio2,
        'electricitycharges_ratio':electricitycharges_ratio,
        'electricitycharges_ratio1':electricitycharges_ratio1,
        'electricitycharges_ratio2':electricitycharges_ratio2,
        'vechilemanitainence_ratio':vechilemanitainence_ratio,
        'vechilemanitainence_ratio1':vechilemanitainence_ratio1,
        'vechilemanitainence_ratio2':vechilemanitainence_ratio2,
        'machinemaintainence_ratio':machinemaintainence_ratio,
        'machinemaintainence_ratio1':machinemaintainence_ratio1,
        'machinemaintainence_ratio2':machinemaintainence_ratio2,
        'rents_ratio':rents_ratio,
        'rents_ratio1':rents_ratio1,
        'rents_ratio2':rents_ratio2, 
        'consumable_ratio':consumable_ratio, 
        'consumable_ratio1':consumable_ratio1,
        'consumable_ratio2':consumable_ratio2,
        'bankcharges_ratio':bankcharges_ratio,
        'bankcharges_ratio1':bankcharges_ratio1,
        'bankcharges_ratio2':bankcharges_ratio2, 
        'otheroperatingexpenses_ratio':otheroperatingexpenses_ratio,
        'otheroperatingexpenses_ratio1':otheroperatingexpenses_ratio1,
        'otheroperatingexpenses_ratio2':otheroperatingexpenses_ratio2, 
        'ebitda_ratio':ebitda_ratio,
        'ebitda_ratio1':ebitda_ratio1,
        'ebitda_ratio2':ebitda_ratio2,
        'depreciation_ratio':depreciation_ratio,
        'depreciation_ratio1':depreciation_ratio1,
        'depreciation_ratio2':depreciation_ratio2, 
        'amortizationexpense_ratio':amortizationexpense_ratio,
        'amortizationexpense_ratio1':amortizationexpense_ratio1,
        'amortizationexpense_ratio2':amortizationexpense_ratio2, 
        'otherexpenses_ratio':otherexpenses_ratio, 
        'otherexpenses_ratio1':otherexpenses_ratio1,
        'otherexpenses_ratio2':otherexpenses_ratio2,
        'operatingProfit_ratio':operatingProfit_ratio,
        'operatingProfit_ratio1':operatingProfit_ratio1,
        'operatingProfit_ratio2':operatingProfit_ratio2, 
        'bank_Interest_Expense_ratio':bank_Interest_Expense_ratio,
        'bank_Interest_Expense_ratio1':bank_Interest_Expense_ratio1,
        'bank_Interest_Expense_ratio2':bank_Interest_Expense_ratio2,
        'other_Interest_Expense_ratio':other_Interest_Expense_ratio,
        'other_Interest_Expense_ratio1':other_Interest_Expense_ratio1,
        'other_Interest_Expense_ratio2':other_Interest_Expense_ratio2,
        'total_Interest_Expense_ratio':total_Interest_Expense_ratio,
        'total_Interest_Expense_ratio1':total_Interest_Expense_ratio1,
        'total_Interest_Expense_ratio2':total_Interest_Expense_ratio2,
        'Interest_Expense_per_hour':Interest_Expense_per_hour,
        'Interest_Expense_per_hour1':Interest_Expense_per_hour1,
        'Interest_Expense_per_hour2':Interest_Expense_per_hour2,
        'bank_Interest_Income_ratio':bank_Interest_Income_ratio,
        'bank_Interest_Income_ratio1':bank_Interest_Income_ratio1,
        'bank_Interest_Income_ratio2':bank_Interest_Income_ratio2, 
        'other_Interest_Income_ratio':other_Interest_Income_ratio, 
        'other_Interest_Income_ratio1':other_Interest_Income_ratio1,
        'other_Interest_Income_ratio2':other_Interest_Income_ratio2,
        'total_Interest_Income_ratio':total_Interest_Income_ratio,
        'total_Interest_Income_ratio1':total_Interest_Income_ratio1,
        'total_Interest_Income_ratio2':total_Interest_Income_ratio2, 
        'net_Income_Before_Taxes_ratio':net_Income_Before_Taxes_ratio,
        'net_Income_Before_Taxes_ratio1':net_Income_Before_Taxes_ratio1,
        'net_Income_Before_Taxes_ratio2':net_Income_Before_Taxes_ratio2, 
        'income_Tax_Expense_ratio':income_Tax_Expense_ratio,
        'income_Tax_Expense_ratio1':income_Tax_Expense_ratio1,
        'income_Tax_Expense_ratio2':income_Tax_Expense_ratio2,
        'net_Income_ratio':net_Income_ratio, 
        'net_Income_ratio1':net_Income_ratio1,
        'net_Income_ratio2':net_Income_ratio2,
        #balance sheet
        'Current_ratio':Current_ratio,
        'Current_ratio1':Current_ratio1,
        'Current_ratio2':Current_ratio2,
        'Quick_ratio':Quick_ratio,
        'Quick_ratio1':Quick_ratio1,
        'Quick_ratio2':Quick_ratio2,
        'Return_on_Assets_ratio':Return_on_Assets_ratio,
        'Return_on_Assets_ratio1':Return_on_Assets_ratio1,
        'Return_on_Assets_ratio2':Return_on_Assets_ratio2,
        'Return_on_Equity_ratio':Return_on_Equity_ratio,
        'Return_on_Equity_ratio1':Return_on_Equity_ratio1,
        'Return_on_Equity_ratio2':Return_on_Equity_ratio2,
        'Gross_Margin_ratio':Gross_Margin_ratio,
        'Gross_Margin_ratio1':Gross_Margin_ratio1,
        'Gross_Margin_ratio2':Gross_Margin_ratio2,
        'Profit_Margin_ratio':Profit_Margin_ratio,
        'Profit_Margin_ratio1':Profit_Margin_ratio1,
        'Profit_Margin_ratio2':Profit_Margin_ratio2,
        'Operating_Margin_ratio':Operating_Margin_ratio,
        'Operating_Margin_ratio1':Operating_Margin_ratio1,
        'Operating_Margin_ratio2':Operating_Margin_ratio2,
        'Asset_Turn_Over_ratio':Asset_Turn_Over_ratio,
        'Asset_Turn_Over_ratio1':Asset_Turn_Over_ratio1,
        'Asset_Turn_Over_ratio2':Asset_Turn_Over_ratio2,
        'Accounts_Receivable_Turnover_ratio':Accounts_Receivable_Turnover_ratio,
        'Accounts_Receivable_Turnover_ratio1':Accounts_Receivable_Turnover_ratio1,
        'Accounts_Receivable_Turnover_ratio2':Accounts_Receivable_Turnover_ratio2,
        'Average_Day_Sales_ratio':Average_Day_Sales_ratio,
        'Average_Day_Sales_ratio1':Average_Day_Sales_ratio1,
        'Average_Day_Sales_ratio2':Average_Day_Sales_ratio2,
        'Day_Receivable_ratio':Days_Receivable_ratio,
        'Day_Receivable_ratio1':Days_Receivable_ratio1,
        'Day_Receivable_ratio2':Days_Receivable_ratio2,         
        'Day_Payable_ratio':Day_Payable_ratio,
        'Day_Payable_ratio1':Day_Payable_ratio1,
        'Day_Payable_ratio2':Day_Payable_ratio2,
        'Inventory_turnover_ratio':Inventory_turnover_ratio,
        'Inventory_turnover_ratio1':Inventory_turnover_ratio1,
        'Inventory_turnover_ratio2':Inventory_turnover_ratio2,
        'Inventory_turnover_period':Inventory_turnover_period,
        'Inventory_turnover_period1':Inventory_turnover_period1,
        'Inventory_turnover_period2':Inventory_turnover_period2,
        'working_capital_turnover_ratio':working_capital_turnover_ratio,
        'working_capital_turnover_ratio1':working_capital_turnover_ratio1,
        'working_capital_turnover_ratio2':working_capital_turnover_ratio2,

        'Debt_ratio':Debt_ratio,
        'Debt_ratio1':Debt_ratio1,
        'Debt_ratio2':Debt_ratio2,
        'Debt_to_Equity_ratio':Debt_to_Equity_ratio,
        'Debt_to_Equity_ratio1':Debt_to_Equity_ratio1,
        'Debt_to_Equity_ratio2':Debt_to_Equity_ratio2

        }
             
    return render(request,'ratio.html', context)      
