#
# Conditional build:
%bcond_without	efi32	# EFI32 bootloader (requires x86_32 gnu-efi)
%bcond_without	efi64	# EFI64 bootloader (requires x86_64 gnu-efi)
#
%ifnarch %{ix86}
# %{x8664} also possible, but requires multilib gnu-efi
%undefine	with_efi32
%endif
%ifnarch %{x8664}
%undefine	with_efi64
%endif
Summary:	Simple bootloader
Summary(pl.UTF-8):	Prosty bootloader
Summary(pt_BR.UTF-8):	Carregador de boot simples
Summary(zh_CN.UTF-8):	Linux操作系统的启动管理器
Name:		syslinux
Version:	6.01
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://www.kernel.org/pub/linux/utils/boot/syslinux/%{name}-%{version}.tar.xz
# Source0-md5:	5fe8959b92255143a334167ca1c395a6
URL:		http://syslinux.zytor.com/
BuildRequires:	gnu-efi
BuildRequires:	libuuid-devel
BuildRequires:	nasm
BuildRequires:	perl-base
BuildRequires:	perl-modules
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	mtools
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

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

%description -l pl.UTF-8
SYSLINUX jest boot-loaderem dla Linuksa, który operuje na dyskietkach
z systemem plików MS-DOS. Jego przeznaczeniem jest uproszczenie
pierwszej instalacji Linuksa, dyskietki ratunkowe oraz inne rzeczy
związane z dyskietkami. Dyskietka syslinuksowa może być modyfikowana w
systemie MS-DOS (a także każdym innym systemie z dostępem do systemu
plików MS-DOS) gdy narzędzia są już stworzone, a także potrzebuje
tylko ~7K programu DOS-owego lub ~13K programu linuksowego do
stworzenia ich po raz pierwszy. Zawiera także program PXELINUX -
program służący do bootowania serwera sieciowego poprzez Boot-PROM
kompatybilny ze specyfikacją Intel PXE (Pre-Execution Environment).

%description -l pt_BR.UTF-8
SYSLINUX é um carregador de boot para o linux, operando em disquetes
com formatação DOS. Sua intenção é simplificar instalações do Linux,
discos de recuperação, e outros usos para disquetes de boot. Um
disquete SYSLINUX pode ser manipulado usando ferramentas padrão do DOS
(ou qualquer sistema que possa acessar um filesystem DOS) e requer
somente um programa DOS de aproximadamente 7K ou linux de 13K para
criá-lo na primeira vez.

Também inclui o PXELINUX, um programa para boot remoto a partir de um
servidor de rede usando um boot PROM compatível com a especificação
Intel PXE (Pre-Execution Environment).

%package devel
Summary:	Header files for syslinux libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek syslinux
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description devel
This package includes the header files needed for compilation of
applications that are making use of the syslinux internals. Install
this package only if you plan to develop or will need to compile
customized syslinux clients.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe potrzebne do kompilowania
aplikacji wykorzystujących kod syslinuksa. Należy go instalować tylko
jeśli chcemy tworzyć lub kompilować własnych klientów syslinuksa.

%prep
%setup -q

%{__sed} -i 's/-march=i386//' sample/Makefile

%build
for d in "bios installer" %{?with_efi32:efi32} %{?with_efi64:efi64} ; do
%{__make} -j1 $d \
	CC="%{__cc}"
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_includedir}}
install bios/core/ldlinux.sys $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__make} -j1 install \
	firmware="bios %{?with_efi32:efi32} %{?with_efi64:efi64}" \
	INSTALLROOT=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir} \
	MANDIR=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README* doc/*.txt
%attr(755,root,root) %{_sbindir}/extlinux
%attr(755,root,root) %{_bindir}/gethostip
%attr(755,root,root) %{_bindir}/isohybrid
%attr(755,root,root) %{_bindir}/isohybrid.pl
%attr(755,root,root) %{_bindir}/keytab-lilo
%attr(755,root,root) %{_bindir}/lss16toppm
%attr(755,root,root) %{_bindir}/md5pass
%attr(755,root,root) %{_bindir}/memdiskfind
%attr(755,root,root) %{_bindir}/mkdiskimage
%attr(755,root,root) %{_bindir}/ppmtolss16
%attr(755,root,root) %{_bindir}/pxelinux-options
%attr(755,root,root) %{_bindir}/sha1pass
%attr(755,root,root) %{_bindir}/syslinux
%attr(755,root,root) %{_bindir}/syslinux2ansi
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.bin
%{_datadir}/%{name}/*.c32
%{_datadir}/%{name}/*.com
%{_datadir}/%{name}/dosutil
%{_datadir}/%{name}/gpxelinux.0
%{_datadir}/%{name}/gpxelinuxk.0
%{_datadir}/%{name}/ldlinux.sys
%{_datadir}/%{name}/lpxelinux.0
%{_datadir}/%{name}/memdisk
%{_datadir}/%{name}/pxelinux.0
%{_datadir}/%{name}/syslinux*.exe
%dir %{_datadir}/%{name}/diag
%{_datadir}/%{name}/diag/geodsp1s.img*
%{_datadir}/%{name}/diag/geodspms.img*
%{_datadir}/%{name}/diag/handoff.bin
%if %{with efi32}
%{_datadir}/%{name}/efi32
%endif
%if %{with efi64}
%{_datadir}/%{name}/efi64
%endif
%{_mandir}/man1/extlinux.1*
%{_mandir}/man1/gethostip.1*
%{_mandir}/man1/lss16toppm.1*
%{_mandir}/man1/ppmtolss16.1*
%{_mandir}/man1/syslinux.1*
%{_mandir}/man1/syslinux2ansi.1*

%files devel
%defattr(644,root,root,755)
%{_datadir}/%{name}/com32
