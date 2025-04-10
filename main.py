
from methods.lehmer import Lehmer
from ui.main_window import MainApp

root = MainApp()

root.mainloop()

lehmer = Lehmer(4122,5, 76 )
print(lehmer.numbers)
