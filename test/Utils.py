def int_generator(seed=1000):
    while True:
        yield seed
        seed += 1

def str_generator(ord_start=97, ord_end=122):
    if ord_start < 0 or ord_end > 0x10FFFF:
        raise ValueError("Ordinals are out of range.")
    if ord_end < ord_start:
        raise ValueError("ord_end must be no less than ord_start.")
    ords = [ord_start]
    generated = ''.join(map(chr, reversed(ords)))
    yield(generated)
    while True:
        idx = 0
        while True:
            if idx >= len(ords):
                ords.append(ord_start)
                break
            if ords[idx] == ord_end:
                ords[idx] = ord_start
                idx += 1
            else:
                ords[idx] += 1
                break
        generated = ''.join(map(chr, reversed(ords)))
        yield(generated)
