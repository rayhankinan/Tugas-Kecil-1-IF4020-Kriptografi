from ..lib import alru_cache_typed


@alru_cache_typed()
async def repeat_add(num: int, shift: int, addition: int):
    result = num
    for i in range(shift):
        result += (addition << (8 * i))
    return result


@alru_cache_typed()
async def repeat_subtract(num: int, shift: int, deduction: int):
    result = num
    for i in range(shift):
        result -= (deduction << (8 * i))
    return result
