Summary:	Firmware for logic analyzers based on the Cypress EZ-USB FX2(LP) chip
Name:		sigrok-firmware-fx2lafw
Version:	0.1.1
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Applications/Engineering
URL:		http://sigrok.org/wiki/Fx2lafw
Source0:	http://downloads.sourceforge.net/sigrok/%{name}-%{version}.tar.gz
# Source0-md5:	6d91d1decac041dc29405379af530261
BuildRequires:	sdcc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fx2lafw is a free/libre/open-source firmware for logic analyzers based
on the Cypress EZ-USB FX2(LP) chip.

It is licensed under the terms of the GNU GPL (version 2 or later),
and uses additional helper code (fx2lib), licensed under the GNU LGPL
(version 2.1 or later).

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
%doc AUTHORS README NEWS ChangeLog
%{_datadir}/sigrok-firmware
