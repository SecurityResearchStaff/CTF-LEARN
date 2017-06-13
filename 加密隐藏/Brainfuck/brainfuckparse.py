# -*- coding:utf-8 -*-

import os

'''
brainfuck语言解释器

用法：将brainfuck内容存入文本中，保存为.bf格式，然后运行run函数

'''


def mainloop(program, bracket_map):  
    pc = 0  
    tape = Tape()  
    while pc < len(program):  
        code = program[pc]  
        if code == ">":  
            tape.advance()  
        elif code == "<":  
            tape.devance()  
        elif code == "+":  
            tape.inc()  
        elif code == "-":  
            tape.dec()  
        elif code == ".":  
            os.write(1, chr(tape.get()))  
        elif code == ",":   
            tape.set(ord(os.read(0, 1)[0]))  
        elif code == "[" and tape.get() == 0:   
            pc = bracket_map[pc]  
        elif code == "]" and tape.get() != 0:  
            pc = bracket_map[pc]  
        pc += 1

class Tape(object):  
    def __init__(self):  
        self.thetape = [0]  
        self.position = 0  
    def get(self):  
        return self.thetape[self.position]  
    def set(self, val):  
        self.thetape[self.position] = val  
    def inc(self):  
        self.thetape[self.position] += 1  
    def dec(self):  
        self.thetape[self.position] -= 1  
    def advance(self):  
        self.position += 1  
        if len(self.thetape) <= self.position:  
            self.thetape.append(0)  
    def devance(self):  
        self.position -= 1

def parse(program):  
    parsed = []  
    bracket_map = {}  
    leftstack = []  
    pc = 0  
    for char in program:  
        if char in ('[', ']', '<', '>', '+', '-', ',', '.'):  
            parsed.append(char)  
            if char == '[':  
                leftstack.append(pc)  
            elif char == ']':  
                left = leftstack.pop()  
                right = pc  
                bracket_map[left] = right  
                bracket_map[right] = left  
            pc += 1  

    return "".join(parsed), bracket_map

def run(fp):  
    program_contents = ""  
    while True:  
        read = os.read(fp, 4096)  
        if len(read) == 0:  
            break  
        program_contents += read  
    os.close(fp)  
    program, bm = parse(program_contents)  
    mainloop(program, bm)  


if __name__=="__main__":
    '''
    传入.bf文件
    '''
    run(os.open("./1.bf", os.O_RDONLY, 0777))
