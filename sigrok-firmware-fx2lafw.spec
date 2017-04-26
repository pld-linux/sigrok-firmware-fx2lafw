Summary:	Firmware for logic analyzers based on the Cypress EZ-USB FX2(LP) chip
Summary(pl.UTF-8):	Firmware dla analizatorów logicznych opartych na układzie Cypress EZ-USB FX2(LP)
Name:		sigrok-firmware-fx2lafw
Version:	0.1.4
Release:	1
License:	GPL v2+ (firmware code), LGPL v2+ (fx2lib library)
Group:		Applications/Engineering
Source0:	http://sigrok.org/download/source/sigrok-firmware-fx2lafw/%{name}-%{version}.tar.gz
# Source0-md5:	d379ebd260aede0b016388f444e9af31
URL:		http://sigrok.org/wiki/Fx2lafw
# sdas8051 or asx8051
BuildRequires:	sdcc >= 2.9.0
Requires:	libsigrok >= 0.1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fx2lafw is a free/libre/open-source firmware for logic analyzers based
on the Cypress EZ-USB FX2(LP) chip.

It is licensed under the terms of the GNU GPL (version 2 or later),
and uses additional helper code (fx2lib), licensed under the GNU LGPL
(version 2.1 or later).

%description -l pl.UTF-8
fx2lafw to wolnodostępne firmware dla analizatorów logicznych opartych
na układzie Cypress EZ-USB FX2(LP).

Jest udostępnione na warunkach licencji GNU GPL (w wersji 2 lub
nowszej) i wykorzystuje dodakowy kod pomocniczy (fx2lib), udostępniony
na warunkach licencji GNU LGLP (w wersji 2.1 lub nowszej).

%prep
%setup -q

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%{_datadir}/sigrok-firmware/fx2lafw-braintechnology-usb-lps.fw
%{_datadir}/sigrok-firmware/fx2lafw-cwav-usbeeax.fw
%{_datadir}/sigrok-firmware/fx2lafw-cwav-usbeedx.fw
%{_datadir}/sigrok-firmware/fx2lafw-cwav-usbeesx.fw
%{_datadir}/sigrok-firmware/fx2lafw-cwav-usbeezx.fw
%{_datadir}/sigrok-firmware/fx2lafw-cypress-fx2.fw
%{_datadir}/sigrok-firmware/fx2lafw-hantek-6022be.fw
%{_datadir}/sigrok-firmware/fx2lafw-sainsmart-dds120.fw
%{_datadir}/sigrok-firmware/fx2lafw-saleae-logic.fw
%{_datadir}/sigrok-firmware/fx2lafw-sigrok-fx2-16ch.fw
%{_datadir}/sigrok-firmware/fx2lafw-sigrok-fx2-8ch.fw
