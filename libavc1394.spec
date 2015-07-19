%define major 	0
%define libname	%mklibname avc1394_ %{major}
%define librom	%mklibname rom1394_ %{major}
%define devname	%mklibname avc1394 -d

Summary:	Control AV firewire devices
Name:		libavc1394
Version:	0.5.4
Release:	11
License:	GPLv2
Group:		System/Libraries
Url:		http://www.sourceforge.net/projects/libavc1394
Source0:	http://downloads.sourceforge.net/project/libavc1394/%{name}/%{name}-%{version}.tar.gz
Patch0:         libavc1394-0.5.4-librom.patch
Patch1:		libavc1394-0.5.4-add-missing-linkage-against-librawutil1394.patch
Buildrequires:	pkgconfig(libraw1394)

%description
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

%package -n %{libname}
Summary:	FireWire interface
Group:		System/Libraries
Provides:	libavc1394 = %{version}-%{release}

%description -n %{libname}
libavc1394 is a programming interface for the 1394 Trade 
Association AV/C (Audio/Video Control) Digital Interface 
Command Set. It is intended for use with GNU/Linux IEEE-1394

%package -n %{librom}
Summary:	FireWire interface
Group:		System/Libraries
Conflicts:	%{_lib}avc1394_0 < 0.5.4-3

%description -n %{librom}
This package contains a shared library for %{name}.

%package -n %{devname}
Summary:	FireWire interface
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{librom} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}avc1394_0-devel < 0.5.4

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -q
%patch0 -p1 -b .rom1394~
%patch1 -p1 -b .rawutil1394~
autoreconf -fiv

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std
install -m755 -p test/.libs/romtest -D %{buildroot}%{_bindir}/romtest

%files -n %{name}-tools
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libavc1394.so.%{major}*

%files -n %{librom}
%{_libdir}/librom1394.so.%{major}*

%files -n %{devname}
%doc README NEWS INSTALL COPYING AUTHORS
%{_includedir}/*
%{_libdir}/libavc1394.so
%{_libdir}/librom1394.so
%{_libdir}/pkgconfig/libavc1394.pc
