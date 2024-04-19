import sys
sys.path.insert(1, '/home/ruby/school/practical_programming/wgc')

from forms.integer_form import IntegerForm

"""Testing the integer form"""
def test_integer_form():
    """
    Tests good an bad user inputs.
    Only postive integers.
    """
    test_cases ={
        'pass_test_cases':{
            'string_int_pass_1' : ("44", 44),
            'string_int_pass_2' : ("0", 0),
            'string_int_pass_3' : ("24", 24),
            'string_int_pass_4' : ("300", 300)
        },
        'fail_test_cases':{
            'int_fail_1' : -1,
            'int_fail_2' : -101,
            'flt_fail_1' : -1.5,
            'flt_fail_2' : -87.3,
            'flt_fail_3' : 1.1,
            'flt_fail_4' : 92.6,
            'string_fail_1' : "1peach2",
            'string_fail_2' : "-25",
            'bool_fail_1' : True,
            'bool_fail_2' : False,
            'none_fail' : None,
            # unsure about testing types
            'type_obj_fail' : {'bad' : 'superbad'},
            'type_tuple_fail' : (2, 'bad',),
            'type_set_fail' : {'apple', 'orange'},
            'type_list_fail' : ['bad', 7]
        }
    }
    
    check = IntegerForm()

    for test_suit in test_cases:
        for key in test_cases[test_suit]:
            value = test_cases[test_suit][key]
            # Need to to decide what is returned
            # to show proper/improper input
            if test_suit == 'pass_test_cases':
                assert check.check_integer(value[0]) == value[1]
            else:
                assert check.check_integer(value) == None