class Mathematician:
    def square_nums(self, numbers):
        return [n*n for n in numbers]


m = Mathematician()

# m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
print(m.square_nums([7, 11, 5, 4]))
