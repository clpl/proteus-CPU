import sys

CHIP_NUM = 2                # 芯片数
BITS = 8                    # 芯片位数
FILE_PREFIX = 'MEM'         # 文件名前缀
MPG_BIT = 16                # 微指令位数

def run(filename):
    fin = open(filename)

    complete = ''
    for i in range(CHIP_NUM*BITS - MPG_BIT):
        complete = complete + '0'
    file_list = []
    for i in range(CHIP_NUM):
        file_list.append(open(FILE_PREFIX + str(i) + '.asm', 'w'))

    for line in fin.readlines():
        if line[0:4] == 'ADDR':
            for fout in file_list:
                fout.write('\n' + 'ORG ' + line[4:9] + 'H\n')
        elif len(line) >= MPG_BIT:
            line = complete + line
            for index, fout in enumerate(file_list):
                fout.write('    DB    ' + line[index*BITS:index*BITS+8] + 'B\n')

    fin.close()
    for fout in file_list:
        fout.write('END')
        fout.close()

if __name__ == '__main__':
    run('ins_bin.txt')
