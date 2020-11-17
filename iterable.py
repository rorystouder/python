def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

#first(["1st", "2nd", "3rd"])
#first({"1st", "2nd", "3rd"})
#first(set()) throws error
