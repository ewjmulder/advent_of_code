from src.util import *

x = Parser.from_file(SAMPLE).to_number_list_multi_line()

print(sum(x))
