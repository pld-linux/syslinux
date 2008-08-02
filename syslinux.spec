Summary:	Simple bootloader
Summary(pl.UTF-8):	Prosty bootloader
Summary(pt_BR.UTF-8):	Carregador de boot simples
Summary(zh_CN.UTF-8):	Linux操作系统的启动管理器
Name:		syslinux
Version:	3.71
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.kernel.org/pub/linux/utils/boot/syslinux/%{name}-%{version}.tar.bz2
# Source0-md5:	a654fbb384279dbd80fb6295b65f34fc
URL:		http://syslinux.zytor.com/
BuildRequires:	nasm
BuildRequires:	perl-base
BuildRequires:	sed >= 4.0
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

sed -i 's/-march=i386//' sample/Makefile
sed -i 's/FPNG_NO_WRITE_SUPPORTED/DPNG_NO_WRITE_SUPPORTED/' com32/lib/MCONFIG

%build
rm -f ldlinux.{bin,bss,lst,sys}
%{__make} -j1 installer \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_includedir}}
install core/ldlinux.sys $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__make} -j1 install-all \
	INSTALLROOT=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir} \
	MANDIR=%{_mandir}

rm -fr $RPM_BUILD_ROOT/{boot,tftpboot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README* doc/*.txt
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/???[.a-z]*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_datadir}/%{name}/com32
