def cost_delivery(quantity, *_, discount=0):
    first = 5
    next = 2
    delivery = first + (next * (quantity - 1))
    if discount == 0:
        return delivery
    else:
        discount_delivery = delivery * (1 - discount)
        return discount_delivery
    
    # result = (5 + 2 * (quantity - 1)) * (1 - discount)
    # return result