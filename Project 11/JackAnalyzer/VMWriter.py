# VM Code Generator

import os


class VMWriter(object):

    def __init__(self):
        pass

    def openout(self, file):
        self._outfile = open(file.replace('.jack', '.vm'), 'w')

    def write_vm_cmd(self, cmd, arg1='', arg2=''):
        self._outfile.write(cmd+' '+str(arg1)+' '+str(arg2)+'\n')

    def write_push(self, segment, index):
        """Writes a VM push command."""
        self.write_vm_cmd('push', segment, index)

    def write_pop(self, segment, index):
        """Writes a VM pop command."""
        self.write_vm_cmd('pop', segment, index)

    def write_arithmetic(self, op):
        """Writes a VM arithmetic command."""
        self.write_vm_cmd(op)

    def write_label(self, label):
        """Writes a VM label command."""
        self.write_vm_cmd('label', label)

    def write_goto(self, label):
        """Writes a VM goto command."""
        self.write_vm_cmd('goto', label)

    def write_if(self, label):
        """Writes a VM if-goto command."""
        self.write_vm_cmd('if-goto', label)

    def write_call(self, name, n_args):
        """Writes a VM call command."""
        self.write_vm_cmd('call', name, n_args)

    def write_function(self, name, n_locals):
        """Writes a VM function command."""
        self.write_vm_cmd('function', name, n_locals)

    def write_return(self):
        """Writes a VM return command."""
        self.write_vm_cmd('return')

    def closeout(self):
        """Closes the output file/stream."""
        self._outfile.close()

    def push_const(self, val):
        self.write_push('constant', val)

    def push_arg(self, arg_num):
        self.write_push('argument', arg_num)

    def push_this_ptr(self):
        self.write_push('pointer', 0)

    def pop_this_ptr(self):
        self.write_pop('pointer', 0)

    def pop_that_ptr(self):
        self.write_pop('pointer', 1)

    def push_that(self):
        self.write_push('that', 0)

    def pop_that(self):
        self.write_pop('that', 0)

    def push_temp(self, temp_num):
        self.write_push('temp', temp_num)

    def pop_temp(self, temp_num):
        self.write_pop('temp', temp_num)
