output = out

linked_list: src/data_structures/linked_list.cpp
	c++ -Wall -Wextra -Werror -std=c++11 src/data_structures/linked_list.cpp -o $(output)/linked_list.o