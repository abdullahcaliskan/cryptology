sha1_hash : main.o sha1.o
	g++ $(CFLAGS) -o sha1_hash main.o sha1.o
main.o : main.cpp sha1.hpp
	g++ $(CFLAGS) -c main.cpp 
sha1.o : sha1.cpp sha1.hpp
	g++ $(CFLAGS) -c sha1.cpp
clean :
	rm -f *.o sha1_hash