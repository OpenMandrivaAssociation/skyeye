%define pre_release rc1

%define rel 0.%{pre_release}.1

Name:		skyeye
Version:	1.2.8
Release:	%mkrel %rel 
License:	GPL
# TODO 
Group:		Development/Tools
Summary:	ARM, Mips, Coldfire simulator
URL:		http://www.skyeye.org/index.shtml
Source0:	%{name}-%{version}_%{pre_release}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
# TODO 
#BuildRequires:	libX11-devel, xorg-x11-proto-devel

%description
SkyEye is an Open Source Software Project (GPL Licence). Origin from GDB/Armulator, 
the goal of SkyEye is to provide an integrated simulation environment in Linux 
and Windows. SkyEye environment simulates/emulates typical Embedded Computer
Systems (Now it supports a series ARM architecture based microprocessors and 
Blackfin DSP Processor). You can run some Embedded Operation System such as 
ARM Linux, uClinux, uc/OS-II (ucos-ii) etc. in SkyEye, and analysis or debug 
them at source level.


%prep
%setup -q -n %{name}-%{version}_%{pre_release}

%build
%configure
%make 

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
