Summary:	Library to support cross-platform C date and time functions
Summary(pl.UTF-8):	Biblioteka wspierająca wieloplatformowe funkcje obsługi daty i czasu w C
Name:		libcdatetime
Version:	20150101
Release:	2
License:	LGPL v3+
Group:		Libraries
Source0:	https://github.com/libyal/libcdatetime/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1e4200b84130019bced0edc7ab97bf49
Patch0:		%{name}-system-libs.patch
URL:		https://github.com/libyal/libcdatetime/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcerror-devel >= 20120425
BuildRequires:	libcstring-devel >= 20120425
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	libcerror >= 20120425
Requires:	libcstring >= 20120425
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
Requires:	libcerror-devel >= 20120425
Requires:	libcstring-devel >= 20120425

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
%patch0 -p1

%build
%{__gettextize}
%{__sed} -i -e 's/ po\/Makefile.in//' configure.ac
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
