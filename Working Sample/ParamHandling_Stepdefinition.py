from behave import *


@given(u'a customer has an {arg1} balance of ${arg2}')
def step_impl(context, arg1,numArg1):
    print(arg1)
    print(numArg1)


@when(u'the customer withdraws ${arg1} from the ATM')
def the_customer_withdraws_10_from_the_atm(context,arg1):
    print(arg1)


@then(u'the "account" balance should be ${arg1}')
def step_impl(context,arg1):
    print(arg1)


@given(u'the user is on the search page')
def step_impl(context):
    print('the user is on the search page')


@when(u'the user searches for {term}')
def step_impl(context,term):
    print(term)


@then(u'results for {term} are displayed')
def step_impl(context,term):
    print(term)

@given(u'a customer adds the following items to the cart')
def step_impl(context):
    for row in context.table:
        item = row['Item']
        quantity = row['Quantity']
        print(f"Item: {item}, Quantity: {quantity}")

@given(u'customer checks out')
def step_impl(context):
    print('customer checks out')

@given(u'log out')
def step_impl(context):
    print('log out')
  

#python -m behave --no-capture --no-color ParamHandling.feature