%define major 	0
%define libname %mklibname avc1394_ %{major}
%define libnamedev %mklibname avc1394 -d

Name:		libavc1394
Version:	0.5.4
Release:	2
Summary:	Control AV firewire devices
License:	GPL
Group:		System/Libraries
Source0:	http://downloads.sourceforge.net/project/libavc1394/%{name}/%{name}-%{version}.tar.gz
URL:		http://www.sourceforge.net/projects/libavc1394

Buildrequires:	pkgconfig(libraw1394)

%description
libavc1394 is a programming interface for the 1394 Trade 
Association AV/C (Audio/Video Control) Digital Interface 
Command Set. It is intended for use with GNU/Linux IEEE-1394

%package -n %{libname}
Summary:	FireWire interface
Group:		System/Libraries
Provides:	libavc1394 = %{version}-%{release}

%description -n %{libname}
libavc1394 is a programming interface for the 1394 Trade 
Association AV/C (Audio/Video Control) Digital Interface 
Command Set. It is intended for use with GNU/Linux IEEE-1394

%package -n %{libnamedev}
Summary:	FireWire interface
Group:		Development/C
Provides:	libavc1394-devel = %{version}-%{release}
Provides:	libavc-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%{_lib}avc1394_0-devel < 0.5.4

%description -n %{libnamedev}
libavc1394 is a programming interface for the 1394 Trade
Association AV/C (Audio/Video Control) Digital Interface
Command Set. It is intended for use with GNU/Linux IEEE-1394

%package -n %{name}-tools
Summary:	FireWire interface
Group:		Development/C
Requires:	%{libname} = %{version}
Obsoletes:	libavc1394_0-testools < 0.5.4

%description -n %{name}-tools
Contains test tools for the libavc1394 library.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std
cp test/.libs/romtest %{buildroot}/%{_bindir}

%files -n %{libname}
%doc README NEWS INSTALL COPYING AUTHORS
%{_libdir}/*.so.%{major}*

%files -n %{libnamedev}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n %{name}-tools
%{_bindir}/*
%{_mandir}/man1/*




%changelog
* Wed Mar 07 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.5.4-1
+ Revision: 782756
- version update 0.5.4

* Mon Feb 20 2012 Götz Waschk <waschk@mandriva.org> 0.5.3-10
+ Revision: 778233
- rebuild

* Sat Dec 31 2011 Frank Kober <emuse@mandriva.org> 0.5.3-9
+ Revision: 748505
- Rebuild removing static lib and libtool archive

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.3-8
+ Revision: 660219
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.3-7mdv2011.0
+ Revision: 602525
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.3-6mdv2010.1
+ Revision: 520754
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.5.3-5mdv2010.0
+ Revision: 425517
- rebuild

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 0.5.3-4mdv2009.1
+ Revision: 320390
- new devel package policy

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.5.3-3mdv2009.0
+ Revision: 222505
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.5.3-2mdv2008.1
+ Revision: 150466
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

