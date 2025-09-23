from JackConstant import *


class SymbolTable(object):
    def __init__(self):
        self.class_scope = {}
        self.subroutine_scope = {}
        self.symbols = {
            SK_STATIC: self.class_scope,
            SK_FIELD: self.class_scope,
            SK_ARG: self.subroutine_scope,
            SK_VAR: self.subroutine_scope
        }
        self.index = {
            SK_STATIC: 0,
            SK_FIELD: 0,
            SK_ARG: 0,
            SK_VAR: 0
        }

    def symbol_string(self, name, table):
        result = 'symbol table '+name+':\n'
        for n, (t, k, i) in table.items():
            result += 'symbol name:'+n+', type:' + \
                t+', kind:'+k+', index:'+str(i)+'\n'
        return result

    def __str__(self):
        return self.symbol_string('class', self.class_symbols)    \
            + self.symbol_string('subroutine', self.subroutine_symbols)

    def start_subroutine(self):
        """Starts a new subroutine scope (i.e., resets the subroutine's symbol table)."""
        self.subroutine_scope.clear()
        self.index[SK_ARG] = 0
        self.index[SK_VAR] = 0

    def define(self, name, type, kind):
        """Defines a new identifier of a given name, type and kind and assigns it a running index.
        # STATIC and FIELD identifiers have a class scope, while ARG and VAR identifiers have a subroutine scope."""
        # if kind not in self.symbols:
        #     raise ValueError(f"Invalid symbol kind: {kind}")
        # table = self.symbols[kind]
        # idx = self.index[kind]
        # table[name] = (type, kind, idx)
        # self.index[kind] += 1
        self.symbols[kind][name] = (type, kind, self.index[kind])
        self.index[kind] += 1

    def var_count(self, kind):
        """Returns the number of variables of the given kind already defined in the current scope."""
        if kind not in self.symbols:
            raise ValueError(f"Invalid symbol kind: {kind}")
        return self.index[kind]

    def lookup(self, name):
        """Returns the (type, kind, index) of the named identifier in the current scope."""
        if name in self.subroutine_scope:
            return self.subroutine_scope[name]
        elif name in self.class_scope:
            return self.class_scope[name]
        else:
            return (None, None, None)

    def type_of(self, name):
        """Returns the type of the named identifier in the current scope."""
        (type, kind, index) = self.lookup(name)
        return type

    def kind_of(self, name):
        (type, kind, index) = self.lookup(name)
        return kind

    def index_of(self, name):
        (type, kind, index) = self.lookup(name)
        return index
