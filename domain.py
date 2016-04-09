class Domain:
    @classmethod
    def get_default_domain(self, n):
        result = {}
        for i in range(n):
            for j in range(n):
                result[(i, j)] = [ (x/n, x%n) for x in range(n*n)]
        return result
    @classmethod
    def print_domain(self, domain):
        pass
