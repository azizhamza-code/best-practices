from script import add


'''def test_add():

    assert 1 + 2 == add(1, 2)'''

def setup_function(function):

   print(f'Runing Setup: {function.__name__}')
   function.x = 10

def teardown_function(function):

   print(f'Runing Teardown: {function.__name__}')
   del function.x

def test_script_add():

   assert add(test_script_add.x) == 11
