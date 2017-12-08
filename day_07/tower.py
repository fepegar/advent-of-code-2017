import re

class Program:

    def __init__(self, name, weight=None, children=None):
        self.name = name
        self.weight = weight
        self.children = [] if children is None else children
        self.disc_weight = None


    def __repr__(self):
        return self.name


    def get_disc_weights(self):
        return [child.get_disc_weight() for child in self.children]


    def get_disc_weight(self):
        if self.disc_weight is None:
            children_weight = sum(self.get_disc_weights())
            self.disc_weight = self.weight + children_weight
        return self.disc_weight


    def is_balanced(self):
        return len(set(self.get_disc_weights())) == 1


    def find_guilty(self):
        if self.is_balanced():
            return self
        weights = self.get_disc_weights()
        fatter = self.children[weights.index(max(weights))]
        return fatter.find_guilty()



class Tower(list):

    def __init__(self, input_path):
        super().__init__()  # is this necessary?
        self.read_tower(input_path)


    def __contains__(self, program_name):
        for program in self:
            if program.name == program_name:
                return True
        return False


    def __repr__(self):
        strings = []
        for program in self:
            strings.append(program.__repr__())
        return '\n'.join(strings)


    def read_tower(self, input_path):
        with open(input_path) as f:
            lines = f.readlines()
        for line in lines:
            info = re.findall(r'(\w+)', line)
            parent_name = info[0]
            weight = int(info[1])
            if parent_name in self:
                parent = self.get_program(parent_name)
                parent.weight = weight
            else:
                parent = Program(parent_name, weight=weight)
                self.append(parent)
            holds_disk = len(info) > 2
            if holds_disk:
                children_names = info[2:]
                for child_name in children_names:
                    if child_name in self:
                        child = self.get_program(child_name)
                    else:
                        child = Program(child_name)
                        self.append(child)
                    parent.children.append(child)


    def get_program(self, program_name):
        for program in self:
            if program.name == program_name:
                return program
        return None


    def get_bottom(self):
        weights = [program.get_disc_weight() for program in self]
        return self[weights.index(max(weights))]


    def find_guilty(self):
        bottom = self.get_bottom()
        return bottom.find_guilty()


    def weight_to_balance(self):
        weights = self.get_bottom().get_disc_weights()
        difference = max(weights) - min(weights)
        program = self.find_guilty()
        return program.weight - difference
