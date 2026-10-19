Name:		flashrom
#Update this version string and create a matching v%{version} tag to cut a release
Version:	1.8.0
Release:	0%{?dist}
Summary:	Simple program for reading/writing flash chips content
License:	GPLv2
URL:		https://flashrom.org

Source0:	https://github.com/metal-toolbox/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	ninja-build
BuildRequires:	pkgconfig
BuildRequires:	pciutils-devel
BuildRequires:	libusb1-devel
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
%ifarch %{ix86} x86_64 aarch64
BuildRequires:	dmidecode
Requires:	dmidecode
%endif
Requires:	udev

%global debug_package %{nil}

%description
flashrom is a utility for identifying, reading, writing, verifying and erasing
flash chips. It is designed to flash BIOS/EFI/coreboot/firmware/optionROM
images on mainboards, network/graphics/storage controller cards, and various
other programmer devices.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%meson --auto-features=auto -Duse_git_version=disabled -Dtests=disabled -Dman-pages=disabled -Ddocumentation=disabled
%meson_build

%install
%meson_install
# The classic CLI is statically linked against libflashrom; ship only the CLI
rm -rf %{buildroot}%{_includedir} %{buildroot}%{_libdir}

%files
%license COPYING.rst
%{_sbindir}/%{name}
%{_datadir}/bash-completion/completions/flashrom.bash

%changelog
