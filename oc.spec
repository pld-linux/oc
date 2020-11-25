#
# Conditional build:
%bcond_with	tests		# perform tests (requires network)
#
Summary:	The OPeNDAP C DAP2 library (client-side only)
Summary(pl.UTF-8):	Biblioteka OPeNDAP DAP2 dla C (tylko strona kliencka)
Name:		oc
Version:	2.0
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.opendap.org/pub/OC/source/%{name}-%{version}.tar.gz
# Source0-md5:	488963bc74053674da4fc88bc13b6264
Patch0:		%{name}-libdir.patch
URL:		http://opendap.org/oc/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	curl-devel >= 7.16.4
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
Requires:	curl >= 7.16.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The OPeNDAP C API (OC) provides a set of C-language type definitions
and functions that can be used to retrieve data over the Internet from
servers that implement the OPeNDAP Data Access Protocol (DAP). The OC
implementation provides a low-overhead way to retrieve this data,
making it practical to include OPeNDAP capability in relatively simple
software.

%description -l pl.UTF-8
OPeNDAP C API (OC) zawiera zbiór definicji typów i funkcji języka C
przeznaczonych do pobierania danych poprzez Internet z serwerów
implementujących protokół OPeNDAP Data Access Protocol (DAP).
Implementacja OC daje możliwość pobierania tych danych z małym
narzutem, czyniąc praktycznym wbudowanie obsługi OPeNDAP w stosunkowo
proste oprogramowanie.

%package devel
Summary:	Header files for OC library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel >= 7.16.4

%description devel
Header files for OC library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OC.

%package static
Summary:	Static OC library
Summary(pl.UTF-8):	Statyczna biblioteka OC
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OC library.

%description static -l pl.UTF-8
Statyczna biblioteka OC.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I conf
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README RELEASE_NOTES
%attr(755,root,root) %{_bindir}/ocprint
%attr(755,root,root) %{_libdir}/liboc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboc.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oc-config
%attr(755,root,root) %{_libdir}/liboc.so
%{_libdir}/liboc.la
%{_includedir}/oc

%files static
%defattr(644,root,root,755)
%{_libdir}/liboc.a
