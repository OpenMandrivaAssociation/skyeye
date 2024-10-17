%define pre_release rc1

%define rel 0.%{pre_release}.1

%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		skyeye
Version:	1.3.0
Release:%rel 
License:	GPLv2
Group:		Emulators
Summary:	ARM, Mips, Coldfire simulator
URL:		https://www.skyeye.org/index.shtml
Source0:	%{name}-%{version}_%{pre_release}.tar.gz
Patch:		skyeye-1.3.0.fix-str-fmt.patch
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	libxpm-devel
BuildRequires:	binutils-devel
BuildRequires:	readline-devel

%description
The goal of SkyEye is to provide an integrated simulation environment in Linux 
and Windows. SkyEye environment simulates/emulates typical Embedded Computer
Systems (Now it supports a series ARM architecture based microprocessors and 
Blackfin DSP Processor). You can run some Embedded Operation System such as 
ARM Linux, uClinux, uc/OS-II (ucos-ii) etc. in SkyEye, and analysis or debug 
them at source level.

%package -n %{libname}
Summary:	%{name} library
Group:		System/Libraries
Provides:	%{libname} = %{version}
	
%description -n %{libname}
%{name} library.

%package -n %{develname}
Summary:	%{name} development library
Group:		Development/Other
Provides:	%{libname} = %{version}
	
%description -n %{develname}
%{name} development library.  

%prep
%setup -q -n %{name}-%{version}_%{pre_release}

%patch -p0

%build
autoreconf -fiv
%configure2_5x --enable-lcd --enable-shared
#libtool wants it badly
mkdir third-party/opcodes/.libs
mkdir third-party/bfd/.libs
mkdir third-party/libiberty/.libs
mkdir third-party/libiberty/pic
mkdir third-party/readline/.libs

%make

%install
%makeinstall

mv %{buildroot}%{_includedir}/include %{buildroot}%{_includedir}/%{name}

#see later how to deal with it
rm -rf %{buildroot}/usr/testsuite

%files
%doc MAINTAINERS README ChangeLog
%{_bindir}/mknandflashdump
%{_bindir}/prof_convert
%{_bindir}/skyeye
%{_bindir}/uart_instance

%files -n %{libname}
%doc MAINTAINERS README ChangeLog
%{_libdir}/%{name}/*so.%{major}*

%files -n %{develname}
%doc MAINTAINERS README ChangeLog
%{_libdir}/%{name}/*.so
%{_includedir}/%{name}/*



