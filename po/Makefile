# SPDX-License-Identifier: MIT
# Copyright (c) 2026 Chris <goabonga@pm.me>
#
# Regenerate the translation catalogues.
#
#   make pot      -> rebuild po/helloworld.pot from src/
#   make update   -> merge new strings from .pot into existing .po files
#   make mo       -> compile .po -> .mo into src/helloworld/locale/
#   make all      -> pot + update + mo
#
# Requires the gettext toolchain (`apt install gettext`).

DOMAIN     := helloworld
PACKAGE_DIR := ../src/helloworld
LOCALES    := fr es
PO_FILES   := $(addsuffix .po,$(LOCALES))
MO_FILES   := $(foreach lang,$(LOCALES),$(PACKAGE_DIR)/locale/$(lang)/LC_MESSAGES/$(DOMAIN).mo)

.PHONY: all pot update mo clean

all: pot update mo

pot:
	xgettext --keyword=_ --keyword=N_ \
	         --from-code=UTF-8 --no-wrap \
	         --package-name=$(DOMAIN) \
	         --output=$(DOMAIN).pot \
	         $(shell cd .. && find src -name '*.py')

update: $(PO_FILES)
	for po in $(PO_FILES); do \
	    msgmerge --update --no-wrap "$$po" $(DOMAIN).pot; \
	done

mo: $(MO_FILES)

$(PACKAGE_DIR)/locale/%/LC_MESSAGES/$(DOMAIN).mo: %.po
	mkdir -p $(@D)
	msgfmt --output-file=$@ $<

clean:
	rm -f $(MO_FILES)
