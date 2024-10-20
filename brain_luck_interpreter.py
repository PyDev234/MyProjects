class Bfk_Interpreter:
    def __init__(self, inst_code = None, inp_stream = None):
        self.mem = [0 for i in range(30001)]
        self.out_buf = []
        self.ptr = 0
        self.inst_ptr = 0
        self.inst_code = inst_code
        if not inst_code: self.inst_code = input("Enter the bfk code: ")
        self.inst_code_len = len(self.inst_code)
        self.iptr = 0
        if inp_stream: self.inp_stream = inp_stream
        else:
            self.iptr = -1
            from sys import stdin
            self.inp_stream = stdin

    def inc_d(self):
        """Increment the data stored at current memory cell"""
        self.mem[self.ptr] = 0 if self.mem[self.ptr]==255 else (self.mem[self.ptr]+1)

    def dec_d(self):
        """Decrement the data stored at current memory cell"""
        self.mem[self.ptr] = (self.mem[self.ptr]-1) if self.mem[self.ptr] else 255
    
    def inc(self):
        """Increment the memory cell"""
        self.ptr = 0 if self.ptr==30000 else (self.ptr+1)

    def dec(self):
        """Decrement the memory cell"""
        self.ptr = (self.ptr-1) if self.ptr else 30000

    def out(self):
        """Prints the data at current memory cell"""
        self.out_buf.append(chr(self.mem[self.ptr]))

    def inp(self):
        if self.iptr>-1:
            assert self.iptr<len(self.inp_stream), "No Input EOF Reached!"
            self.mem[self.ptr] = ord(self.inp_stream[self.iptr])
            self.iptr += 1
        else:
            d = self.inp_stream.read(1)
            if d=='\n': d = self.inp_stream.read(1)
            assert d!='', "No Input EOF Reached!"
            self.mem[self.ptr] = ord(d)

    def jmp_forward(self):
        """Move the instruction pointer(in right direction) upto matching ']'"""
        l_brkt = 0
        self.inst_ptr += 1
        while (self.inst_ptr<self.inst_code_len) and (l_brkt>-1):
            l_brkt += (self.inst_code[self.inst_ptr]=='[') - (self.inst_code[self.inst_ptr]==']')
            self.inst_ptr += 1
        self.inst_ptr -= 1

    def jmp_backward(self):
        """Move the instruction pointer(in left direction) upto matching '['"""
        r_brkt = 0
        self.inst_ptr -= 1
        while (self.inst_ptr>-1) and (r_brkt>-1):
            r_brkt += (self.inst_code[self.inst_ptr]==']') - (self.inst_code[self.inst_ptr]=='[')
            self.inst_ptr -= 1
        self.inst_ptr += 1

    def exec_code(self):
        while (self.inst_ptr < self.inst_code_len):
            match(self.inst_code[self.inst_ptr]):
                case '>': self.inc()
                case '<': self.dec()
                case '+': self.inc_d()
                case '-': self.dec_d()
                case '.': self.out()
                case ',': self.inp()
                case '[': (self.jmp_forward() if self.mem[self.ptr]==0 else 0)
                case ']': (self.jmp_backward() if self.mem[self.ptr]!=0 else 0)
            self.inst_ptr += 1
        return "".join(self.out_buf)

    def printopt(self):
        self.exec_code()
        print("".join(self.out_buf))

if __name__ == '__main__':
    test_cases = {
        (",>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.", "\x08\x09"): 'H'
    }
    bfk = Bfk_Interpreter(",>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.", "\x08\x09")
    bfk.printopt()