# m4/libcerror.m4
%define		libcerror_ver	20120425
Summary:	Library to support cross-platform C date and time functions
Summary(pl.UTF-8):	Biblioteka wspierająca wieloplatformowe funkcje obsługi daty i czasu w C
Name:		libcdatetime
Version:	20181004
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libcdatetime/releases
Source0:	https://github.com/libyal/libcdatetime/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	87e84e8f1dc736b44caa723022b7f433
URL:		https://github.com/libyal/libcdatetime/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libcerror >= %{libcerror_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcdatetime is a library to support cross-platform C date and time
functions.

%description -l pl.UTF-8
libcdatetime to biblioteka wspierająca wieloplatformowe funkcje
obsługi daty i czasu w C.

%package devel
Summary:	Header files for libcdatetime library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcdatetime
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcerror-devel >= %{libcerror_ver}

%description devel
Header files for libcdatetime library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcdatetime.

%package static
Summary:	Static libcdatetime library
Summary(pl.UTF-8):	Statyczna biblioteka libcdatetime
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcdatetime library.

%description static -l pl.UTF-8
Statyczna biblioteka libcdatetime.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcdatetime.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libcdatetime.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcdatetime.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcdatetime.so
%{_includedir}/libcdatetime
%{_includedir}/libcdatetime.h
%{_pkgconfigdir}/libcdatetime.pc
%{_mandir}/man3/libcdatetime.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcdatetime.a
