from lib.solutions.CHK.checkout_solution import CheckoutSolution

class TestCheckout():
    def test_checkout(self):
        assert CheckoutSolution.checkout(self, "AAABBC") == 195
        assert CheckoutSolution.checkout(self, "AAAAAD") == 215
        assert CheckoutSolution.checkout(self, "EEBCD") == 115
        assert CheckoutSolution.checkout(self, "FFFFF") == 40
        assert CheckoutSolution.checkout(self, "HHHHHH") == 55
        assert CheckoutSolution.checkout(self, "NNNMM") == 135
        assert CheckoutSolution.checkout(self, "RRRQQ") == 180
        assert CheckoutSolution.checkout(self, "STXSTX") == 90
        assert CheckoutSolution.checkout(self, "UUUUUU") == 200
        assert CheckoutSolution.checkout(self, "VVVKKB") == 280
