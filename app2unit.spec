%global debug_package %{nil}

Name:		app2unit
Version:	1.1.2
Release:	1
Source0:	https://github.com/Vladimir-csp/app2unit/archive/refs/tags/v%{version}.tar.gz
Summary:	Utility to launch commands as systemd user units
URL:		https://github.com/Vladimir-csp/app2unit
License:	GPL-3.0
Group:		System/Utility

BuildRequires: make
BuildRequires: scdoc

%description
%summary

%prep
%autosetup -p1

%install
%make_install prefix='/usr'

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}.1.zst
