Summary:	Simple bootloader
Summary(pl):	Prosty bootloader
Summary(pt_BR):	Carregador de boot simples
Summary(zh_CN):	Linux≤Ÿ◊˜œµÕ≥µƒ∆Ù∂Øπ‹¿Ì∆˜
Name:		syslinux
Version:	2.09
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.kernel.org/pub/linux/utils/boot/syslinux/%{name}-%{version}.tar.bz2
# Source0-md5:	703f11a01acf67a9f83ec082ca395565
Patch0:		%{name}-nowin32.patch
Patch1:		%{name}-cpp-comment.patch
URL:		http://syslinux.zytor.com/
BuildRequires:	perl
BuildRequires:	nasm
Requires:	mtools
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

%description -l pl
SYSLINUX jest boot-loaderem dla Linux'a, ktÛry operuje na dyskietkach
z systemem plikÛw MS-DOS. Jego przeznaczeniem jest uproszczenie
pierwszej instalacji Linux'a, dyskietki ratunkowe oraz inne rzeczy
zwi±zane z dyskietkami. Dyskietka SYSLINX'owa moøe byÊ modyfikowana w
systemie MS-DOS (a takøe kaødym innym systemie z dostÍpem do systemu
plikÛw MS-DOS) gdy narzÍdzia sa juø stworzone, a takøe potrzebuje
tylko ~7K programu DOS'owego lub ~13K programu Linux'owego do
stworzenia ich po raz pierwszy. Zawiera takøe program PXELINUX -
program s≥uø±cy do bootowania servera sieciowego poprzez Boot-PROM
kompatybilny ze specyfikacj± Intel PXE (Pre-Execution Environment).

%description -l pt_BR
SYSLINUX È um carregador de boot para o linux, operando em disquetes
com formataÁ„o DOS. Sua intenÁ„o È simplificar instalaÁıes do Linux,
discos de recuperaÁ„o, e outros usos para disquetes de boot. Um
disquete SYSLINUX pode ser manipulado usando ferramentas padr„o do DOS
(ou qualquer sistema que possa acessar um filesystem DOS) e requer
somente um programa DOS de aproximadamente 7K ou linux de 13K para
cri·-lo na primeira vez.

TambÈm inclui o PXELINUX, um programa para boot remoto a partir de um
servidor de rede usando um boot PROM compatÌvel com a especificaÁ„o
Intel PXE (Pre-Execution Environment).

%package libs
Summary:        syslinux shared libraries
Summary(pl):    Biblioteki wspÛ≥dzielone syslinux
Group:          Libraries

%description libs
syslinux shared libraries.

%description libs -l pl
Biblioteki wspÛ≥dzielone syslinux.

%package devel
Summary:        syslinux static libraries
Summary(pl):    Biblioteki statyczne syslinux
Summary(pt_BR): Bibliotecas est·ticas para desenvolvimento com openldap
Summary(ru):    Û‘¡‘…ﬁ≈”À…≈ ¬…¬Ã…œ‘≈À… syslinux
Summary(uk):    Û‘¡‘…ﬁŒ¶ ¬¶¬Ã¶œ‘≈À… syslinux
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}-%{release}

%description devel
This package includes the development libraries and header files
needed for compilation of applications that are making use of the syslinux
internals. Install this package only if you plan to develop or will
need to compile cutomized syslinux clients.

%description devel -l pl
Biblioteki statyczne syslinux.

%package static
Summary:        syslinux static libraries
Summary(pl):    Biblioteki statyczne syslinux
Summary(pt_BR): Bibliotecas est·ticas para desenvolvimento com openldap
Summary(ru):    Û‘¡‘…ﬁ≈”À…≈ ¬…¬Ã…œ‘≈À… syslinux
Summary(uk):    Û‘¡‘…ﬁŒ¶ ¬¶¬Ã¶œ‘≈À… syslinux
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}-%{release}

%description static
This package includes the development libraries and header files
needed for compilation of applications that are making use of the syslinux
internals.

%description static -l pl
Biblioteki statyczne syslinux.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} installer CC=%{__cc}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name},%{_includedir}}

%{__make} install install-lib \
	INSTALLROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README *.doc */*.doc
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}

%files libs
%defattr(644,root,root,755)
%{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.so
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
