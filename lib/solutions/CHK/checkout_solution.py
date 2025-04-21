class CheckoutSolution:
    # skus = unicode string
    def checkout(self, skus):
        self.PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
        self.SPECIAL_OFFERS_DISCOUNT = {'A': [(5, 200), (3, 130)], 'B': [(2, 45)]}
        self.SPECIAL_OFFERS_FREE = {'E': (2, 'B')}

        # Check to see input is a string
        if not isinstance(skus, str):
            return -1

        # Create a dictionary with zero count for each SKU
        sku_counts_dict = {sku: 0 for sku in self.PRICES.keys()}

        # Check to see if each SKU is in the PRICES dictionary and add to count of each SKU is it is
        for char in skus:
            if char not in self.PRICES:
                return -1
            sku_counts_dict[char] += 1

        print(f"SKU counts: {sku_counts_dict}")

        for sku, count in sku_counts_dict.items():
            if sku in self.SPECIAL_OFFERS_FREE:
                free_count, free_sku = self.SPECIAL_OFFERS_FREE[sku]
                print(f"Free offer: {sku} for {free_sku}")
                free_items = count // free_count
                print(f"Free items: {free_items}")
                sku_counts_dict[free_sku] = max(0, sku_counts_dict[free_sku] - free_items)
                print(f"Updated {free_sku} count: {sku_counts_dict[free_sku]}")

        total_price = 0
        for sku, count in sku_counts_dict.items():
            if sku in self.SPECIAL_OFFERS_DISCOUNT:
                offers = self.SPECIAL_OFFERS_DISCOUNT[sku]
                for offer_count, offer_price in offers:
                    num_offers = count // offer_count
                    total_price += num_offers * offer_price
                    count %= offer_count

            total_price += count * self.PRICES[sku]
        return total_price

# # test function
# if __name__ == "__main__":
#     checkout = CheckoutSolution()
#     print(checkout.checkout("EE"))
#     print(checkout.checkout("EEB"))
#     print(checkout.checkout("EEBB"))
#     print(checkout.checkout("EEBBB"))
#     print(checkout.checkout("AABBEE"))






