Summary:	Firmware for logic analyzers based on the Cypress EZ-USB FX2(LP) chip
Name:		sigrok-firmware-fx2lafw
Version:	0.1.0
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Applications/Engineering
URL:		http://sigrok.org/wiki/Fx2lafw
Source0:	http://downloads.sourceforge.net/sigrok/%{name}-%{version}.tar.gz
# Source0-md5:	4e1080dbaaf44f1faba503a742b8bc56
BuildRequires:	sdcc
BuildArch:	noarch

%description
fx2lafw is a free/libre/open-source firmware for logic analyzers based
on the Cypress EZ-USB FX2(LP) chip.

It is licensed under the terms of the GNU GPL (version 2 or later),
and uses additional helper code (fx2lib), licensed under the GNU LGPL
(version 2.1 or later).

%prep
%setup -q

%build
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

# libsigrok will look here
%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT/%{_datadir}/sigrok-firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS ChangeLog
%{_datadir}/sigrok-firmware
