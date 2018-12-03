# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 21:10:03 2018

@author: Garrett
"""

class DictionaryDescriber:
    
    def __init__(self, obj, original=True):
        self.blue_print = {}
        self.max_depth = 0
        self.obj = obj
        self.num_els = 0
        self.original=original
        self.indent_dict = {}
        self.indent_count = 0

    
    def summarize_dict(self, current_depth=1, depth=0, verbose=True, original=True):
        if isinstance(self.obj, dict):
            self.max_depth = depth
            for key, val in self.obj.iteritems():
                self.num_els+=1
                temp_obj = DictionaryDescriber(val)
                temp_obj.summarize_dict(depth+1, 0, verbose, False)
                if temp_obj.max_depth+current_depth>self.max_depth:
                    self.max_depth = temp_obj.max_depth+current_depth
        else:
            return
        if verbose:
            print 'Object: ' + str(self.obj)
            print 'Max Depth: ' + str(self.max_depth)
            print 'Number of Elements: ' + str(self.num_els)
        else:
            if original:
                print 'Object: ' + str(self.obj)
                print 'Max Depth: ' + str(self.max_depth)
                print 'Number of Elements: ' + str(self.num_els)
                
    def _get_tree(self, current_depth=0):
        self.blue_print[current_depth] = []
        if isinstance(self.obj, dict):
            self.blue_print[current_depth].append(self.obj.keys())
            for key, val in self.obj.iteritems():
                temp_obj = DictionaryDescriber(val, original=False)
                temp_obj._get_tree(current_depth+1)
                try:
                    if len(temp_obj.blue_print[current_depth+1])>0:
                        self.blue_print[(current_depth+1, key)].append(temp_obj.blue_print)
                except KeyError:
                    if len(temp_obj.blue_print[current_depth+1])>0:
                        self.blue_print[(current_depth+1, key)] = []
                        self.blue_print[(current_depth+1, key)].append(temp_obj.blue_print)

        else:
            return
        if self.original:
            return self.blue_print
            
    """def print_tree(self):
        tree = self._get_tree()
        #print 'Tree'
        #print tree
        for key in sorted(tree.iterkeys()):
            for l in tree[key]:
                for el in l:
                    print el,
        for key in sorted(tree.iterkeys()):
            for l in tree[key]:
                for el in l:
                    print el,
                    try:
                        if isinstance(self.obj[el], dict):
                            temp_obj = DictionaryDescriber(self.obj[el])
                            temp_obj.print_tree()
                    except KeyError:
                            pass
            print"""
                
    """def _get_indent_dict(self, tree, indent_count=0, original=False):
        for key in sorted(tree.iterkeys()):
            val = tree[key]
            for l in val:
                if isinstance(l, dict):
                        #sub_tree = DictionaryDescriber(tree, original=False)
                        self._get_indent_dict(l, indent_count, False)
                else:
                    for el in l:
                        if isinstance(el, tuple):
                            self.indent_dict[el[1]] = indent_count
                        else:
                            self.indent_dict[el] = indent_count
                            #return self.indent_count
                        indent_count+=1
                indent_count+=1
        if original:
            print 'Indent Dict'
            print self.indent_dict
            """
    def _get_indent_dict(self, tree, original=False):
        for key in sorted(tree.iterkeys()):
            self.indent_dict[key] = self.indent_count
            val = tree[key]
            if isinstance(val, dict):
                self._get_indent_dict(val, False)
            else:
                self.indent_dict[key] = self.indent_count
            self.indent_count+=1
        if original:
            return self.indent_dict   
    
    def print_tree(self, pre_tree=None, indent_dict=None):
        if pre_tree is None:
            tree = self._get_tree()
        else:
            tree = pre_tree
        if tree is None:
            return
        else:
            if indent_dict is None:
                indent_dict = self._get_indent_dict(self.obj, True)
        for key in sorted(tree.iterkeys()):
            for l in tree[key]:
                if isinstance(l, dict):
                    temp_obj = DictionaryDescriber(l, original=True)
                    temp_obj.print_tree(l, indent_dict)
                else:
                    prev_tabs = 0
                    for el in sorted(l):
                        tabs = indent_dict[el]
                        print '\t'*(tabs-prev_tabs) + el,
                        prev_tabs = tabs
            print
            for el in l:
                    try:
                        if isinstance(self.obj[el], dict):
                            temp_obj = DictionaryDescriber(self.obj[el], original=False)
                            temp_obj.print_tree()
                    except KeyError:
                            pass
        #print indent_dict
        
        

def _test(verbose=True):
    test_dict = {'one':1, 'two':2, 'three':{'four':4, 'five':5, 'six':{'seven':7}}}
    test_dict2 = {'1': 1, 'b':{'2':2, '3': 3, 'c':{'4' :4, 'd':{'5':5}}}, '6': 6}
    empty_dict = {}
    one_level_dict = {'1': 1, '2': 2}
    multi_level = {'one':1, 'two':{'a':'aye', 'b':'bee'}, 'three':{'c':'see', 'd':'dee'}, 'four':4}
    test_obj = DictionaryDescriber(test_dict)
    print 'Test Raw'
    print test_dict
    #test_obj.summarize_dict(verbose=verbose)
    print 'Test Tree' 
    print test_obj._get_tree()
    print 'Print Test Tree'
    test_obj.print_tree()
    print
    test_obj2 = DictionaryDescriber(test_dict2)
    #print test_dict2
    #test_obj2.summarize_dict(verbose=verbose)
    #test_obj2.print_tree()
    #print test_obj2._get_tree()
    #print
    test_empty = DictionaryDescriber(empty_dict)
    #print empty_dict
    #test_empty.summarize_dict(verbose=verbose)
    test_empty.print_tree()
    #print test_empty._get_tree()
    #print
    #test_one = DictionaryDescriber(one_level_dict)
    #print one_level_dict
    #test_one.summarize_dict(verbose=verbose)
    #test_one.print_tree()
    #print test_one._get_tree()
    print
    test_multi = DictionaryDescriber(multi_level)
    print 'Multi Level Raw'
    print multi_level
    print 'Get Tree'
    print test_multi._get_tree()
    print 'Print Tree'
    test_multi.print_tree()
    

if __name__ == '__main__':
    _test()
    #_test(verbose=False)