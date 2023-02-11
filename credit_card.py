# the below code is masked the digits of a credit card and leave only the last four..
credit_card = "9443-874-2105-8088"
def get_credit_card(a):
    last_credit_card = len(a[-4:])
    credit_card_length = len(a[:])
    masked_credit_card = credit_card_length - last_credit_card
    for i in range(masked_credit_card):
        print("*", end="")
    print(a[-4:])
    #print("Credit card numbers are: ", a)
    print("Credit card length is: ", credit_card_length)
    print("Last 4 digits are: ", a[-last_credit_card:])
    print("Masked credit card is: ", a[:masked_credit_card])
get_credit_card(credit_card)
