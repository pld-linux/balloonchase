Summary: 	Balloon Chase.
Name:		balloonchase
Version:	0.9.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://koti.mbnet.fi/makegho/c/bchase/%{name}-%{version}.tar.bz2
URL:		http://koti.mbnet.fi/makegho/c/bchase/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel >= 1.2.0
Requires:	SDL >= 1.2.0
Requires:	SDL_image >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Balloon Chase is a game where you fly a hot air balloon 
and try to blow the other player out of the screen.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_bindir}
install -d $RPM_BUILD_ROOT/%{_datadir}/%{name}/images

cp main $RPM_BUILD_ROOT/%{_datadir}/%{name}/%{name}
cp images/* $RPM_BUILD_ROOT/%{_datadir}/%{name}/images

cat > $RPM_BUILD_ROOT/%{_bindir}/%{name} <<EOF
#!/bin/sh
cd %{_datadir}/%{name}
./%{name} \$@
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc VERSION README COPYING
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/images
%{_datadir}/%{name}/images/*
