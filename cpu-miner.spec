Name:		cpuminer-wolf
Version:	2.4.0
Release:	1
License:	GPL-2.0
Summary:	Optimized CPU-miner for Bitcoin / Litecoin and others
URL:		https://github.com/wolf9466/cpuminer-multi
Group:		Productivity/Networking/Other
Source:		https://github.com/wolf9466/cpuminer-multi/archive/%{name}-%{version}.tar.gz
BuildRequires:	libcurl-devel jansson-devel automake
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
This is a multi-threaded CPU miner for Litecoin and Bitcoin,
fork of Jeff Garzik's reference cpuminer.

See https://bitcointalk.org/index.php?topic=55038.0 for more details.

%prep
%setup -q

%build
./autogen.sh
%configure
%__make %{?_smp_mflags}

%install
%__make DESTDIR="%{buildroot}" install

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS example-cfg.json
%{_bindir}/minerd
%doc /usr/share/man/man1/minerd.1.gz

%changelog
* Mon Sep 12 2016 Anatolii Vorona <vorona.tolik@gmail.com> 2.4.0-1
- new package built with tito

* Wed Dec 11 2013 Huaren Zhong <huaren.zhong@gmail.com> - 2.3.2
- Rebuild for Fedora

