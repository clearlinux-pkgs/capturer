#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : capturer
Version  : 3.0
Release  : 10
URL      : https://files.pythonhosted.org/packages/9a/98/e2cac95d1cba553b10552511fdb55043b00a99bf8c1ed913ecbc654d6bfb/capturer-3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/9a/98/e2cac95d1cba553b10552511fdb55043b00a99bf8c1ed913ecbc654d6bfb/capturer-3.0.tar.gz
Summary  : Easily capture stdout/stderr of the current process and subprocesses
Group    : Development/Tools
License  : MIT
Requires: capturer-license = %{version}-%{release}
Requires: capturer-python = %{version}-%{release}
Requires: capturer-python3 = %{version}-%{release}
Requires: humanfriendly
BuildRequires : buildreq-distutils3
BuildRequires : humanfriendly
BuildRequires : pytest

%description
==============================================================================

%package license
Summary: license components for the capturer package.
Group: Default

%description license
license components for the capturer package.


%package python
Summary: python components for the capturer package.
Group: Default
Requires: capturer-python3 = %{version}-%{release}

%description python
python components for the capturer package.


%package python3
Summary: python3 components for the capturer package.
Group: Default
Requires: python3-core
Provides: pypi(capturer)
Requires: pypi(humanfriendly)

%description python3
python3 components for the capturer package.


%prep
%setup -q -n capturer-3.0
cd %{_builddir}/capturer-3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1608055678
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
py.test capturer/tests.py
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/capturer
cp %{_builddir}/capturer-3.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/capturer/4533bebc7b149028bc2932234fc49ca4d1a61d07
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/capturer/4533bebc7b149028bc2932234fc49ca4d1a61d07

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
