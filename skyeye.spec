%define pre_release rc1

%define rel 0.%{pre_release}.2

%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Name:		skyeye
Version:	1.3.0
Release:	%mkrel %rel 
License:	GPLv2
Group:		Emulators
Summary:	ARM, Mips, Coldfire simulator
URL:		http://www.skyeye.org/index.shtml
Source0:	%{name}-%{version}_%{pre_release}.tar.gz
#Patch0:		skyeye-1.2.8-fix_open_mode.diff
Patch1:		skyeye-1.3.0.fix-str-fmt.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
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
#%patch0 -p0
%patch1 -p0

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
rm -rf %{buildroot}
#cp /usr/share/automake-1.10/mkinstalldirs ./third-party
%makeinstall

mv %{buildroot}%{_includedir}/include %{buildroot}%{_includedir}/%{name}

#see later how to deal with it
rm -rf %{buildroot}/usr/testsuite

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc MAINTAINERS README ChangeLog
%{_bindir}/mknandflashdump
%{_bindir}/prof_convert
%{_bindir}/skyeye
%{_bindir}/uart_instance

%files -n %{libname}
%{_libdir}/%{name}/*so.%{major}*

%files -n %{develname}
%{_libdir}/%{name}/*.la
%{_libdir}/%{name}/*.so
%{_includedir}/%{name}/*

