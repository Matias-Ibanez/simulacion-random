from cuadrado import ParteCentralDelCuadrado
from lehmer import Lehmer
from ui.main_window import MainApp

root = MainApp()

root.mainloop()

parte = ParteCentralDelCuadrado(123 ,3, 5)
lehmer = Lehmer(4122,5, 76 )
print(lehmer.numbers)
