#!/bin/bash

rpmname=python3-sphinx
version=1.4.6
release=1

# Patch name
appliance_name=${appliance}-${version}

# Creating source tarball file
echo "Creating tarball files ..."
source_tarball=${rpmname}-${version}.tar.gz
tar czf ${source_tarball} ${rpmname}-${version}

echo "Moving tarball to RPM SOURCE folder ..."
cp ${source_tarball} ~/rpmbuild/SOURCES/.

# Going for rpmbuild
echo "Building SRPM file"
rpmbuild -bs Sphinx.spec

echo "Building RPM from specfile"
rpmbuild --rebuild ~/rpmbuild/SRPMS/${rpmname}-${version}-${release}.el7.centos.src.rpm
