#!/usr/bin/env bash

set -o xtrace
set -o errexit

RPMBUILD=${HOME}/rpmbuild

microdnf update -y
microdnf install -y dnf epel-release almalinux-release-devel
dnf install -y rpm-build rpmdevtools tar gzip
dnf config-manager --set-enabled crb

SPEC=${RPMBUILD}/SPECS/flashrom.spec
mkdir -p ${RPMBUILD}/SPECS ${RPMBUILD}/SOURCES
cp .github/flashrom.spec ${SPEC}

# Build the source tarball from the checked-out tree (run from the repo root)
# instead of downloading the tag, so the RPM is built from exactly this code.
VERSION=$(awk '/^Version:/ {print $2}' ${SPEC})
tar --exclude-vcs --transform "s,^\.,flashrom-${VERSION}," \
    -czf ${RPMBUILD}/SOURCES/v${VERSION}.tar.gz .

dnf builddep -y ${SPEC}
rpmbuild -bb ${SPEC}
