include config.mk

INSTALL_PREFIX := $(DESTDIR)/$(PREFIX)
INSTALL_BIN := $(INSTALL_PREFIX)/bin
INSTALL_SHARE := $(INSTALL_PREFIX)/share

SED_INJECT := -e 's@%PREFIX%@$(PREFIX)@g' -e 's@%VERSION%@$(VERSION)@g'

all:
	true

install:
	install -D -m 755 src/$(TARGET) $(INSTALL_BIN)/$(TARGET)
	sed -i $(SED_INJECT) $(INSTALL_BIN)/$(TARGET)
	mkdir -p $(INSTALL_SHARE)/$(TARGET)
	install -m 644 data/*.conf $(INSTALL_SHARE)/$(TARGET)/

clean:
	true

.PHONY: all install clean
