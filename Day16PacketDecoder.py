from copy import deepcopy

dict = [['0', '0000'], ['1', '0001'], ['2', '0010'], ['3', '0011'], ['4', '0100'], ['5', '0101'], ['6', '0110'],
        ['7', '0111'], ['8', '1000'], ['9', '1001'], ['A', '1010'], ['B', '1011'], ['C', '1100'], ['D', '1101'],
        ['E', '1110'], ['F', '1111']]

with open("day16PacketTest.txt") as f:
    raw_data = f.read().strip()

data = bin(int(raw_data, base=16))[2:]
data = data.zfill(-(-len(data) // 4) * 4)


def parse(decrypted_packet, count):
    if decrypted_packet == "" or int(decrypted_packet) == 0:
        return 0
    if count == 0:
        return parse(decrypted_packet, count=-1)

    Version = int(decrypted_packet[0:3], 2)
    Type = int(decrypted_packet[3:6], 2)

    if Type == 4:
        idx = 6
        packet_value = ''
        check = True
        while check:
            if decrypted_packet[idx] == "0":
                check = False
            packet_value += decrypted_packet[idx + 1:idx + 5]
            idx += 5
        packet_value = int(packet_value, 2)
        return Version + parse(decrypted_packet[idx:], count=-1)

    I = int(decrypted_packet[6], 2)
    if I == 0:
        packet_value = int(decrypted_packet[7:22], 2)
        return Version + parse(decrypted_packet[22:22 + packet_value], -1) + parse(decrypted_packet[22 + packet_value:],
                                                                                   count=-1)

    elif I == 1:
        packet_value = int(decrypted_packet[7:18], 2)
        return Version + parse(decrypted_packet[18:], count=packet_value)


def operate(Type, values):
    if Type == 0:
        return sum(values)
    elif Type == 1:
        r = 1
        for v in values:
            r *= v
        return r
    elif Type == 2:
        return min(values)
    elif Type == 3:
        return max(values)
    elif Type == 5:
        assert len(values) == 2
        return int(values[0] > values[1])
    elif Type == 6:
        assert len(values) == 2
        return int(values[0] < values[1])
    elif Type == 7:
        assert len(values) == 2
        return int(values[0] == values[1])


def parseSum(i, j=-1):

    if i == j:
        return None, None

    if i > len(data) - 4:
        return None, None

    Version = int(data[i + 0: i + 3], 2)
    Type = int(data[i + 3:i + 6], 2)

    if Type == 4:
        i += 6
        packet_value = ""
        check = True
        while check:
            if data[i] == "0":
                check = False
            packet_value += data[i + 1:i + 5]
            i += 5

        packet_value = int(packet_value, 2)
        return packet_value, i

    sub_packets = []
    next_start = None
    I = int(data[i + 6], 2)
    if I == 0:
        packet_value = int(data[i + 7:i + 22], 2)
        end = i + 22 + packet_value
        idx = i + 22
        prev_idx = None
        while idx != None:
            prev_idx = idx
            x, idx = parseSum(idx, j=end)
            sub_packets.append(x)
        sub_packets = sub_packets[:-1]
        next_start = prev_idx

    else:
        packet_value = int(data[i + 7:i + 18], 2)
        idx = i + 18
        while packet_value > 0:
            x, idx = parseSum(idx)
            packet_value -= 1
            sub_packets.append(x)
        next_start = idx

    return operate(Type, sub_packets), next_start




result1 = parseSum(0)[0]
print(result1)
