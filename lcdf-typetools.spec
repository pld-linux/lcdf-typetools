Summary:	LCDF Typetools - some programs for manipulating Type 1 fonts
Summary(pl.UTF-8):	LCDF Typetools - programy do obróbki fontów Type 1
Name:		lcdf-typetools
Version:	2.43
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	http://www.lcdf.org/~eddietwo/type/%{name}-%{version}.tar.gz
# Source0-md5:	41ea69d3c01c2457f53b9b5ab0f734d7
URL:		http://www.lcdf.org/~eddietwo/type/#typetools
BuildRequires:	kpathsea-devel
BuildRequires:	libstdc++-devel
Obsoletes:	mminstance
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The LCDF Typetools package contains several programs for manipulating
PostScript Type 1, Type 1 multiple master, and PostScript-flavored
OpenType fonts. LCDF Typetools includes the mmafm and mmpfb programs,
which were formerly distributed as part of a different package
(mminstance).

%description -l pl.UTF-8
Pakiet LCDF Typetools zawiera kilka programów do obróbki fontów w
formacie PostScript Type 1, Type 1 multiple master i podobnych do
postscriptowych fontów OpenType. LCDF Typetools zawiera programy
mmafm i mmpfb, które kiedyś były dostępne jako część innego pakietu
(mminstance).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS ONEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
