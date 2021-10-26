# creditcalc
This is Loan Calculator project of the Python track of JetBrain Academy

Program to calculate different financial parameters.

In this stage, you are going to implement the following features:

Calculation of differentiated payments. To do this, the user can run the program specifying interest, number of monthly payments, and loan principal.
Calculate for annuity payment the principal, number of monthly payments, and monthly payment amount. The user specifies all the known parameters with command-line arguments, and one parameter will be unknown. This is the value the user wants to calculate.
Handling of invalid parameters. 

The program is supposed to work from the command line and parse the following parameters:

--type indicates the type of payment: "annuity" or "diff" (differentiated).

--payment is the monthly payment amount. 

--principal is used for calculations of both types of payment. You can get its value if you know the interest, annuity payment, and number of months.

--periods denotes the number of months needed to repay the loan. It's calculated based on the interest, annuity payment, and principal.

--interest is specified without a percent sign. Note that it can accept a floating-point value. Our loan calculator can't calculate the interest, so it must always be provided. 
