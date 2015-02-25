Installable Lesson Demo (version 1)
===================================

Starting to explore the idea of lessons-as-packages using Python distutils.

To try it out:

1.  Clone this repo.
2.  `make create` to create a distribution file `dist/something-0.0.1.tar.gz`.
3.  `make install` to install it in your Python.
    -   You may wish to create a virtualenv first...
    -   But `make install` writes a list of installed files to `installed-files.txt`...
    -   ...so you can `cat installed-files.txt | xargs rm -rf` to get rid of them all.
4.  `lesson view something` to view this demo lesson.
    -   This emulates a learner viewing the lesson locally.
    -   The HTML and CSS will have been put in `$PYTHON_INSTALL_DIR/lessons/something`,
        e.g., `/home/aturing/anaconda/lessons/something`.
5.  `mkdir /tmp/stuff` and `lesson files something /tmp/stuff` to copy code and data into `/tmp/stuff`.
    -   This imitates a learner getting the sample code and data files for the lesson.
