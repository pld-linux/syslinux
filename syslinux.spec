Summary:	Simple bootloader
Summary(pl):	Prosty bootloader
Name:		syslinux
Version:	1.62
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.kernel.org/pub/linux/utils/boot/syslinux/%{name}-%{version}.tar.bz2
Patch0:		%{name}-no_mount.patch
URL:		http://www.kernel.org/software/syslinux/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
SYSLINUX is a boot loader for the Linux operating system which
operates off MS-DOS floppies. It is intended to simplify first-time
installation of Linux, rescue disks, and other uses for boot floppies.
A SYSLINUX floppy can be manipulated using standard MS-DOS (or any
other OS that can access an MS-DOS filesystem) tools once it has been
created, and requires only a ~ 7K DOS program or ~ 13K Linux program
to create it in the first place. It also includes PXELINUX, a program
to boot off a network server using a boot PROM compatible with the
Intel PXE (Pre-Execution Environment) specification.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Warning: 
this version does work in different way than the docs states because I
added temporary patch no_mount.patch to avoid tricky image mounting
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

%description -l pl
SYSLINUX jest boot-loaderem dla Linux'a, który operuje na dyskietkach 
z systemem plików MS-DOS. Jego przeznaczeniem jest uproszczenie pierwszej
instalacji Linux'a, dyskietki ratunkowe oraz inne rzeczy zwi±zane z
dyskietkami. Dyskietka SYSLINX'owa mo¿e byæ modyfikowana w systemie
MS-DOS (a tak¿e ka¿dym innym systemie z dostêpem do systemu plików MS-DOS)
gdy narzêdzia sa ju¿ stworzone, a tak¿e potrzebuje tylko ~7K programu 
DOS'owego lub ~13K programu Linux'owego do stworzenia ich po raz pierwszy.
Zawiera tak¿e program PXELINUX - program s³u¿±cy do bootowania servera
sieciowego poprzez Boot-PROM kompatybilny ze specyfikacj± Intel PXE 
(Pre-Execution Environment).
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
UWAGA:
Ta wersja dzia³a inaczej ni¿ jest to opisane w dokumentacji, poniewa¿
doda³em tymczasowy patch no_mount.patch aby zapobiedz tricky image mounting.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

%prep
%setup -q
%patch

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}}

install *.sys *.bin *.com $RPM_BUILD_ROOT%{_libdir}/%{name}
install syslinux $RPM_BUILD_ROOT%{_bindir}

# I'm not sure if this should be packed /klakier
#install gethostip $RPM_BUILD_ROOT%{_bindir}

gzip -9nf README *.doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*
