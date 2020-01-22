# Deployment documentation

Once your application is in a functional state you will need to get it to the user in some form. For example if your software is designed to run on a Redhat based system you would create a [RPM](https://en.wikipedia.org/wiki/RPM_Package_Manager) to deploy to your users. If you are targeting a Debain based system (such as Ubuntu) you would create a [DEB](https://wiki.debian.org/HowToPackageForDebian) package. For Windows you can leverage the [WiX toolset](https://wixtoolset.org/) to create a installer for windows based applications. There are also platform neutral solutions such as a [docker](https://www.docker.com/) container that depend on docker being installed on the host system.

What ever method you choose you **must** package your code in some manner and then test that the package installs and executes on the desired platform. This may require you to develop multiple solutions depending on where and how your code will be used.

TODO: Write your documentation here

## Submission

All files for this lab should be added to **this** directory. Remember that [30% of your grade](../../docs/syllabus.md#grading) is dependent on individual effort! So you **MUST** document what you worked on for this lab. If you spent the entire lab doing research then you must upload a summary of your research. Any work that is not documented by some sort of artifact (source code, documentation, etc.) will not be counted towards your final grade.

This lab is due on the date specified in the root level [README.md](../../README.md).
