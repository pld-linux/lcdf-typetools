Summary:	LCDF Typetools - some programs for manipulating Type 1 fonts
Summary(pl):	LCDF Typetools - programy do obróbki fontów Type 1
Name:		lcdf-typetools
Version:	2.3
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	http://www.lcdf.org/~eddietwo/type/%{name}-%{version}.tar.gz
# Source0-md5:	7e662fa148bffec9b66bc5a155f6b7a1
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

%description -l pl
Pakiet LCDF Typetools zawiera kilka programów do obróbki fontów w
formacie PostScript Type 1, Type 1 multiple master i podobnych do
postscriptowych fontów OpenType. LCDF Typetools zawiera programy
mmafm i mmpfb, które kiedy¶ by³y dostêpne jako czê¶æ innego pakietu
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
