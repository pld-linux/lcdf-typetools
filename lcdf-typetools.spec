Summary:	LCDF Typetools - some programs for manipulating Type 1 fonts
Summary(pl.UTF-8):	LCDF Typetools - programy do obróbki fontów Type 1
Name:		lcdf-typetools
Version:	2.85
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	http://www.lcdf.org/~eddietwo/type/%{name}-%{version}.tar.gz
# Source0-md5:	e9eefde14131dfcc5add91b92fcb7627
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
%attr(755,root,root) %{_bindir}/cfftot1
%attr(755,root,root) %{_bindir}/mmafm
%attr(755,root,root) %{_bindir}/mmpfb
%attr(755,root,root) %{_bindir}/otfinfo
%attr(755,root,root) %{_bindir}/otftotfm
%attr(755,root,root) %{_bindir}/t1dotlessj
%attr(755,root,root) %{_bindir}/t1lint
%attr(755,root,root) %{_bindir}/t1rawafm
%attr(755,root,root) %{_bindir}/t1reencode
%attr(755,root,root) %{_bindir}/t1testpage
%attr(755,root,root) %{_bindir}/ttftotype42
%{_datadir}/%{name}
%{_mandir}/man1/cfftot1.1*
%{_mandir}/man1/mmafm.1*
%{_mandir}/man1/mmpfb.1*
%{_mandir}/man1/otfinfo.1*
%{_mandir}/man1/otftotfm.1*
%{_mandir}/man1/t1dotlessj.1*
%{_mandir}/man1/t1lint.1*
%{_mandir}/man1/t1rawafm.1*
%{_mandir}/man1/t1reencode.1*
%{_mandir}/man1/t1testpage.1*
%{_mandir}/man1/ttftotype42.1*
