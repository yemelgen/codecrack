CC = gcc
CFLAGS = -Wall -DTEST_URIPATH
LDFLAGS =
TARGET = uripath
SOURCES = uripath.c

.PHONY: clean build
all: clean build

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $(TARGET) $(SOURCES) $(LDFLAGS)

build: $(TARGET)

clean:
	rm -f $(TARGET)
