Summary:	Simple bootloader
Summary(pl):	Prosty bootloader
Summary(pt_BR):	Carregador de boot simples
Summary(zh_CN):	Linux操作系统的启动管理器
Name:		syslinux
Version:	3.31
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.kernel.org/pub/linux/utils/boot/syslinux/%{name}-%{version}.tar.bz2
# Source0-md5:	5faae89d18baf92e28bc820c62270db9
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

%description -l pl
SYSLINUX jest boot-loaderem dla Linuksa, kt髍y operuje na dyskietkach
z systemem plik體 MS-DOS. Jego przeznaczeniem jest uproszczenie
pierwszej instalacji Linuksa, dyskietki ratunkowe oraz inne rzeczy
zwi眤ane z dyskietkami. Dyskietka syslinuksowa mo縠 by� modyfikowana w
systemie MS-DOS (a tak縠 ka縟ym innym systemie z dost阷em do systemu
plik體 MS-DOS) gdy narz阣zia s� ju� stworzone, a tak縠 potrzebuje
tylko ~7K programu DOS-owego lub ~13K programu linuksowego do
stworzenia ich po raz pierwszy. Zawiera tak縠 program PXELINUX -
program s硊勘cy do bootowania serwera sieciowego poprzez Boot-PROM
kompatybilny ze specyfikacj� Intel PXE (Pre-Execution Environment).

%description -l pt_BR
SYSLINUX � um carregador de boot para o linux, operando em disquetes
com formata玢o DOS. Sua inten玢o � simplificar instala珲es do Linux,
discos de recupera玢o, e outros usos para disquetes de boot. Um
disquete SYSLINUX pode ser manipulado usando ferramentas padr鉶 do DOS
(ou qualquer sistema que possa acessar um filesystem DOS) e requer
somente um programa DOS de aproximadamente 7K ou linux de 13K para
cri�-lo na primeira vez.

Tamb閙 inclui o PXELINUX, um programa para boot remoto a partir de um
servidor de rede usando um boot PROM compat韛el com a especifica玢o
Intel PXE (Pre-Execution Environment).

%package devel
Summary:	Header files for syslinux libraries
Summary(pl):	Pliki nag丑wkowe bibliotek syslinux
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description devel
This package includes the header files needed for compilation of
applications that are making use of the syslinux internals. Install
this package only if you plan to develop or will need to compile
customized syslinux clients.

%description devel -l pl
Ten pakiet zawiera pliki nag丑wkowe potrzebne do kompilowania
aplikacji wykorzystuj眂ych kod syslinuksa. Nale縴 go instalowa� tylko
je秎i chcemy tworzy� lub kompilowa� w砤snych klient體 syslinuksa.

%prep
%setup -q
sed -i 's/-march=i386//' sample/Makefile
sed -i 's/FPNG_NO_WRITE_SUPPORTED/DPNG_NO_WRITE_SUPPORTED/' com32/lib/MCONFIG

%build
rm -f ldlinux.{bin,bss,lst,sys}
%{__make} installer \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name},%{_includedir}}
install ldlinux.sys $RPM_BUILD_ROOT%{_libdir}/%{name}

%{__make} install-all \
	INSTALLROOT=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

install extlinux/extlinux $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README* *.doc */*.doc
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/???[.a-z]*

%files devel
%defattr(644,root,root,755)
%{_libdir}/%{name}/com32
