# Default action is to show what commands are available.
all : commands

## commands : Display available commands.
commands : Makefile
	@sed -n 's/^##//p' $<

## create   : create a distribution.
create :
	python setup.py sdist

## clean    : clean up generated files.
clean :
	@rm -rf MANIFEST dist $$(find . -name '*~' -print)
