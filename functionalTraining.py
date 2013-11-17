__author__ = 'fpaulo'

class Monoid:
    def __init__(self, null, lift, op):
        self.null = null
        self.lift = lift
        self.op = op

    def fold(self, xs):
        if hasattr(xs, "__fold__"):
            return xs.__fold__(self)
        else:
            return reduce(self.op, (self.lift(x) for x in xs), self.null)

    def __call__(self, *args):
        return self.fold(args)

    def star(self):
        return Monoid(self.null, self.lift, self.op)


if __name__ == "__main__":
    #ints = [10,20,30,40]
    #letters = ["a","b","c"]
    #
    #adder = lambda x,y: x+y
    #
    #def reductor(list):
    #    return reduce(adder, list)
    #
    ##sum List(10,20,30,40) is 100
    #print 'Sum of list of ints:', reductor(ints)
    #
    ##sum List("a", "b", "c") is "abc"
    #print 'Sum of list of strings', reductor(letters)

    summ = Monoid(0, lambda x: x, lambda a, b: a + b)
    listm = Monoid([], lambda x: [x], lambda a, b: a + b)

    print listm([1],[2])



