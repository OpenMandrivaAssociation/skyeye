%define pre_release rc1

%define rel 0.%{pre_release}.1

Name:		skyeye
Version:	1.2.8
Release:	%mkrel %rel 
License:	GPLv2
Group:		Emulators
Summary:	ARM, Mips, Coldfire simulator
URL:		http://www.skyeye.org/index.shtml
Source0:	%{name}-%{version}_%{pre_release}.tar.gz
Patch0:     skyeye-1.2.8-fix_open_mode.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: pkgconfig(gtk+-2.0)

%description
The goal of SkyEye is to provide an integrated simulation environment in Linux 
and Windows. SkyEye environment simulates/emulates typical Embedded Computer
Systems (Now it supports a series ARM architecture based microprocessors and 
Blackfin DSP Processor). You can run some Embedded Operation System such as 
ARM Linux, uClinux, uc/OS-II (ucos-ii) etc. in SkyEye, and analysis or debug 
them at source level.


%prep
%setup -q -n %{name}-%{version}_%{pre_release}
%patch0 -p0

%build
%configure --enable-lcd
%make 

%install
rm -rf $RPM_BUILD_ROOT
cp /usr/share/automake-1.10/mkinstalldirs ./third-party
%makeinstall_std

rm -Rf $RPM_BUILD_ROOT/%_libdir/*.{a,la}
rm -Rf $RPM_BUILD_ROOT/%_includedir/
rm -Rf $RPM_BUILD_ROOT/%_infodir/ 
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc MAINTAINERS README ChangeLog
%_bindir/skyeye

