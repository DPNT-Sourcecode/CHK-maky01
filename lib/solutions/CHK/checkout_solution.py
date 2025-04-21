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

        total_price = 0
        for sku, count in sku_counts_dict.items():
            if sku in self.SPECIAL_OFFERS:
                offer_count, offer_price = self.SPECIAL_OFFERS[sku]
                num_offers = count // offer_count
                total_price += num_offers * offer_price
                count %= offer_count
            total_price += count * self.PRICES[sku]
        return total_price

# # test function
# if __name__ == "__main__":
#     checkout = CheckoutSolution()
#     skus = 'AABBCD'
#     print(checkout.checkout(skus))



    

