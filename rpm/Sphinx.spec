Name:		python3-sphinx
Version:	1.4.6
Release:	1%{?dist}
Summary:	Sphinx Euclid specific RPM deployment package
Group:		Development/Libraries
License:	BSD Licence
Source0:	%{name}-%{version}.tar.gz

Requires:	python-docutils
Requires:	python-jinja2

# Some macros disabled
%define debug_package %{nil}
%define __arch_install_post %{nil}
%define __os_install_post %{nil}


%description
Sphinx is a tool that makes it easy to create intelligent and beautiful documentation, written by Georg Brandl and licensed under the BSD license.
It was originally created for the Python documentation, and it has excellent facilities for the documentation of software projects in a range of languages.

%prep
%setup -q


%build
# With python 3 support from cvmfs
make build PYTHON=python3

%install
mkdir -p %{buildroot}%{_prefix}/lib/python3.6/site-packages
mkdir -p %{buildroot}%{_prefix}/bin
cp -r %{_builddir}/%{name}-%{version}/build/lib/sphinx %{buildroot}%{_prefix}/lib/python3.6/site-packages
cp %{_builddir}/%{name}-%{version}/sphinx-* %{buildroot}%{_prefix}/bin/.

%check
# scons tests -j1

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

# BUILDROOT is automatically prepended to files path
%files
%{_bindir}/sphinx-*
%{_prefix}/lib/python3.6/site-packages/sphinx

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Feb 21 2018 Matthieu Marseille <matthieu.marseille@thales-services.fr> 1.4.6-1
- Initial release
