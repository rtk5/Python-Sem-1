#nested function
def outer():
    print('this is outer function')
    def inner():
        print('this is inner function')
    inner()
outer()      #code runs till here(no output), then outer is called runs till inner print, 
 #                                  then inner is called
