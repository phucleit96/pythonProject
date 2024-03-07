def unique_in_order(iterable):
    result = []
    if len(iterable) <= 1:
        return iterable
    else:
        for x in range(len(iterable)-1):
            if iterable[x] != iterable[x+1]:
                result.append[iterable[x]]
        return result

