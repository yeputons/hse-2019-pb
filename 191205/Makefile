.PHONY: all clean

SVGS=$(wildcard *.svg)
SVGPDFS=$(patsubst %.svg,%.pdf,$(SVGS))

all: 191205.pdf

191205.pdf: 191205.tex $(filter-out 191205.pdf, $(wildcard *.tex 191205.*)) $(SVGPDFS)
	pdflatex -shell-escape "$<" && pdflatex -shell-escape "$<"

%.pdf: %.svg
	inkscape -D "--file=$<" "--export-pdf=$@"

clean:
	rm $(filter-out 191205.tex,$(wildcard 191205.*)) *.pdf >/dev/null 2>&1
