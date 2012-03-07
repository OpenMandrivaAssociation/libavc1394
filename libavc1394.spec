%define major 	0
%define libname %mklibname avc1394_ %major
%define libnamedev %mklibname avc1394 -d

Name: 		libavc1394
Version: 	0.5.4
Release: 	1
Summary:        Control AV firewire devices
License: 	GPL
Group: 		System/Libraries
Source0: 	http://downloads.sourceforge.net/project/libavc1394/%{name}/%{name}-%{version}.tar.gz
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

%package -n %{libnamedev}
Summary: FireWire interface
Group: Development/C
Provides: libavc1394-devel = %version-%release
Provides: libavc-devel = %version-%release
Requires: %libname = %{version}
Obsoletes: %{_lib}avc1394_0-devel

%description -n %{libnamedev}
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
%configure2_5x --disable-static
%make

%install
%makeinstall_std
cp test/.libs/romtest %{buildroot}/%_bindir
rm -rf %{buildroot}/%{_libdir%}/*.la

%files -n %{libname}
%doc README NEWS INSTALL COPYING AUTHORS
%{_libdir}/*.so.%{major}*

%files -n %{libnamedev}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n %name-tools
%_bindir/*
%_mandir/man1/*


