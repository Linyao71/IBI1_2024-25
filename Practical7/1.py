import sys
import re

# 读取输入文件
with open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r') as input_file:
    inp = input_file.read()

# 目标模式
tata = re.compile(r'TATA[AT]{1,2}', re.IGNORECASE)

# 输出文件
with open('tata_genes.fa', 'w') as output:
    currentseq = []
    currentname = ""

    for line in inp.splitlines():
        if re.match(r'>', line):  # 识别序列头
            if currentseq:
                full = ''.join(currentseq)
                if tata.search(full):
                    output.write(f"{currentname}\n{full}\n")
                currentseq = []

            find = re.search(r'gene:(\S+)', line)
            if find:
                currentname = find.group(1)
        else:
            currentseq.append(line.strip())  # 累积序列
