#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x597240FE94E60165 (rbtcollins@hp.com)
#
Name     : extras
Version  : 1.0.0
Release  : 33
URL      : http://pypi.debian.net/extras/extras-1.0.0.tar.gz
Source0  : http://pypi.debian.net/extras/extras-1.0.0.tar.gz
Source99 : http://pypi.debian.net/extras/extras-1.0.0.tar.gz.asc
Summary  : Useful extra bits for Python - things that shold be in the standard library
Group    : Development/Tools
License  : MIT
Requires: extras-legacypython
Requires: extras-python3
Requires: extras-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
extras
        ======
        
        extras is a set of extensions to the Python standard library, originally
        written to make the code within testtools cleaner, but now split out for
        general use outside of a testing context.
        
        
        Documentation
        -------------

%package legacypython
Summary: legacypython components for the extras package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the extras package.


%package python
Summary: python components for the extras package.
Group: Default
Requires: extras-legacypython
Requires: extras-python3

%description python
python components for the extras package.


%package python3
Summary: python3 components for the extras package.
Group: Default
Requires: python3-core

%description python3
python3 components for the extras package.


%prep
%setup -q -n extras-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507153512
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1507153512
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
