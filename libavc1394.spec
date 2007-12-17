%define name 	libavc1394
%define version 0.5.3
%define release %mkrel 1

%define major 	_0
%define libname %mklibname avc1394 %major
%define libnamedev %mklibname avc1394 %major -d

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary:        Control AV firewire devices
License: 	GPL
Group: 		System/Libraries
Source0: 	%{name}-%{version}.tar.bz2
URL:            http://www.sourceforge.net/projects/libavc1394

Buildrequires: 	libraw1394-devel

%description
libavc1394 is a programming interface for the 1394 Trade 
Association AV/C (Audio/Video Control) Digital Interface 
Command Set. It is intended for use with GNU/Linux IEEE-1394

%package -n %{libname}
Summary: FireWire interface
Group: System/Libraries
Provides: libavc1394 = %version-%release

%description -n %{libname}
libavc1394 is a programming interface for the 1394 Trade 
Association AV/C (Audio/Video Control) Digital Interface 
Command Set. It is intended for use with GNU/Linux IEEE-1394

%package -n %{libname}-devel
Summary: FireWire interface
Group: Development/C
Provides: libavc1394-devel = %version-%release
Provides: libavc-devel = %version-%release
Requires: %libname = %{version}

%description -n %{libname}-devel
libavc1394 is a programming interface for the 1394 Trade
Association AV/C (Audio/Video Control) Digital Interface
Command Set. It is intended for use with GNU/Linux IEEE-1394

%package -n %name-tools
Summary: FireWire interface
Group: Development/C
Requires: %libname = %{version}
Obsoletes: libavc1394_0-testools

%description -n %name-tools
Contains test tools for the libavc1394 library.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
cp test/.libs/romtest $RPM_BUILD_ROOT/%_bindir

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(-,root,root)
%doc README NEWS INSTALL COPYING AUTHORS
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(- ,root,root)
%{_libdir}/*.la
%{_libdir}/*.a
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n %name-tools
%defattr(- ,root,root)
%_bindir/*
%_mandir/man1/*


