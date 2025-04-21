import collections

class CheckoutSolution:

    PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    SPECIAL_OFFERS = {'A': (3, 130), 'B': (2, 45)}

    # skus = unicode string
    def checkout(self, skus):

        # Check to see input is a string
        if not isinstance(skus, str):
            return -1

        # Create a dictionary to count the number of each SKU
        sku_counts_dict = collections.Counter()

        # Check to see if each SKU is in the PRICES dictionary and add to count of each SKU is it is
        for char in skus:
            if char not in self.PRICES:
                return -1
            sku_counts_dict[char] += 1
        
        print (sku_counts_dict)


        # sku_counts = tuple()


# check to see if input is valid, return -1 if not valid
#   check each character in skus is in PRICES

# Sum each character


# Calculate total price with discounts


    
