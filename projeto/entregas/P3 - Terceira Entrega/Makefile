# Slidev build pipeline para a P3
#
# Uso:
#   make install     # primeira vez — npm install + playwright chromium
#   make dev         # preview com hot-reload em localhost:3030
#   make pdf         # gera slides-generated.pdf
#   make pptx        # gera slides-generated.pptx
#   make all         # ambos
#   make clean       # apaga outputs + node_modules

SLIDES   := slides.md
PDF_OUT  := slides.pdf
PPTX_OUT := slides.pptx

.PHONY: install dev build pdf pptx all clean

install:
	npm install
	npx playwright install chromium

dev:
	npx slidev $(SLIDES) --open

build:
	npx slidev build $(SLIDES)

pdf: $(PDF_OUT)

$(PDF_OUT): $(SLIDES)
	npx slidev export $(SLIDES) --format pdf --output $(PDF_OUT)

pptx: $(PPTX_OUT)

$(PPTX_OUT): $(SLIDES)
	npx slidev export $(SLIDES) --format pptx --output $(PPTX_OUT)

all: pdf pptx

clean:
	rm -rf dist node_modules $(PDF_OUT) $(PPTX_OUT)
