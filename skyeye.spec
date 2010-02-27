%define pre_release rc1

%define rel 0.%{pre_release}.1

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

%description
The goal of SkyEye is to provide an integrated simulation environment in Linux 
and Windows. SkyEye environment simulates/emulates typical Embedded Computer
Systems (Now it supports a series ARM architecture based microprocessors and 
Blackfin DSP Processor). You can run some Embedded Operation System such as 
ARM Linux, uClinux, uc/OS-II (ucos-ii) etc. in SkyEye, and analysis or debug 
them at source level.


%prep
%setup -q -n %{name}-%{version}_%{pre_release}
#%patch0 -p0
%patch1 -p0

%build
autoreconf -fiv
%configure2_5x --enable-lcd

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

#see later how to deal with it
rm -rf %{buildroot}/usr/testsuite

rm -Rf %{buildroot}/%_libdir/*.{a,la}
rm -Rf %{buildroot}/%_includedir/
rm -Rf %{buildroot}/%_infodir/ 
%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc MAINTAINERS README ChangeLog
%{_bindir}/*
%{_libdir}/*

