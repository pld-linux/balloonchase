Summary:	Balloon Chase game
Summary(pl.UTF-8):	Gra Balloon Chase
Name:		balloonchase
Version:	0.9.6
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://koti.mbnet.fi/makegho/c/bchase/%{name}-%{version}.tar.bz2
# Source0-md5:	ed386a8e30f90ad13dd404f219e4332b
URL:		http://koti.mbnet.fi/makegho/c/bchase/
Patch0:		%{name}-Makefile.patch
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Balloon Chase is a game where you fly a hot air balloon and try to
blow the other player out of the screen.

%description -l pl.UTF-8
Balloon Chase to gra, w której lata się balonem wypełnionym ciepłym
powietrzem, próbując wypchnąć drugiego gracza z ekranu.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/images}

cp %{name} $RPM_BUILD_ROOT%{_datadir}/%{name}
cp %{name}.dat $RPM_BUILD_ROOT%{_datadir}/%{name}
cp images/* $RPM_BUILD_ROOT%{_datadir}/%{name}/images

cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/sh
cd %{_datadir}/%{name}
./%{name} \$@
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc VERSION README
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
# hey, isn't it arch-dependent binary??? if so, it cannot be in %{_datadir}!
%attr(755,root,root) %{_datadir}/%{name}/%{name}
%{_datadir}/%{name}/%{name}.dat
%dir %{_datadir}/%{name}/images
%{_datadir}/%{name}/images/*
