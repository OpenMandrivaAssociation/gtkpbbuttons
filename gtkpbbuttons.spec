%define name gtkpbbuttons
%define version 0.6.8
%define release %mkrel 1

Name: %{name}
Summary: GTK display client for pbbuttonsd
Version: %{version}
Release: %{release}
Source: http://prdownloads.sourceforge.net/pbbuttons/%{name}-%{version}.tar.bz2
Source1: gtkpbbuttons.startup
Patch0: gtkpbbuttons_default_theme.patch
URL: http://pbbuttons.sourceforge.net/
Group: System/Configuration/Hardware
BuildRoot: %{_tmppath}/%{name}-buildroot
License: GPL
Requires: pbbuttonsd >= 0.5.0
BuildRequires: pbbuttonsd-devel >= 0.6.5
BuildRequires: popt-devel libgtk+2-devel libaudiofile-devel
ExclusiveArch: ppc

%description
A visualisation client for pbbuttonsd to display
messages from the server in nice GTK popup windows.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q -n %{name}-%{version}

%patch0 -p1

%build
%configure
%make

%install
%makeinstall_std
install -c -D -m755 %{SOURCE1} %buildroot%{_sysconfdir}/X11/xinit.d/gtkpbbuttons
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc AUTHORS BUGS COPYING README TODO
%config(noreplace) %{_sysconfdir}/X11/xinit.d/gtkpbbuttons
%{_bindir}/*
%{_mandir}/man*/*
%dir %{_datadir}/%{name}/themes
%{_datadir}/%{name}/themes/*

