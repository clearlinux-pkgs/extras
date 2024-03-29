#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x597240FE94E60165 (rbtcollins@hp.com)
#
Name     : extras
Version  : 1.0.0
Release  : 64
URL      : http://pypi.debian.net/extras/extras-1.0.0.tar.gz
Source0  : http://pypi.debian.net/extras/extras-1.0.0.tar.gz
Source1  : http://pypi.debian.net/extras/extras-1.0.0.tar.gz.asc
Summary  : Useful extra bits for Python - things that shold be in the standard library
Group    : Development/Tools
License  : MIT
Requires: extras-license = %{version}-%{release}
Requires: extras-python = %{version}-%{release}
Requires: extras-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
extras
        ======
        
        extras is a set of extensions to the Python standard library, originally
        written to make the code within testtools cleaner, but now split out for
        general use outside of a testing context.
        
        
        Documentation
        -------------

%package license
Summary: license components for the extras package.
Group: Default

%description license
license components for the extras package.


%package python
Summary: python components for the extras package.
Group: Default
Requires: extras-python3 = %{version}-%{release}

%description python
python components for the extras package.


%package python3
Summary: python3 components for the extras package.
Group: Default
Requires: python3-core
Provides: pypi(extras)

%description python3
python3 components for the extras package.


%prep
%setup -q -n extras-1.0.0
cd %{_builddir}/extras-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635726724
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/extras
cp %{_builddir}/extras-1.0.0/LICENSE %{buildroot}/usr/share/package-licenses/extras/d261d21949861edf5b8ef7bebf89682368f6ea9a
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/extras/d261d21949861edf5b8ef7bebf89682368f6ea9a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
