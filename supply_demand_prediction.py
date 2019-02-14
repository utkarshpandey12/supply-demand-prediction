"model = -0.09928789*(Month)^(-5) + 1.4858187*(Skillset)^(-5) - 0.3368483*(location)^(-5) + 2.511014"

jan_pred = []
feb_pred = []
mar_pred = []
apr_pred = []
may_pred = []
jun_pred = []
jul_pred = []
aug_pred = []
sep_pred = []
oct_pred = []
nov_pred = []
dec_pred = []
"prediction of demand for 8 locations for candidates belonging to skillist no 166"
"based on weights and intercept calculated in source.py file"
for i in range(8):
 i = i+1
 jan_pred.append(round(-0.09928789*(1**-5) + 1.4858187*(166**-5) - 0.3368483*(i**-5) + 2.511014))
 feb_pred.append(round(-0.09928789*(2**-5) + 1.4858187*(166**-5) - 0.3368483*(i**-5) + 2.511014))
 mar_pred.append(round(-0.09928789*(3**-5) + 1.4858187*(166**-5) - 0.3368483*(i**-5) + 2.511014))
 apr_pred.append(round(-0.09928789*(4**-5) + 1.4858187*(166**-5) - 0.3368483*(i**-5) + 2.511014))
 may_pred.append(round(-0.09928789*(5**-5) + 1.4858187*(166**-5) - 0.3368483*(i**-5) + 2.511014))
 jun_pred.append(round(-0.09928789*(6**-5) + 1.4858187*(166**-5) - 0.3368483*(i**-5) + 2.511014))
 jul_pred.append(round(-0.09928789*(7**-5) + 1.4858187*(166**-5) - 0.3368483*(i**-5) + 2.511014))
 aug_pred.append(round(-0.09928789*(8**-5) + 1.4858187*(166**-5) - 0.3368483*(i**-5) + 2.511014))
 sep_pred.append(round(-0.09928789*(9**-5) + 1.4858187*(166**-5) - 0.3368483*(i**-5) + 2.511014))
 oct_pred.append(round(-0.09928789*(10**-5) + 1.4858187*(166**-5) - 0.3368483*(i**-5) + 2.511014))
 nov_pred.append(round(-0.09928789*(11**-5) + 1.4858187*(166**-5) - 0.3368483*(i**-5) + 2.511014))
 dec_pred.append(round(-0.09928789*(12**-5) + 1.4858187*(166**-5) - 0.3368483*(i**-5) + 2.511014))
print("Below are the predicted demand of skillset no 166 for 12 months period and are generated using weights and intercept given by source.py")
print(jan_pred)
print(feb_pred)
print(mar_pred)
print(apr_pred)
print(may_pred)
print(jun_pred)
print(jul_pred)
print(aug_pred)
print(sep_pred)
print(oct_pred)
print(nov_pred)
print(dec_pred)

"As described earlier instead of treating all 396 bench candidates we will only"
"consider 14 bench candidates for supply analysis. These 14 candidates information"
"can be inferred from demandv1.1 updated excel file "
"Out of these 14 bench candidates 0 belong to bangalore , 4 to bhubaneswar , 3 from pune "
" 2 from noida , 3 from gurgaon , 1 from hyderabad  , 0 from chennai and 1 from Hartford"
"these candiadte informatio will form our initial supply "

"initial supply for 8 cities for 14 bench candidates"

supply = [0,4,3,2,3,1,0,1]
"this funtion implements supply management based on demand of N+2"
"and also subtracts current month demand "
"list1 is current supply available , list2 is demand prediction for N+2 month"
"and list3 is current month demand i.e Nth month demand which will be "
"subtracted from the current month supply"
"This assumes current month demand is met at last and supply is mapped first"
"the montly expense borne by company in order to maintain"
"bench candidateswill be calculated assuming demand is met on last day of the month"
"For example new hiring takes place on 1st of every month and demand is met on "
"last day of the month so company cost will be calculated for previous bench +"
"newhires people cost"
def supply_management(list1,list2,list3):
    newhire = [0,0,0,0,0,0,0,0]
    o = []
    "check for shortage in supply according to N+2 month demand"
    for i in range(8):
        if list1[i]-list2[i]<0:
            newhire[i]  = list2[i]-list1[i]
    total_hired_candidate =0
    for i in range(8):
       "updating supply to current demand needs based on newhire requirement" 
       list1[i] = list1[i]+newhire[i]
       total_hired_candidate += newhire[i]
       o.append(list1[i])  
    "subtracting Nth month demand which will serve as list1 for next month"
    for i in range(8):
        if list1[i]-list3[i]>0:
            list1[i] = list1[i]-list3[i]
        else:
            list1[i] = 0
            
    "Final bench strength is calculated at end of month"
    final_bench_month = 0
    for i in range(8):
        final_bench_month += list1[i]
        
    return list1,o,total_hired_candidate,final_bench_month
"all 12 months supply analysis based on N+2 Demand"
print("Below are the optimised supply plan according to demand plan which is mapped according to N+2 method so that supply chain efficiency is increased")
listed1,jan_supply,jan_hired_candidate,jan_final_bench = supply_management(supply,mar_pred,jan_pred)
janu =listed1
print(jan_supply)
listed2,feb_supply,feb_hired_candidate,feb_final_bench = supply_management(janu,apr_pred,feb_pred)
febr =listed2
print(feb_supply)
listed3,mar_supply,mar_hired_candidate,mar_final_bench = supply_management(febr,may_pred,mar_pred)
marc =listed3
print(mar_supply)
listed4,apr_supply,apr_hired_candidate,apr_final_bench = supply_management(marc,jun_pred,apr_pred)
apri = listed4
print(apr_supply)
listed5,may_supply,may_hired_candidate,may_final_bench = supply_management(apri,jul_pred,may_pred)
may =listed5
print(may_supply)
listed6,jun_supply,jun_hired_candidate,jun_final_bench = supply_management(may,aug_pred,jun_pred)
june=listed6
print(jun_supply)
listed7,jul_supply,jul_hired_candidate,jul_final_bench = supply_management(june,sep_pred,jul_pred)
july =listed7
print(jul_supply)
listed8,aug_supply,aug_hired_candidate,aug_final_bench = supply_management(july,oct_pred,aug_pred)
augu = listed8
print(aug_supply)
listed9,sep_supply,sep_hired_candidate,sep_final_bench = supply_management(augu,nov_pred,sep_pred)
sept = listed9
print(sep_supply)
listed10,oct_supply,oct_hired_candidate,oct_final_bench = supply_management(sept,dec_pred,oct_pred)
octo = listed10
print(oct_supply)
listed11,nov_supply,nov_hired_candidate,nov_final_bench = supply_management(octo,jan_pred,nov_pred)
nove = listed11
print(nov_supply)
listed12,dec_supply,dec_hired_candidate,dec_final_bench = supply_management(nove,feb_pred,dec_pred)
print(dec_supply)
" list containing all bench at end of each month which will be used in"
"calculating expenses"
total_bench_candidates_unbilled_monthly = [jan_final_bench
,feb_final_bench,mar_final_bench,apr_final_bench,may_final_bench,
jun_final_bench,jul_final_bench,aug_final_bench,sep_final_bench,oct_final_bench,
nov_final_bench,dec_final_bench]

"expense for a month will be calculated for on account of no of candidates which "
"are new hires for that month + unbilled candidates"
"assuming attrition to be 20% every month uniformly"

def monthly_expenditure(monthly_bench,rate,hires,attrition):
    
    expense_monthly = monthly_bench*rate + hires*rate-0.2*(monthly_bench+hires)*rate
    expense_monthly = expense_monthly/(10**5)
    return expense_monthly
print("Below is the monthly expenses incurred each month in lakhs of $ units ")
jan_expense= monthly_expenditure(jan_final_bench,685,jan_hired_candidate,0.2)
print(jan_expense)
feb_expense= monthly_expenditure(feb_final_bench,685,feb_hired_candidate,0.2)
print(feb_expense)
mar_expense= monthly_expenditure(mar_final_bench,685,mar_hired_candidate,0.2)
print(mar_expense)
apr_expense= monthly_expenditure(apr_final_bench,685,apr_hired_candidate,0.2)
print(apr_expense)
may_expense= monthly_expenditure(may_final_bench,685,may_hired_candidate,0.2)
print(may_expense)
jun_expense= monthly_expenditure(jun_final_bench,685,jun_hired_candidate,0.2)
print(jun_expense)
jul_expense= monthly_expenditure(jul_final_bench,685,jul_hired_candidate,0.2)
print(jul_expense)
aug_expense= monthly_expenditure(aug_final_bench,685,aug_hired_candidate,0.2)
print(aug_expense)
sep_expense= monthly_expenditure(sep_final_bench,685,sep_hired_candidate,0.2)
print(sep_expense)
oct_expense= monthly_expenditure(oct_final_bench,685,oct_hired_candidate,0.2)
print(oct_expense)
nov_expense= monthly_expenditure(nov_final_bench,685,nov_hired_candidate,0.2)
print(nov_expense)
dec_expense= monthly_expenditure(dec_final_bench,685,dec_hired_candidate,0.2)
print(dec_expense)

total_expense_annualy = jan_expense+feb_expense+mar_expense+apr_expense+may_expense+jun_expense+jul_expense+aug_expense+sep_expense+oct_expense+nov_expense+dec_expense
"The recalculated budget for 14 bench candidates as mentioned in ppt"
budget = 2.01
gain_loss = (total_expense_annualy-budget)*100/(budget)
if total_expense_annualy>budget:
    print("Supply chain is suffering reported loss estimated anually is %d percent approximately and total expense is %f lakhs $U.S" %(-gain_loss,total_expense_annualy))
elif total_expense_annualy==budget:
    print('supply chain is just doing fair job profit is 0 %')
else:
    print("supply chain is doing great reported profits  anually is approximately %d percent and total expense is %f lakhs $U.S" %(-gain_loss,total_expense_annualy))
























 
