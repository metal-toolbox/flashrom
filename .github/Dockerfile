FROM almalinux:10-minimal AS base

RUN microdnf update -y && microdnf install -y dnf epel-release almalinux-release-devel

FROM base AS flashrom
WORKDIR /src
COPY . .
RUN .github/build-alma-rpms.sh

FROM base
COPY --from=flashrom /root/rpmbuild/RPMS/x86_64/flashrom*.rpm /tmp
RUN dnf install -y /tmp/flashrom*.rpm
