import sys
sys.path.insert(1, '/home/ruby/school/practical_programming/wgc')

from forms.string_form import StringForm

def test_string_form():
    test_cases = {
        'pass_test_cases' : {
            # Should probably add some formatting rules...
            'str_pass_1' : ('Math', 'Math'),
            'str_pass_2' : ('enGlIsh', 'English'),
            'str_pass_3' : ('maTH 207', 'Math 207'),
            'str_pass_4' : ('137 CS', '137 CS'),
            'str_pass_5' : ('mat 217', 'MAT 217'),
            # bit of user freedom with this one,
            # can't control everything
            'str_pass_5' : ('% soci 3033', '% Soci 3033'),
            'str_pass_6' : ('6578', '6578')
        },
        'fail_test_cases' : {
            'int_fail_1' : 25,
            'int_fail_2' : -3,
            'int_fail_3' : 0,
            'flt_fail_1' : 2.2,
            'flt_fail_2' : -905.6,
            'bool_fail_1' : True,
            'bool_fail_2' : False,
            'none_fail' : None,
             # unsure about testing types
            'type_obj_fail' : {'really' : 'silly'},
            'type_tuple_fail' : (2, 'really',),
            'type_set_fail' : {'peach', 'mango'},
            'type_list_fail' : ['wolf', 3]
        }
    }

    check = StringForm()

    for test_suit in test_cases:
        for key in test_cases[test_suit]:
            value = test_cases[test_suit][key]
            # Need to to decide what is returned
            # to show proper/improper input
            if test_suit == 'pass_test_cases':
                assert check.check_string(value[0]) == value[1]
            else:
                assert check.check_string(value) == None
test_string_form()