# Default action is to show what commands are available.
all : commands

## commands  : Display available commands.
commands : Makefile
	@sed -n 's/^##//p' $<

## create    : create a distribution.
create :
	python setup.py sdist

## install   : install package.
install :
	python setup.py install --record installed-files.txt

## uninstall : remove using record of installed files.
uninstall : installed-files.txt
	cat installed-files.txt | xargs rm -rf

## clean     : clean up generated files.
clean :
	@rm -rf MANIFEST build dist installed-files.txt $$(find . -name '*~' -print)
