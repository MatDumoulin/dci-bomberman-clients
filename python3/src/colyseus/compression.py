from fossil_delta import create_delta, apply_delta

class Compression:

    @staticmethod
    def hydrate(prev, delta):
        return apply_delta(prev, delta)
