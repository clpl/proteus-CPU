import sys

instr_lst = open('terms.txt').readlines()

def run(filename):
    fin = open(filename)
    flag = 0 # 0 - pre; 1 - ongoing;

    for line in fin.readlines():
        
        line = line.strip()
        if line[0:2] == '//':
            continue
        if flag == 0:
            next_addr = line[0:6]
            flag = 1
            continue
        elif flag == 1:
            if line[1] == ':':


if __name__ == '__main__':
    run(sys.argv[1])
