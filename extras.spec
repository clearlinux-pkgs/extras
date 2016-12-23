#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : extras
Version  : 1.0.0
Release  : 24
URL      : http://pypi.debian.net/extras/extras-1.0.0.tar.gz
Source0  : http://pypi.debian.net/extras/extras-1.0.0.tar.gz
Summary  : Useful extra bits for Python - things that shold be in the standard library
Group    : Development/Tools
License  : MIT
Requires: extras-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : testtools
BuildRequires : testtools-python

%description
======
extras
======
extras is a set of extensions to the Python standard library, originally
written to make the code within testtools cleaner, but now split out for
general use outside of a testing context.

%package python
Summary: python components for the extras package.
Group: Default

%description python
python components for the extras package.


%prep
%setup -q -n extras-1.0.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd py2 ; py.test-2.7 ; popd
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
