## Module 1 : Modules et packages 

# creer un module
def display():
    print("PythonGeeks")
if __name__ == "__main__":
    display()


#importer un module
import pythongeeks
pythongeeks.display()

from pythongeeks import * 
display()


from pythongeeks import display 
display()


import website.pythongeeks
pythongeeks.display()

import website.pythongeeks as pg
pg.display()
Output
