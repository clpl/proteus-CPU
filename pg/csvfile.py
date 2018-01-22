import sys

terms = open('terms.txt').readlines()
for i in range(len(terms)):
    terms[i] = terms[i].strip()
instr_lst = terms[1:9]
ins_bus_in = terms[11:16]
ins_bus_out = terms[18:24]

all_instr = {}

def put_hex(num):
    s = hex(int(num, 2))[2:]
    for i in range(4 - len(s)):
        s = '0' + s
    return s

def put_hex_(num):
    s = hex(num)[2:]
    for i in range(4 - len(s)):
        s = '0' + s
    return s

def put_bin(num, width):
    s = bin(num)[2:]
    for i in range(width - len(s)):
        s = '0' + s
    return s


def run(filename):
    fin = open(filename)
    fout = open('pyOut.csv', 'w')

    flag = 0 # 0 - pre; 1 - ongoing;
    active_instr = set()
    A = '000000'
    P = '000'
    N = '000000'
    bus_in = '111'
    bus_out = '1111'
    cur_addr = '000000'

    for line in fin.readlines():
        line = line.strip()
        if len(line) < 2:
            continue
        if line[0:2] == '//':
            fout.write(line[2:] + '\n')
            continue
        if flag == 0:
            cur_addr = line[0:6]
            flag = 1
            continue
        elif flag == 1:
            if line == 'end':
                # fout.write('ADDR ' + put_hex(cur_addr) + 'H\n')
                ins = A
                for instr in instr_lst:
                    if instr in active_instr:
                        ins = ins + '1'
                    else:
                        ins = ins + '0'
                for instr in active_instr:
                    if instr in ins_bus_in:
                        bus_in = put_bin(ins_bus_in.index(instr), 3)
                    if instr in ins_bus_out:
                        bus_out = put_bin(ins_bus_out.index(instr), 4)
                ins = ins + bus_in + bus_out + P + N
                fout.write(',' + ','.join(list(ins)) + '\n')
                all_instr[int(cur_addr, 2)] = ins
                flag = 0
                active_instr = set()
                A = '000000'
                P = '000'
                N = '000000'
                bus_in = '111'
                bus_out = '1111'
                cur_addr = '000000'
                continue
            if line[1] == ':':
                if line[0] == 'P':
                    P = line[2:5]
                elif line[0] == 'A':
                    A = line[2:8]
                elif line[0] == 'N':
                    N = line[2:8]
                continue
            if (line not in instr_lst) and (line not in ins_bus_in) and (line not in ins_bus_out):
                print(line + ' 指令未找到！')
            active_instr.add(line)

    # for cur_addr in sorted(list(all_instr.keys())):
    #     fout.write('ADDR ' + put_hex_(cur_addr) + 'H\n')
    #     fout.write(all_instr[cur_addr] + '\n')

if __name__ == '__main__':
    run('input.txt')
