.PHONY: all clean

SVGS=$(wildcard *.svg)
SVGPDFS=$(patsubst %.svg,%.pdf,$(SVGS))

all: 191128.pdf

191128.pdf: 191128.tex $(filter-out 191128.pdf, $(wildcard *.tex 191128.*)) $(SVGPDFS)
	pdflatex -shell-escape "$<" && pdflatex -shell-escape "$<"

%.pdf: %.svg
	inkscape -D "--file=$<" "--export-pdf=$@"

clean:
	rm $(filter-out 191128.tex,$(wildcard 191128.*)) *.pdf >/dev/null 2>&1
